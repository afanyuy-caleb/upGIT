from sqlalchemy.orm import sessionmaker
from ..config.database import engine
from ..models.remote_repo import RemoteRepo as remote_repo_model
from ..crud import remote_repo as remote_repo_crud
from ..constants import logger

"""Create a db session"""
Session = sessionmaker(engine)
session = Session()
        
def save(remote_repo_object):
    remote_repo = remote_repo_model(**remote_repo_object)
    try:
        saved_repo = remote_repo_crud.create(session, remote_repo)
        logger.info("Successfully created remote_repo")
        return saved_repo
    except Exception as e:
        logger.error("Failed to create remote_repo: %s" % e)
        return False

def get_all():
    print("\nGetting all remote_repos....") 
    try:
        remote_repos = remote_repo_crud.get_all(session)
        logger.info(f"All remote_repos: {remote_repos}")
        return remote_repos
    except Exception as e:
        logger.error("Failed to get remote_repos: %s" % e)
        return False
        
def get_id():
    try:
        id = int(input("Enter the remote_repo ID: "))
        remote_repo = remote_repo_crud.get_remote_repo(session, id)
        logger.info(f"Successfully retrieved {remote_repo}")
    except Exception as e:
        logger.error("Failed to get remote_repos: %s" % e)
        return False

def get_specific():
    try:
        column = input("Enter the column name: ")
        value = input("Enter the value: ")
        remote_repos = remote_repo_crud.get_by_column(session, column, value)
        logger.info(f"Successfully retrieved remote_repos with {remote_repos}")
    except Exception as e:
        logger.error("Failed to get remote_repos: %s" % e)
        return False
  
def delete_remote_repo():
    try:
        id = int(input("Enter the remote_repo ID: "))
        deleted = remote_repo_crud.delete(session, id)
        logger.info(f"Successfully deleted remote_repo with id {id}")
    except Exception as e:
        logger.error("Failed to delete remote_repo: %s" % e)