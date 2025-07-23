from utils import log
from sqlalchemy.orm import Session
from . import models, schemas

def create_url(db: Session, url: schemas.UrlCreate):
    log(stack="backend", level="info", pkg="repository", message="create_url called")
    db_url = models.URL(original_url=url.original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url(db: Session, url_id: int):
    log(stack="backend", level="info", pkg="repository", message="get_url called")
    return db.query(models.URL).filter(models.URL.id == url_id).first()

def get_url_by_shortened(db: Session, shortened_url: str):
    log(stack="backend", level="info", pkg="repository", message="get_url_by_shortened called")
    return db.query(models.URL).filter(models.URL.shortened_url == shortened_url).first()

def get_urls(db: Session, skip: int = 0, limit: int = 10):
    log(stack="backend", level="info", pkg="repository", message="get_urls called")
    return db.query(models.URL).offset(skip).limit(limit).all()

def delete_url(db: Session, url_id: int):
    log(stack="backend", level="info", pkg="repository", message="delete_url called")
    db_url = db.query(models.URL).filter(models.URL.id == url_id).first()
    if db_url:
        db.delete(db_url)
        db.commit()
    return db_url