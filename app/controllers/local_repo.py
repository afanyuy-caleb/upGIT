from ..models.local_repo import LocalRepo as local_repo_model
from ..crud import local_repo as local_repo_crud
from ..utils.constants import logger

def save(local_repo_object):
    local_repo = local_repo_model(**local_repo_object)
    try:
        saved_repo = local_repo_crud.create(local_repo=local_repo)
        logger.info("Successfully created local_repo")
        return saved_repo
    except Exception as e:
        logger.error("Failed to create local_repo: %s" % e)
        return False

def get_all():
    try:
        local_repos = local_repo_crud.get_all()
        logger.info(f"All local_repos: {local_repos}")
        return local_repos
    except Exception as e:
        logger.error("Failed to get local_repos: %s" % e)
        return False
        
def get_id(id):
    try:
        local_repo = local_repo_crud.get_local_repo(id=id)
        logger.info(f"Successfully retrieved {local_repo}")
        return local_repo
    except Exception as e:
        logger.error("Failed to get local_repos: %s" % e)
        return False

def get_specific(column: str, value, limit=None):
    try:
        local_repos = local_repo_crud.get_by_column(field=column, value=value, limit=limit)
        logger.info(f"Successfully retrieved local_repos with {local_repos}")
        return local_repos
    except Exception as e:
        logger.error("Failed to get local_repos: %s" % e)
        return False

def get_conditional(condition, limit=None):
    try:
        local_repos = local_repo_crud.get_by_condition(condition=condition, limit=limit)
        logger.info(f"Successfully retrieved local_repos with {local_repos}")
        return local_repos
    except Exception as e:
        logger.error("Failed to get local_repos: %s" % e)
        return False
    
def delete_local_repo(id):
    try:
        deleted = local_repo_crud.delete(local_repo_id=id)
        logger.info(f"Successfully deleted local_repo with id {id}")
        return deleted
    except Exception as e:
        logger.error("Failed to delete local_repo: %s" % e)
        return False