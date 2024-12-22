"""A decorator method to handle the exceptions that may occur durring the crud"""
from .constants import logger
from ..config.database import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps #to maintain the function metadata when called

Session = sessionmaker(bind=engine)

def transaction_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Create a db session"""
        session = Session()
        try:
            # Perform database transaction
            result = func(session, *args, **kwargs)
            session.commit()
            session.refresh(result)
            return result
        except SQLAlchemyError as e:
            session.rollback()
            # Log the error
            logger.error(f"A database connection error occured: {e}")
            return None
        except Exception as e:
            session.rollback()
            logger.error(f"An unexpected error occurred during crud operation: {e}")
            return None
        finally:
            session.close()
            logger.info(f"Database session closed after {func.__name__}")
            
    return wrapper