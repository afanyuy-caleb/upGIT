from ..schema.user import User
from ..controllers import remote_repo, branch, local_repo, local_branch
import os
from .cli import CLI

def iterative_backup(user_id):
    """Backing up from the database"""
    
    
def new_backup(user : User, backup_object):
    # Get the remote repository id
    repo = remote_repo.get_specific(column='user_id', value=user.id, limit=1)
    if repo not in [None, False, '', []]:
        # verify whether or not the branch exists
        branch_name = backup_object['branch'].lower().replace(' ', '_')
        branch_exists = branch.get_specific(column='name', value=branch_name, limit=1)
        
        is_new_branch = False
        is_new_folder = False
        
        if branch_exists in [None, False, '', []]:
            """create the branch"""
            branch_object = {
                'name': branch_name,
                'remote_repo': repo.id
            } 
            created_branch = branch.save(branch_object)
            branch_id = created_branch.id  
            is_new_branch = True                      
        else:
            branch_id = branch_exists.id
        # create the folder
        if os.path.isdir(backup_object['path']):
            # create folder
            folder_object = {
                'name': backup_object['path'],
                'user_id': user.id,
                'backup_frequency': backup_object['backup_frequency']
            }
            created_folder = local_repo.get_specific(column='name', value=backup_object['path'], limit=1)
            if created_folder in [None, False, '', []]:
                created_folder = local_repo.save(folder_object)
                is_new_folder = True

            # save the local_branch
            local_branch_object = {
                'repo_id': created_folder.id,
                'branch_id': branch_id
            }
            if is_new_folder or is_new_branch:
                local_branch.save(local_branch_object)
                
            cli = CLI(local_dir=created_folder.name, local_dir_id=created_folder.id, remote_url=repo.clone_url, branch_name=branch_name)
