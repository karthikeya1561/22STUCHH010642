from pydantic import BaseModel

class UrlCreate(BaseModel):
    original_url: str

class UrlResponse(BaseModel):
    id: int
    original_url: str
    short_url: str

class UrlInDB(UrlResponse):
    created_at: str
    updated_at: str