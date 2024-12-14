from sqlalchemy.orm import sessionmaker
from ..config.database import engine
from ..models.user import User as user_model
from ..schema.user import UserCreate
from ..crud import user as user_crud
from ..constants import logger

"""Create a db session"""
Session = sessionmaker(engine)
session = Session()

def register():
    print("\nCreating user....")
    user_object = {
        'name': input("username: "),
        'email': input("email: "),
        'password': input("password: "),
        'confirm_password': input("password confirmation: ")
    }
    try:
        """Validate the user information"""
        user = UserCreate(**user_object)
        user = user.dict()
        
        """remove the confirm password_field and Insert the user"""
        user.pop('confirm_password')
        model_object = user_model(**user)
        
        """hash the password field"""
        model_object.set_password()
        
        """Insert the new user"""
        created_user = user_crud.create(session, model_object)
        logger.info(f"User created without fault \n{created_user}")
        return True
        
    except Exception as e:
        logger.error(f"Error occured creating user {e}")
        return False
        
def login():
    print("\nGetting all users....") 
    user_info = {
        'email': input("email: "),
        'password': input("password: ")
    }
    try:
        user = user_crud.get_by_column(session, field='email', value=user_info["email"])
        
        print(user)
    except Exception as e:
        logger.error("Failed to get users: %s" % e)
        return False