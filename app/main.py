import os, sys
from .utils.constants import logger
from .config.database import init_db
from .auth import user as user_auth
from app import demo
from .controllers import user as user_controllers
from .controllers import remote_repo as remote_repo_controller
from .services.github import GithubUtililty

def db_connection():
    """Initialize the database connection"""
    try:
        init_db()
        logger.info('successfully established database connection')     
    except Exception as e:
        logger.error('error connecting to database:  %s' % e)

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
    # db_connection()
    
    # print("1. create account\t 2. Login")
    # choice = int(input("Enter your choice: "))
    
    # if choice == 1:
    #     handle_acc_creation()
    # elif choice == 2:
    #     login_status = user_auth.login()
        
    #     if login_status[0]:
    #         """Redirect to the home page"""
    
    # run the demo file
    demo.run_demo()
    