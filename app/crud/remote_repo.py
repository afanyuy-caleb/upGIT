from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.remote_repo import RemoteRepo
from ..utils.decorator import transaction_decorator

@transaction_decorator
def create(session, remote_repo: RemoteRepo):
    """Create a new remote_repo in the database"""
    session.add(remote_repo)
    return remote_repo

@transaction_decorator
def get_all(session, limit: int = 20, skip: int = 0):
    """Get all remote_repos from the database"""
    result = session.query(RemoteRepo).all()
    return result

@transaction_decorator
def get_remote_repo(session, id: int):
    """Get the remote_repos by the given id"""
    result = session.query(RemoteRepo).filter_by(id = id).one_or_none()
    return result

@transaction_decorator
def get_by_column(session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(RemoteRepo, field)
    condition = filter_column.like(f"%{value}%")
    if limit == 1:
        return session.query(RemoteRepo).filter(condition).first()
    result = session.query(RemoteRepo).filter(condition).all()
    return result

@transaction_decorator
def delete(session, remote_repo_id: int):
    remote_repo_to_delete = session.query(RemoteRepo).filter_by(id=remote_repo_id).one_or_none()
    if remote_repo_to_delete:
        session.delete(remote_repo_to_delete)   
        return remote_repo_to_delete
    else:
        raise Exception(f"Couldn't find remote_repo with id {remote_repo_id}")
                    