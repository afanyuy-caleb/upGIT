from loguru import logger
import os, sys

from .constants import logger
from .config.database import (
    init_db,
    connect_to_database,
    disconnect_from_database
)

from .controllers import user as user_controller

def db_connection():
    """Initialize the database connection"""
    try:
        init_db()
        logger.info('successfully established database connection')     
    except Exception as e:
        logger.error('error connecting to database:  %s' % e)


def main():
    db_connection()
    print("\nHi there! Welcome to this mini sqlalchemy demo. Kindly choose an option")        
    print("1. create a user\t 2. select all users\t")
    choice = int(input("Enter your choice: "))
    
    while choice not in range(1, 3):
        choice = int(input("Enter your choice: "))
    
    if choice == 1:
        user_controller.create_user()
    else:
        user_controller.get_users()