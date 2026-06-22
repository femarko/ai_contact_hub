from fastapi import Depends
from typing import Callable

from ai_contact_hub.config import get_settings
from ai_contact_hub.infrastructure.db.session import session_factory
from ai_contact_hub.infrastructure.db.repositories import ContactRepositoryImpl
from ai_contact_hub.domain.interfaces.contact_repository import ContactRepoProto
from ai_contact_hub.application.use_cases.process_new_comment import ProcessNewMessage
from ai_contact_hub.application.emails.service import NotificationService
from ai_contact_hub.application.emails.text_templates import (
    owner_notification,
    user_confirmation,
)
from ai_contact_hub.application.interfaces import EmailTemplate
from ai_contact_hub.shared.enums import EmailSubject
from ai_contact_hub.application.ai.service import AIService
from ai_contact_hub.infrastructure.db.sqlalchemy_uow import SqlAlchemyUnitOfWork
from ai_contact_hub.infrastructure.ai.groq_client import GroqClient
from ai_contact_hub.infrastructure.ai.fallback import fallback_sentiment
from ai_contact_hub.infrastructure.emails.smtp_client import SMTP_Client



def get_contact_repository(session = Depends(session_factory)) -> ContactRepoProto:
    return ContactRepositoryImpl(session)

def get_ai_client() -> GroqClient:
    return GroqClient(
        api_key=get_settings().groq_api_key
    )

def get_fallback() -> Callable[..., dict[str, str]]:
    return fallback_sentiment

def get_ai_service(
        ai_client=Depends(get_ai_client),
        fallback=Depends(get_fallback)
) -> AIService:
    return AIService(
        ai_client,
        fallback
    )

def get_email_client() -> NotificationService:
    return NotificationService(
        email_client=SMTP_Client,
        owner_email=get_settings().owner_email,
        owner_template=EmailTemplate(
            subject=EmailSubject.OWNER,
            text_builder=owner_notification
        ),
        user_template=EmailTemplate(
            subject=EmailSubject.USER,
            text_builder=user_confirmation
        )
    )

def get_uow() -> Callable[..., SqlAlchemyUnitOfWork]:
    return lambda:SqlAlchemyUnitOfWork(session_factory)


def get_process_new_message_uc(
        ai_service=Depends(get_ai_service),
        email_client=Depends(get_email_client),
        uow=Depends(get_uow)

) -> ProcessNewMessage:
    return ProcessNewMessage(
        ai_service,
        email_client,
        uow
    )
