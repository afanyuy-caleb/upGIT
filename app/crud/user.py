from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.user import User
from ..schema.user import UserUpdate
from ..utils.decorator import transaction_decorator

@transaction_decorator
def create(session, user: User):
    """Create a new user in the database"""
    session.add(user)
    return user

@transaction_decorator
def get_all(session, limit: int = 20, skip: int = 0):
    """Get all users from the database"""
    result = session.query(User).all()
    return result

@transaction_decorator
def get_user(session, id: int):
    """Get the users by the given id"""
    result = session.query(User).filter_by(id = id).one_or_none()
    return result

@transaction_decorator
def get_by_column(session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(User, field)
    condition = filter_column.like(f"%{value}%")
    return session.query(User).filter(condition).all()

@transaction_decorator
def get_by_email(session, email: str):
    """Login a user by their email"""
    user = session.query(User).filter_by(email=email).one_or_none()
    return user

@transaction_decorator
def update(session, user_id: int, user: UserUpdate):
    """Update the user with the given id"""
    user_to_update = session.query(User).filter_by(id=user_id).one_or_none()
    if user_to_update:   
        for key, value in user.dict().items():
            if value is not None:
                setattr(user_to_update, key, value)
        if user.dict().get('password'):
            user_to_update.set_password()    
        return True
    else:
        raise Exception(f"Couldn't find user with id {user_id}")

@transaction_decorator
def delete(session, user_id: int):
    user_to_delete = session.query(User).filter_by(id=user_id).one_or_none()
    if user_to_delete:
        session.delete(user_to_delete)  
        return user_to_delete
    else:
        raise Exception(f"Couldn't find user with id {user_id}")
                    