from utils import log
def log_config_operation(operation: str):
    log(stack="config.py", level="INFO", pkg="core", message=f"{operation} called")
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "usTTNfJctGkuUBAR"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
