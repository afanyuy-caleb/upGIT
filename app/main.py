import os, sys
import threading
from app.utils.constants import logger
from app.config.database import init_db
from app.auth import user as user_auth
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
    
    # Launch the main app
    MainApp()
    
    # The pull functionality
    # pull.pull(user_id=1, local_repo_id=4, branch_id=3)
    

    