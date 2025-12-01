from pydantic import BaseSettings

class Settings(BaseSettings):
    db_urls: str
    db_db: str

    class Config:
        env_file = ".env"

settings = Settings()
