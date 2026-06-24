import os

from pathlib import Path
from functools import lru_cache
from pydantic import (
    PostgresDsn,
    EmailStr,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


ENV = os.getenv("ENV")
env_file = ".env.loc" if ENV == "local" else ".env"


BASE_DIR = Path.cwd()
LOG_FILE = BASE_DIR / "logs" / "app.log"


class Settings(BaseSettings):
    postgres_host: str
    db_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str
    groq_api_key: str
    smtp_host: str
    smtp_port: int
    smtp_user: str
    smtp_password: str
    owner_email: EmailStr
    
    model_config = SettingsConfigDict(
        env_file=env_file,
        extra="ignore"
    )

    @property
    def db_url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg",
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.postgres_host,
                port=self.db_port,
                path=self.postgres_db
            )
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore
