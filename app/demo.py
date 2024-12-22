from .utils.constants import logger
from .auth import user as user_auth
from .controllers import user as user_controller
from .controllers import branch as branch_controller
from .controllers import remote_repo as remote_controller
from .controllers import file as file_controller
from .controllers import local_repo as local_repo_controller
from .controllers import local_branch as local_branch_controller

def get_operations(model: str):
    return [f'create a {model}', f'get all {model}s', f'get {model} by id', f'get {model} by specific column', f'update {model}', f'delete {model}']


def run_demo():
    operation_handler = [{
        "model": 'user',
        "methods": [user_auth.register, user_controller.get_all, user_controller.get_id, user_controller.get_specific, user_controller.update_user, user_controller.delete_user]
        },
        {
        "model": 'file',
        "methods": [file_controller.save, file_controller.get_all, file_controller.get_id, file_controller.get_specific, file_controller.delete_file]
        },
        {
        "model": 'branch',
        "methods": [branch_controller.save, branch_controller.get_all, branch_controller.get_id, branch_controller.get_specific, branch_controller.delete_branch]
        },
        {
        "model": 'remote_repo',
        "methods": [remote_controller.save, remote_controller.get_all, remote_controller.get_id, remote_controller.get_specific, remote_controller.delete_remote_repo]
        },
        {
        "model": 'local_repo',
        "methods": [local_repo_controller.save, local_repo_controller.get_all, local_repo_controller.get_id, local_repo_controller.get_specific, local_repo_controller.delete_local_repo]
        },
        {
        "model": 'local_branch',
        "methods": [local_branch_controller.save, local_branch_controller.get_all, local_branch_controller.get_id, local_branch_controller.get_specific, local_branch_controller.delete_local_branch]
        }
    ]
    models = [operation['model'] for operation in operation_handler]
    print("\nHi there! Welcome to this mini sqlalchemy demo. \nWhich model do you want to work on?")
    
    model_string = ''
    num = 1
    for model in models:
        model_string += str(num)+ '. '+model+ '\t '
        num += 1
    print(model_string)
    model = int(input("Enter your choice: "))
    
    try:
        operations = get_operations(models[model - 1])
        print("\nWhich operation do you want to perform?")
        op_num = 1
        for operation in operations:
            print (f"{op_num}.  {operation}")
            op_num += 1
        operation = int(input("Enter your choice: "))
        while operation not in range(1, len(operations)+1):
            operation = int(input("Enter your choice: "))
        
        #call the associate function to run
        operation_handler[model - 1]['methods'][operation - 1]()
    except IndexError as e:
        logger.error("Invalid choice: %s" % e)
        quit()
    except Exception as e:
        logger.error("An error occurred: %s" % e)
        quit()