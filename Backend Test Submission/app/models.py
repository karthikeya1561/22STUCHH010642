from utils import log

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def log_model_operation(operation: str):
    log(stack="models.py", level="INFO", pkg="models", message=f"{operation} called")


class URLMapping(Base):
    __tablename__ = 'url_mappings'

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, nullable=False)