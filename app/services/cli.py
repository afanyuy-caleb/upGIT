import os, sys
import subprocess
from ..utils.decorator import cli_decorator
from .manage_files import organize_files
import shutil
from ..utils.constants import logger
import socket

class CLI():
    def __init__(self, local_dir_id, remote_url, branch_name, local_dir=None):
        if local_dir:
            self.local_dir = local_dir
        self.remote_url = remote_url
        self.branch_name = branch_name
        
        self.chunk_dirs = organize_files(dir_path=self.local_dir, folder_id=local_dir_id)
        self.init_git()
        self.add_remote()
        self.create_branch()
        self.add()
        self.commit()
        self.delete_chunk()
        self.push()
    
    @cli_decorator
    def init_git(self):
        result = subprocess.run(['git', 'init'], cwd=self.local_dir, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    
    @cli_decorator
    def add_remote(self):
        result = subprocess.run(['git', 'remote', '-v'], cwd=self.local_dir, capture_output=True, check=True, text=True)
        
        if self.remote_url not in result.stdout.strip():
            result = subprocess.run(['git', 'remote', 'add', 'origin', self.remote_url], cwd=self.local_dir, capture_output=True, check=True, text=True)  
        return result.stdout.strip()
    
    @cli_decorator
    def create_branch(self):
        # check if branch exists
        result = subprocess.run(['git', 'branch', '--list', self.branch_name], cwd=self.local_dir, capture_output=True, check=True, text=True)
        if self.branch_name not in result.stdout:    
            result = subprocess.run(['git', 'checkout', '-b', self.branch_name], cwd=self.local_dir, capture_output=True, check=True)
        return result.stdout.strip()
    
    @cli_decorator
    def add(self):
        result = subprocess.run(['git', 'add', '.'], cwd=self.local_dir, capture_output=True, check=True, text=True)
        return result.stdout.strip()
    
    @cli_decorator
    def commit(self, message="successful backup"):
        result = subprocess.run(['git', 'commit', '-m', message], cwd=self.local_dir, capture_output=True, check=True, text=True)
        return result.stdout.strip()
    
    def delete_chunk(self):
        for dir in self.chunk_dirs:
            if os.path.exists(dir):
                shutil.rmtree(dir)
                logger.info(f"successfully Deleted {dir}")

    def is_connected(self):
        try:
            # Perform a DNS lookup to check for internet connectivity
            socket.gethostbyname("www.google.com")
            return True
        except socket.error:
            return False
    
    @cli_decorator
    def push(self):
        """Push to git if there is internet connectivity"""
        if self.is_connected():
            result = subprocess.run(['git', 'push', 'origin', self.branch_name], cwd=self.local_dir, capture_output=True, check=True, text=True)
            logger.info("commit successfully pushed")
            return result.stdout.strip()
        else:
            raise Exception("no internet connection found, push failed")

    # push to remote branch if there is internet connection available