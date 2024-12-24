from ..models.local_branch import LocalBranch as local_branch_model
from ..crud import local_branch as local_branch_crud
from ..utils.constants import logger

def save(local_branch_object):
    local_branch = local_branch_model(**local_branch_object)
    try:
        saved_repo = local_branch_crud.create(local_branch=local_branch)
        logger.info("Successfully created local_branch")
        return saved_repo
    except Exception as e:
        logger.error("Failed to create local_branch: %s" % e)
        return False

def get_all():
    try:
        local_branchs = local_branch_crud.get_all()
        logger.info(f"All local_branchs: {local_branchs}")
        return local_branchs
    except Exception as e:
        logger.error("Failed to get local_branchs: %s" % e)
        return False
        
def get_id(id: int):
    try:
        local_branch = local_branch_crud.get_local_branch(id=id)
        logger.info(f"Successfully retrieved {local_branch}")
        return local_branch
    except Exception as e:
        logger.error("Failed to get local_branchs: %s" % e)
        return False

def get_specific(column: str, value, limit=None):
    try:
        local_branchs = local_branch_crud.get_by_column(field=column, value=value, limit=limit)
        logger.info(f"Successfully retrieved local_branchs with {local_branchs}")
        return local_branchs
    except Exception as e:
        logger.error("Failed to get local_branchs: %s" % e)
        return False
  
def delete_local_branch(id):
    try:
        deleted = local_branch_crud.delete(local_branch_id=id)
        logger.info(f"Successfully deleted local_branch with id {id}")
        return deleted
    except Exception as e:
        logger.error("Failed to delete local_branch: %s" % e)
        return False