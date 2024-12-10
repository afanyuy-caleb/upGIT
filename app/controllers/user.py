from sqlalchemy.orm import sessionmaker
from ..config.database import engine
from ..models.user import User
from ..crud.user import *
from ..constants import logger

"""Create a db session"""
Session = sessionmaker(engine)
session = Session()

def create_user():
    print("\nCreating user....")
    name = input("username: ")
    email = input("email: ")
    password = input("password: ")
    
    """Generate a new user"""
    user = User(name=name, email=email, password=password)
    user.set_password(password)
    
    """Insert the new user"""
    
    try:    
        create(session, user)
        logger.info("User created without fault")
    except Exception as e:
        logger.error("Failed to create user: %s" % e)
        
def get_users():
    print("\nGetting all users....")
    
    try:
        users = get_all(session)
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    except Exception as e:
        logger.error("Failed to get users: %s" % e)