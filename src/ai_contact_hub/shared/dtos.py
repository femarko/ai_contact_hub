from pydantic import (
    BaseModel,
    EmailStr,
)
from pydantic_extra_types.phone_numbers import PhoneNumber



class ContactDTO(BaseModel):
    name: str
    email: EmailStr
    phone: PhoneNumber
    message: str
