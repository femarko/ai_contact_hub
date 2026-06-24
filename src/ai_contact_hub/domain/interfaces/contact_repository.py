from typing import Protocol

from ai_contact_hub.domain.entities.contact import Contact



class ContactRepoProto(Protocol):
    def save(self, contact: Contact) -> int: ...

    def update(
            self,
            contact_id: int,
            sentiment: str,
            sentiment_source: str
    ) -> None: ...
