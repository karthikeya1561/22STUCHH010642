
from fastapi import APIRouter, HTTPException, Depends
from utils import log
from typing import List
from app.schemas import UrlCreate, UrlResponse
from app.crud import create_url, get_url, get_urls
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/urls/", response_model=UrlResponse)
async def shorten_url(url: UrlCreate):
    log(stack="backend", level="info", pkg="controller", message="shorten_url called")
    db_url = await create_url(url)
    return db_url

@router.get("/urls/{url_id}", response_model=UrlResponse)
async def read_url(url_id: int):
    log(stack="backend", level="info", pkg="controller", message="read_url called")
    db_url = await get_url(url_id)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url

@router.get("/urls/", response_model=List[UrlResponse])
async def read_all_urls(db: Session = Depends(get_db)):
    log(stack="backend", level="info", pkg="controller", message="read_all_urls called")
    return await get_urls(db)