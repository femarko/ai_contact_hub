from dataclasses import dataclass
from typing import (
    Callable,
    Protocol,
    Self
)
from ai_contact_hub.domain.interfaces.contact_repository import ContactRepoProto
from ai_contact_hub.domain.entities.contact import Contact


class UoWProto(Protocol):
    contacts: ContactRepoProto

    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def commit(self) -> None: ...
    def flush(self) -> None: ...
    def refresh(self, instance: Contact) -> None: ...
    def rollback(self) -> None: ...


class AiServiceProto(Protocol):
    async def analyze(self, text: str) -> dict[str, str]: ...


class EmailClientProto(Protocol):
    async def send(
        self,
        to: str,
        subject: str,
        body: str,
    ) -> None: ...


@dataclass(frozen=True)
class EmailTemplate:
    subject: str
    text_builder: Callable[..., str]
