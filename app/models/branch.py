from sqlalchemy import Column, Integer, String, Text, ARRAY, DateTime, Enum, ForeignKey
from ..config.database import Base
from datetime import datetime
import bcrypt

class Branch(Base):
    """Branch model"""
    
    __tablename__ = "branches"
    
    """table attributes"""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    remote_repo = Column(Integer, ForeignKey('remoteRepos.id'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    """Method to be implemented"""
    def set_password(self) -> str:
        salt = bcrypt.gensalt()
        self.password = self.password.encode('utf-8')
        self.password = bcrypt.hashpw(self.password, salt=salt)
        self.password = self.password.decode('utf-8')
        
    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))
    
    def __repr__(self):
        """Return a string representation of the branch class"""
        return f"Branch(branch_name = {self.name}, branch_parent = {self.remote_repo}\n"

