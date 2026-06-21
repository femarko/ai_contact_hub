from ai_contact_hub.infrastructure.emails.smtp_client import (
    send_email
)
from ai_contact_hub.infrastructure.emails.templates import (
    owner_notification,
    user_confirmation
)

from ai_contact_hub.config import get_settings


async def send_contact_notifications(
    name: str,
    email: str,
    message: str
):
    await send_email(
        to=get_settings().owner_email,
        subject="Новое обращение",
        body=owner_notification(
            name,
            email,
            message
        )
    )


    await send_email(
        to=email,
        subject="Мы получили ваше обращение",
        body=user_confirmation(
            name,
            message
        )
    )
