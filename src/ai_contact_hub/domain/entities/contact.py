from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (
    String,
    Text,
)


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    phone: Mapped[Optional[str]] = mapped_column(String(30))
    message: Mapped[str] = mapped_column(Text)
    sentiment: Mapped[Optional[str]]
    sentiment_source: Mapped[Optional[str]]
