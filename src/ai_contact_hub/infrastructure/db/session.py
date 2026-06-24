from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    Session,
)

from ai_contact_hub.config import get_settings



engine = create_engine(get_settings().db_url)


type SessionFactory = sessionmaker[Session]


def session_factory() -> SessionFactory:
    return sessionmaker[Session](
        autocommit=False,
        autoflush=False,
        bind=engine
    )
