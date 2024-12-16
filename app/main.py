import os, sys
from .constants import logger
from .config.database import init_db
from .auth import user as user_auth
from app import demo
from .controllers import user as user_controllers
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
        
        repo_name = user.name + '_' + user.id
        print(repo_name)
        
    except Exception as e:
        logger.error('Error registering user and repo: %s' % e)
    
def main():
    db_connection()
    
    print("1. create account\t 2. Login")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        handle_acc_creation()
    elif choice == 2:
        login_status = user_auth.login()
        
        if login_status[0]:
            """Redirect to the home page"""
    
    
    # run the demo file
    # demo.run_demo()
    
    
        

