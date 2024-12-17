from ..models.branch import Branch as branch_model
from ..crud import branch as branch_crud
from ..utils.constants import logger

def save(branch_object):
    branch = branch_model(**branch_object)
    try:
        saved_repo = branch_crud.create(branch=branch)
        logger.info("Successfully created branch")
        return saved_repo
    except Exception as e:
        logger.error("Failed to create branch: %s" % e)
        return False

def get_all():
    print("\nGetting all branchs....") 
    try:
        branchs = branch_crud.get_all()
        logger.info(f"All branchs: {branchs}")
        return branchs
    except Exception as e:
        logger.error("Failed to get branchs: %s" % e)
        return False
        
def get_id():
    try:
        id = int(input("Enter the branch ID: "))
        branch = branch_crud.get_branch(id=id)
        logger.info(f"Successfully retrieved {branch}")
    except Exception as e:
        logger.error("Failed to get branchs: %s" % e)
        return False

def get_specific():
    try:
        column = input("Enter the column name: ")
        value = input("Enter the value: ")
        branchs = branch_crud.get_by_column(field=column, value=value)
        logger.info(f"Successfully retrieved branchs with {branchs}")
    except Exception as e:
        logger.error("Failed to get branchs: %s" % e)
        return False
  
def delete_branch():
    try:
        id = int(input("Enter the branch ID: "))
        deleted = branch_crud.delete(branch_id=id)
        logger.info(f"Successfully deleted branch with id {id}")
    except Exception as e:
        logger.error("Failed to delete branch: %s" % e)