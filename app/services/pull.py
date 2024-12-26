from ..controllers import local_repo as local_repo_controller
from ..models.local_repo import LocalRepo

def pull(user_id, local_repo_id):
    """Pulls the latest changes from the remote repository."""
    condition = [LocalRepo.user_id == user_id, LocalRepo.id == local_repo_id]
    local_repo = local_repo_controller.get_conditional(condition=condition, limit=1)
    
    if local_repo:
        pass
    print(local_repo)
    