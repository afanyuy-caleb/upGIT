from ..models.file import File as file_model
from ..crud import file as file_crud
from ..utils.constants import logger

def save(file_object):
    file = file_model(**file_object)
    try:
        saved_repo = file_crud.create(file=file)
        logger.info("Successfully created file")
        return saved_repo
    except Exception as e:
        logger.error("Failed to create file: %s" % e)
        return False

def get_all():
    print("\nGetting all files....") 
    try:
        files = file_crud.get_all()
        logger.info(f"All files: {files}")
        return files
    except Exception as e:
        logger.error("Failed to get files: %s" % e)
        return False
        
def get_id():
    try:
        id = int(input("Enter the file ID: "))
        file = file_crud.get_file(id=id)
        logger.info(f"Successfully retrieved {file}")
    except Exception as e:
        logger.error("Failed to get files: %s" % e)
        return False

def get_specific():
    try:
        column = input("Enter the column name: ")
        value = input("Enter the value: ")
        files = file_crud.get_by_column(field=column, value=value)
        logger.info(f"Successfully retrieved files with {files}")
    except Exception as e:
        logger.error("Failed to get files: %s" % e)
        return False
  
def delete_file():
    try:
        id = int(input("Enter the file ID: "))
        deleted = file_crud.delete(file_id=id)
        logger.info(f"Successfully deleted file with id {id}")
    except Exception as e:
        logger.error("Failed to delete file: %s" % e)