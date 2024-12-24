from sqlalchemy import select
from ..models.file import File
from ..utils.decorator import transaction_decorator

@transaction_decorator
def create(session, file: File):
    """Create a new file in the database"""
    session.add(file)
    return file

@transaction_decorator
def get_all(session, limit: int = 20, skip: int = 0):
    """Get all files from the database"""
    result = session.query(File).all()
    return result

@transaction_decorator
def get_file(session, id: int):
    """Get the files by the given id"""
    result = session.query(File).filter_by(id = id).one_or_none()
    return result

@transaction_decorator
def get_by_column(session, field:str, value, skip:int=0, limit: int=10):
    filter_column = getattr(File, field)
    condition = filter_column.like(f"%{value}%")
    if limit == 1:
        return session.query(File).filter(condition).first()
    return session.query(File).filter(condition).all()

@transaction_decorator
def delete(session, file_id: int):
    file_to_delete = session.query(File).filter_by(id=file_id).one_or_none()
    if file_to_delete:
        session.delete(file_to_delete)
        return file_to_delete
    else:
        raise Exception(f"Couldn't find file with id {file_id}")
                    