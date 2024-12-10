from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from databases import Database
from sqlalchemy.orm import sessionmaker

import os, sys
from ..constants import logger, PATH_TO_DB

DATABASE_URL = "sqlite:///%s" % PATH_TO_DB

"""Create database variables"""
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

def init_db():
    """Initialize the database"""
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized successfully")

def connect_to_database():
    """Connect to the database"""
   
    
def disconnect_from_database():
    """disconnect from the database"""
