from sqlalchemy.orm import sessionmaker
from ..config.database import engine
from ..models.user import User as user_model
from ..schema.user import UserUpdate
from ..crud import user as user_crud
from ..constants import logger

"""Create a db session"""
Session = sessionmaker(engine)
session = Session()
        
def get_all():
    print("\nGetting all users....") 
    try:
        users = user_crud.get_all(session)
        logger.info(f"All users: {users}")
        return users
    except Exception as e:
        logger.error("Failed to get users: %s" % e)
        return False
        
        
def get_id():
    try:
        id = int(input("Enter the user ID: "))
        user = user_crud.get_user(session, id)
        logger.info(f"Successfully retrieved {user}")
    except Exception as e:
        logger.error("Failed to get users: %s" % e)
        return False

def get_specific():
    try:
        column = input("Enter the column name: ")
        value = input("Enter the value: ")
        users = user_crud.get_by_column(session, column, value)
        logger.info(f"Successfully retrieved users with {users}")
        
    except Exception as e:
        logger.error("Failed to get users: %s" % e)
        return False

def update_user():
    try:
        id = int(input("Enter the user ID: "))
        user_object = {
            'name': input("username: "),
            'email': input("email: "),
            'password': input("password: ")
        }
        """trim the object of empty fields"""
        user_object = {key : value for key, value in user_object.items() if value not in [None, '', []] }
        
        user = UserUpdate(**user_object)
        updated_user = user_crud.update(session, id, user)
        print(updated_user)
        logger.info(f"Successfully updated user with id {id}")

    except Exception as e:
        logger.error("Failed to update user: %s" % e)
        
def delete_user():
    try:
        id = int(input("Enter the user ID: "))
        deleted = user_crud.delete(session, id)
        logger.info(f"Successfully deleted user with id {id}")

    except Exception as e:
        logger.error("Failed to delete user: %s" % e)