import os
from ..utils.constants import logger
from ..controllers import file as file_controller

"""add a to-be-deleted array that contains the dir_paths of all the chunks to be deleted after commit"""

to_be_deleted = []
main_dir = None
def organize_files(dir_path, folder_id, subdir=False):
    global to_be_deleted
    global main_dir
    try:
        if not subdir:
            main_dir = dir_path 
        file_list = os.listdir(dir_path)
        
        for file in file_list:
            if file == ".git":
                continue
            file_path = os.path.join(dir_path, file)  
            if os.path.isdir(file_path):
                organize_files(file_path, folder_id, subdir=True)
            
            # check file size
            file_size = os.path.getsize(file_path)
            if file_size > 1 * 1024 * 1024:
                filename = os.path.basename(file_path)
                chunk_dir = os.path.dirname(file_path)
                
                """ignore the file"""
                gitignore_path = os.path.join(os.path.dirname(file_path), '.gitignore')
                with open(gitignore_path, 'a') as gitignore_file:
                    gitignore_file.write(f"{filename}\n")
                
                """split the file"""
                chunk_folder_name = os.path.splitext(filename)[0].capitalize() + '_UPGIT_CHUNKS'
                chunk_dir = os.path.join(chunk_dir, chunk_folder_name)
                if not os.path.exists(chunk_dir):
                    os.mkdir(chunk_dir)
                
                to_be_deleted.append(chunk_dir)
                chunk_size = 1 * 1024 *1024
                split(file_path, chunk_dir, chunk_size)
                
                """save file to db"""
                file_object = {
                    'name': filename,
                    'repo_id': folder_id,
                    'size': file_size,
                    'filepath': file_path
                }
                file_controller.save(file_object)
                    
        return to_be_deleted
    except Exception as e:
        logger.error(f"An error occurred while organizing files: {e}")
        return None

def split(filepath, chunk_dir, chunk_size):
    with open(filepath, 'rb') as file:
        chunk_number = 1
        while chunk := file.read(chunk_size):
            chunk_name = os.path.basename(filepath) + f"part_{chunk_number}"
            with open(os.path.join(chunk_dir, chunk_name), 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_number += 1
        # log the progress
        logger.info(f"{chunk_number-1} chunks of {os.path.basename(filepath)} have been created")

            