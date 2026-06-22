from typing import Callable

from ai_contact_hub.domain.entities.contact import Contact
from ai_contact_hub.application.interfaces import UoWProto
from ai_contact_hub.shared.dtos import ContactDTO
from ai_contact_hub.application.emails.service import NotificationService
from ai_contact_hub.application.ai.service import AIService



class ProcessNewMessage:
    def __init__(
            self,
            ai_service: AIService,
            email_client: NotificationService,
            uow: Callable[..., UoWProto]
    )  -> None:
        self.ai_service = ai_service
        self.email_client = email_client
        self.uow = uow
        
    async def execute(
            self,
            contact_dto: ContactDTO
        ) -> None:
        new_contact = Contact(
            name=contact_dto.name,
            email=contact_dto.email,
            phone=contact_dto.phone,
            message=contact_dto.message
        )
        with self.uow() as uow:
            new_contact_id = uow.contacts.save(new_contact)
            uow.commit()
        
        await self.email_client.notify_user(
            user_name=contact_dto.name,
            user_email=contact_dto.email,
            user_message=contact_dto.message
        )
        await self.email_client.notify_owner(
            user_name=contact_dto.name,
            user_email=contact_dto.email,
            user_message=contact_dto.message
        )

        ai_result = await self.ai_service.analyze(contact_dto.message)
        sentiment = ai_result["sentiment"]
        source = ai_result["source"]
        with self.uow() as uow:
            uow.contacts.update(
                contact_id=new_contact_id,
                sentiment=sentiment,
                sentiment_source=source
            )
            uow.commit()
