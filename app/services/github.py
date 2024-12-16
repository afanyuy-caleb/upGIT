from github import Auth, Github
import os
from dotenv import load_dotenv

load_dotenv()

class GithubUtililty():
    def __init__(self):
        auth = Auth.Token(os.getenv('GITHUB_TOKEN'))
        gh = Github(auth=auth)
        self.user = gh.get_user()
    
    def create_repo(self):
        pass
    
    def get_repo(self, repo_name = None):
        for repo in self.user.get_repos():
            print(repo)
    
    def delete_repo(self, repo_name):
        pass