from typing import Self
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError
)

from ai_contact_hub.infrastructure.db.repositories import ContactRepositoryImpl
from ai_contact_hub.domain.errors import (
    ORMError,
    ORMIntegrityError
)



class SqlAlchemyUnitOfWork:
    def __init__(self, session_factory) -> None:
        self._session_factory = session_factory()

    def __enter__(self) -> Self:
        self.session = self._session_factory()
        self.contacts = ContactRepositoryImpl(self.session)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        try:
            if exc_type:
                self.rollback()
        finally:
            self.session.close()

    def commit(self) -> None:
        try:
            self.session.commit()
        except IntegrityError as e:
            raise ORMIntegrityError(
                "Record already exists"
            ) from e
        except SQLAlchemyError as e:
            raise ORMError(
                "Failed to save record"    
            ) from e
        finally:
            self.rollback()

    def rollback(self) -> None:
        self.session.rollback()
