from typing import Self

from ai_contact_hub.infrastructure.db.repositories import ContactRepositoryImpl



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
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
