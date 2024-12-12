from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.user import User

def create(session: Session, user: User):
    """Create a new user in the database"""
    session.add(user)
    session.commit()
    session.close()
    

def get_all(session: Session, limit: int = 20, skip: int = 0):
    """Get all users from the database"""
    result = session.query(User).all()
    session.close()
    return result

def get_by_id(session: Session, id: int):
    """Get the users by the given id"""
    result = session.query(User).filter_by(id = id)
    session.close()
    return result