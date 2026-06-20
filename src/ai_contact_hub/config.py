import os

from functools import lru_cache
from pydantic import PostgresDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


ENV = os.getenv("ENV", "local")
env_file = ".env.loc" if ENV == "local" else ".env"


class Settings(BaseSettings):
    postgres_host: str
    db_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str
    groq_api_key: str
    
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
