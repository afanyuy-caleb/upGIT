from ..schema.user import User
from ..controllers import remote_repo, branch, local_repo, local_branch
import os


def iterative_backup():
    """Backing up from the database"""
    
    
def new_backup(user : User, backup_object):
    # Get the remote repository id
    repo = remote_repo.get_specific(column='user_id', value=user.id, limit=1)
    if repo not in [None, False, '', []]:
        # verify whether or not the branch exists
        branch_name = backup_object['branch'].lower().replace(' ', '_')
        branch_exists = branch.get_specific(column='name', value=branch_name, limit=1)
        if branch_exists in [None, False, '', []]:
            """create the branch"""
            branch_object = {
                'name': branch_name,
                'remote_repo': repo.id
            } 
            created_branch = branch.save(branch_object)
            branch_id = created_branch.id                        
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
            created_folder = local_repo.save(folder_object)

            # save the local_branch
            local_branch_object = {
                'repo_id': created_folder.id,
                'branch_id': branch_id
            }
            saved_local_branch = local_branch.save(local_branch_object)
            
            # initialize git in folder
            
            # add a remote url (the clone url)
            
            # scan the files for those larger than 100MB and split into chunks if any
            
            # add to git
            
            # commit
            
            # push to remote branch if there is internet connection available

        