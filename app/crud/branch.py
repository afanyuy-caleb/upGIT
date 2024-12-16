from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.branch import Branch

def create(session: Session, branch: Branch):
    """Create a new branch in the database"""
    session.add(branch)
    session.commit()
    session.close()
    return branch

def get_all(session: Session, limit: int = 20, skip: int = 0):
    """Get all branchs from the database"""
    result = session.query(Branch).all()
    session.close()
    return result

def get_branch(session: Session, id: int):
    """Get the branchs by the given id"""
    result = session.query(Branch).filter_by(id = id).one_or_none()
    session.close()
    return result

def get_by_column(session: Session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(Branch, field)
    condition = filter_column.like(f"%{value}%")
    return session.query(Branch).filter(condition).all()

def delete(session: Session, branch_id: int):
    branch_to_delete = session.query(Branch).filter_by(id=branch_id).one_or_none()
    if branch_to_delete:
        session.delete(branch_to_delete)
        session.commit()
        return branch_to_delete
    else:
        raise Exception(f"Couldn't find branch with id {branch_id}")
                    