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

def get_operations(model: str):
    return [f'create a {model}', f'get all {model}s', f'get {model} by id', f'get {model} by specific column', f'update {model}', f'delete {model}']

def main():
    db_connection()
    operation_handler = [{
        "method": [user_controller.create_user, user_controller.get_users]
        },
        {
        "method": [user_controller.create_user, user_controller.get_users]
        },
        {
        "method": [user_controller.create_user, user_controller.get_users]
        }
    ]
    models = ['user', 'file', 'repo']
    print("\nHi there! Welcome to this mini sqlalchemy demo. \nWhich model do you want to work on?")
    print("1. user\t 2. file\t 3. repository\t")
    model = int(input("Enter your choice: "))
    
    try:
        operations = get_operations(models[model - 1])
        print("\nWhich operation do you want to perform?")
        op_num = 1
        for operation in operations:
            print (f"{op_num}.  {operation}")
            op_num += 1
        operation = int(input("Enter your choice: "))
        
        while operation not in range(1, len(operations)):
            operation = int(input("Enter your choice: "))
        
        operation_handler[model - 1]['method'][operation - 1]()
    
    except IndexError as e:
        logger.error("Invalid choice: %s" % e)
        quit()
    
    except Exception as e:
        logger.error("An error occurred: %s" % e)
        quit()
        

