from fastapi import (
    APIRouter,
    Depends,
)

from ai_contact_hub.shared.dtos import ContactDTO
from ai_contact_hub.entrypoints.http.dependencies import get_process_new_message_uc
from ai_contact_hub.shared.responses import ContactResponse


contact_router = APIRouter(
    prefix="/api",
    tags=["Contact"]
)


@contact_router.post("/contact", status_code=201)
async def process_new_comment(
        data: ContactDTO,
        uc = Depends(get_process_new_message_uc),
) -> ContactResponse:
    await uc.execute(data)
    return ContactResponse(message="Contact saved")
