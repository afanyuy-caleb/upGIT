from sqlalchemy import select
from ..models.branch import Branch
from ..utils.decorator import transaction_decorator

@transaction_decorator
def create(session, branch: Branch):
    """Create a new branch in the database"""
    session.add(branch)
    return branch

@transaction_decorator
def get_all(session, limit: int = 20, skip: int = 0):
    """Get all branchs from the database"""
    result = session.query(Branch).all()
    return result

@transaction_decorator
def get_branch(session, id: int):
    """Get the branchs by the given id"""
    result = session.query(Branch).filter_by(id = id).one_or_none()
    return result

@transaction_decorator
def get_by_column(session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(Branch, field)
    condition = filter_column.like(f"%{value}%")
    return session.query(Branch).filter(condition).all()

@transaction_decorator
def delete(session, branch_id: int):
    branch_to_delete = session.query(Branch).filter_by(id=branch_id).one_or_none()
    if branch_to_delete:
        session.delete(branch_to_delete)
        return branch_to_delete
    else:
        raise Exception(f"Couldn't find branch with id {branch_id}")
                    