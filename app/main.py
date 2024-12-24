import os, sys
from .utils.constants import logger
from .config.database import init_db
from .auth import user as user_auth
from app import demo
from .controllers import user as user_controllers
from .controllers import remote_repo as remote_repo_controller
from .services.github import GithubUtililty
from .services import backup
import subprocess

def db_connection():
    """Initialize the database connection"""
    try:
        init_db()
        logger.info('successfully established database connection')     
    except Exception as e:
        logger.error('error connecting to database:  %s' % e)

def is_git_installed():
    try:
        # Execute the 'git --version' command
        result = subprocess.run(['git', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            logger.info(f"Git is installed: {result.stdout.strip()}")
            return True
        else:
            logger.error("Git is not installed or not added to the system PATH.")
            return False
    except FileNotFoundError:
        # Exception when git command is not found
        logger.error("Git is not installed or not accessible.")
        return False

def handle_acc_creation():
    """Handle user registration and remote repo creation"""
    try:
        user = user_auth.register()
        github_obj = GithubUtililty()
        repo_name = 'upGIT' + '_' + user.name + '_' + str(user.id)
        
        created_repo = github_obj.create_repo(repo_name=repo_name)
        
        repo_object = {
            'name': created_repo.name,
            'user_id': user.id,
            'url': created_repo.html_url,
            'clone_url': created_repo.clone_url
        }
        """Save the repo to the database"""
        saved_repo = remote_repo_controller.save(repo_object)
        if saved_repo:
            logger.info(f'Successfully created remote repository for {created_repo.name} and saved it to the database')
        else:
            raise Exception('Failed to create remote repository')
    except Exception as e:
        logger.error('Error registering user and repo: %s' % e)
    
def main():    
    db_connection()
    if not is_git_installed():
        return
    
    print("1. create account\t 2. Login")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        handle_acc_creation()
    elif choice == 2:
        login_status = user_auth.login()
        
        if login_status[0]:
            """Redirect to the home page"""
            logger.info(f"successful login for {login_status[1].name}")
            backup_object = {
                'path': input('enter folder path: '),
                'backup_frequency': input('enter backup frequency(in hours, xh): '),
                'branch': input('enter branch name: ')
            }
            backup.new_backup(user=login_status[1], backup_object=backup_object)    
    
    # run the demo file
    # demo.run_demo()
    