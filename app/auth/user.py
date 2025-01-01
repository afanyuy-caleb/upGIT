from ..models.user import User as user_model
from ..schema.user import UserCreate
from ..crud import user as user_crud
from ..utils.constants import logger
import os

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
        created_user = user_crud.create(user=model_object)
        
        # write the user id to flat file
        with open(os.path.join(os.path.dirname(__file__), 'user_id.txt'), 'w') as f:
            f.write(str(created_user.id))
        
        logger.info(f"User created without fault \n{created_user}")
        return created_user
        
    except Exception as e:
        logger.error(f"Error occured creating user {e}")
        return False
        
def login():
    print("\nPlease login into your account") 
    user_info = {
        'email': input("email: "),
        'password': input("password: ")
    }
    try:
        user = user_crud.get_by_email(email=user_info["email"])
        if user:
            if user.check_password(user_info["password"]): 
                logger.info(f"User, {user.name} logged in successfully")
                return True, user
        logger.error(f"Incorrect email or password")
        return False, "Incorrect email or password"
    except Exception as e:
        logger.error("Failed to authenticate user: %s" % e)
        return False