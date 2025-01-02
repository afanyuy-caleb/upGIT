import os, sys
import threading
from app.utils.constants import logger
from app.config.database import init_db
from app.auth import user as user_auth
from app import demo
from app.controllers import (
    user as user_controllers,
    remote_repo as remote_repo_controller,
    local_repo as local_repo_controller
)
from app.services.github import GithubUtililty
from app.services import initial_backup, pull, background_backup
from app.views.view import MainApp
from app.utils.decorator import global_exception_handler

def start_backup_thread():
    """Start the backup thread"""
    backup_thread = threading.Thread(target=background_backup.bg_backup())
    backup_thread.daemon = True
    backup_thread.start()

@global_exception_handler
def db_connection():
    """Initialize the database connection"""
    init_db()
    
def main():    
    db_connection()
    # start_backup_thread()
    app = MainApp()
    
    # print("1. create account\t 2. Login")
    # choice = int(input("Enter your choice: "))
    
    # if choice == 1:
    #     handle_acc_creation()

    # login_status = user_auth.login()
    
    # if login_status[0]:
    #     """Redirect to the home page"""
    #     logger.info(f"successful login for {login_status[1].name}")
    #     print("1. backup\t 2. recover latest backup")
    #     choice = int(input("Enter your choice: "))

    #     if choice == 2:
    #         pull_object = {
    #             'user_id': int(input("Enter user id: ")),
    #             'local_repo_id': int(input("Enter local repo id: ")),
    #             'branch_id': int(input("Enter branch id: "))
    #         }
    #         pull.pull(**pull_object)
    #     else:
    #         backup_object = {
    #             'path': input('enter folder path: '),
    #             'backup_frequency': input('enter backup frequency(in hours, xh): '),
    #             'branch_name': input('enter branch name: ')
    #         }
    #         initial_backup.new_backup(user=login_status[1], backup_object=backup_object)    
        
    # run the demo file
    # demo.run_demo()
    