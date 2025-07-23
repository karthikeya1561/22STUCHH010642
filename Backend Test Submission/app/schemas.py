from utils.log import log
from pydantic import BaseModel

def log_schema_operation(operation: str):
    log(stack="backend", level="info", pkg="domain", message=f"{operation} called")

class UrlCreate(BaseModel):
    original_url: str

class UrlResponse(BaseModel):
    id: int
    original_url: str
    short_url: str

class UrlInDB(UrlResponse):
    created_at: str
    updated_at: str