import logging
import aiosmtplib
from email.message import EmailMessage

from ai_contact_hub.config import get_settings
from ai_contact_hub.domain.errors import EmailError



logger = logging.getLogger("emails")


class SMTP_Client:
    @staticmethod
    async def send(
        to: str,
        subject: str,
        body: str
    ) -> None:
        message = EmailMessage()
        message["From"] = get_settings().smtp_user
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)
        try:
            await aiosmtplib.send(
                message,
                hostname=get_settings().smtp_host,
                port=get_settings().smtp_port,
                username=get_settings().smtp_user,
                password=get_settings().smtp_password,
                start_tls=True,
            )
        except aiosmtplib.SMTPException as exc:
            context = "Failed to send email to user"
            logger.exception("%s", context)
