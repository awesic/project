import secrets
from typing import List

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings

load_dotenv()


class Config(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)

    CORS_ORIGINS: List[AnyHttpUrl] = []

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    POSTGRES_DRIVER: str
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Config()


def get_url():
    return f"{settings.POSTGRES_DRIVER}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@" \
           f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}?async_fallback=True"
