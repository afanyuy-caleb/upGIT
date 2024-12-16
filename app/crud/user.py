from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.user import User
from ..schema.user import UserUpdate

def create(session: Session, user: User):
    """Create a new user in the database"""
    session.add(user)
    session.commit()
    session.close()
    return user

def get_all(session: Session, limit: int = 20, skip: int = 0):
    """Get all users from the database"""
    result = session.query(User).all()
    session.close()
    return result

def get_user(session: Session, id: int):
    """Get the users by the given id"""
    result = session.query(User).filter_by(id = id).one_or_none()
    session.close()
    return result

def get_by_column(session: Session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(User, field)
    condition = filter_column.like(f"%{value}%")
    return session.query(User).filter(condition).all()

def get_by_email(session: Session, email: str):
    """Login a user by their email"""
    user = session.query(User).filter_by(email=email).one_or_none()
    return user

def update(session: Session, user_id: int, user: UserUpdate):
    """Update the user with the given id"""
    user_to_update = session.query(User).filter_by(id=user_id).one_or_none()
    if user_to_update:   
        for key, value in user.dict().items():
            if value is not None:
                setattr(user_to_update, key, value)
        if user.dict().get('password'):
            user_to_update.set_password()    
        session.commit()
        session.close()
        return True
    else:
        raise Exception(f"Couldn't find user with id {user_id}")

def delete(session: Session, user_id: int):
    user_to_delete = session.query(User).filter_by(id=user_id).one_or_none()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        return user_to_delete
    else:
        raise Exception(f"Couldn't find user with id {user_id}")
                    