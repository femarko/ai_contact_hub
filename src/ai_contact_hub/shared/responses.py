from pydantic import BaseModel



class ContactResponse(BaseModel):
    message: str
