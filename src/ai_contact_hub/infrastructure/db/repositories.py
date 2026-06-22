from ai_contact_hub.domain.entities.contact import Contact
from sqlalchemy import update
from sqlalchemy.exc import (
    IntegrityError,
    SQLAlchemyError
)

from ai_contact_hub.domain.errors import (
    ORMError,
    ORMIntegrityError
) 



class ContactRepositoryImpl:

    def __init__(self, session):
        self.session = session

    def save(self, contact: Contact) -> int:

        model = Contact(
            name=contact.name,
            email=contact.email,
            phone=contact.phone,
            message=contact.message
        )
        self.session.add(model)
        try:
            self.session.flush()
        except IntegrityError as e:
            raise ORMIntegrityError(
                "Record already exists"
            ) from e
        except SQLAlchemyError as e:
            raise ORMError(
                "Failed to save record"
            ) from e      
        return model.id

    def update(self,
               contact_id: int,
               sentiment: str,
               sentiment_source: str
    ) -> None:
        self.session.execute( 
            update(Contact).where(Contact.id == contact_id)
            .values(sentiment=sentiment)
            .values(sentiment_source=sentiment_source)
        )
