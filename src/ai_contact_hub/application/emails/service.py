from ai_contact_hub.application.interfaces import (
    EmailTemplate
)
from ai_contact_hub.application.interfaces import EmailClientProto



class NotificationService:
    def __init__(
            self,
            email_client: EmailClientProto,
            owner_email_address: str,
            owner_template: EmailTemplate,
            user_template: EmailTemplate
    ) -> None:
        self.email_client = email_client
        self.owner_email_address = owner_email_address
        self.owner_template = owner_template
        self.user_template = user_template
        
    async def notify_owner(
        self,
        user_name: str,
        user_email_address: str,
        user_message: str
    ) -> None:
        await self.email_client.send(
            to=self.owner_email_address,
            subject=self.owner_template.subject,
            body=self.owner_template.text_builder(
                name=user_name,
                email=user_email_address,
                message=user_message,
            )
        )

    async def notify_user(
        self,
        user_name: str,
        user_email: str,
        user_message: str
    ) -> None:
        await self.email_client.send(
            to=user_email,
            subject=self.user_template.subject,
            body=self.user_template.text_builder(
                name=user_name,
                message=user_message
            )
        )
