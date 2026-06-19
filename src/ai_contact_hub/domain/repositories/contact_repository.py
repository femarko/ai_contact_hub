from typing import Protocol

from ai_contact_hub.domain.entities.contact import Contact


class ContactRepoProto(Protocol):
    def save(self, contact: Contact) -> None:
        ...
