from sqlalchemy import Column, Integer, String, Text, ARRAY, DateTime, Enum, ForeignKey
from ..config.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime
import bcrypt

class User(Base):
    """User model"""
    
    __tablename__ = "users"
    
    """table attributes"""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    
    """Method to be implemented"""
    def set_password(self, plain_password: str) -> str:
        salt = bcrypt.gensalt()
        plain_password = plain_password.encode('utf-8')
        self.password = bcrypt.hashpw(plain_password, salt=salt)
        self.password = self.password.decode('utf-8')
        
    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))
    
    def __repr__(self):
        """Return a string representation of the user class"""
        return f"\n<user_name = {self.name}, user_email = {self.email}, user_password = {self.password}>\n"

