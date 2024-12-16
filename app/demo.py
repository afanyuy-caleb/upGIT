from .constants import logger
from .auth import user as user_auth
from .controllers import user as user_controllers

def get_operations(model: str):
    return [f'create a {model}', f'get all {model}s', f'get {model} by id', f'get {model} by specific column', f'update {model}', f'delete {model}']


def run_demo():
    operation_handler = [{
        "method": [user_auth.register, user_controllers.get_all, user_controllers.get_id, user_controllers.get_specific, user_controllers.update_user, user_controllers.delete_user]
        },
        {
        "method": [user_auth.register, user_controllers.get_all]
        },
        {
        "method": [user_auth.register, user_controllers.get_all]
        }
    ]
    models = ['user', 'file', 'repo']
    print("\nHi there! Welcome to this mini sqlalchemy demo. \nWhich model do you want to work on?")
    print("1. user\t 2. file\t 3. repository\t")
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
            
        operation_handler[model - 1]['method'][operation - 1]()
    except IndexError as e:
        logger.error("Invalid choice: %s" % e)
        quit()
    except Exception as e:
        logger.error("An error occurred: %s" % e)
        quit()