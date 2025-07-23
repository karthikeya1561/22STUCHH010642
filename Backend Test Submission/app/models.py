from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URLMapping(Base):
    __tablename__ = 'url_mappings'

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, nullable=False)