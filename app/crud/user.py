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
    # query = select(User).offset(skip).limit(limit)
    result = session.query(User).filter_by(name = 'test user')
    session.close()
    return result