from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.remote_repo import RemoteRepo

def create(session: Session, remote_repo: RemoteRepo):
    """Create a new remote_repo in the database"""
    session.add(remote_repo)
    session.commit()
    session.close()
    return remote_repo

def get_all(session: Session, limit: int = 20, skip: int = 0):
    """Get all remote_repos from the database"""
    result = session.query(RemoteRepo).all()
    session.close()
    return result

def get_remote_repo(session: Session, id: int):
    """Get the remote_repos by the given id"""
    result = session.query(RemoteRepo).filter_by(id = id).one_or_none()
    session.close()
    return result

def get_by_column(session: Session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(RemoteRepo, field)
    condition = filter_column.like(f"%{value}%")
    return session.query(RemoteRepo).filter(condition).all()

def delete(session: Session, remote_repo_id: int):
    remote_repo_to_delete = session.query(RemoteRepo).filter_by(id=remote_repo_id).one_or_none()
    if remote_repo_to_delete:
        session.delete(remote_repo_to_delete)
        session.commit()
        return remote_repo_to_delete
    else:
        raise Exception(f"Couldn't find remote_repo with id {remote_repo_id}")
                    