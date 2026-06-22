from fastapi import (
    Request,
    HTTPException
)
from ai_contact_hub.domain.errors import (
    ORMError,
    ORMIntegrityError,
    EmailError,
)



def register_exception_handlers(app):    
    @app.exception_handler(ORMError)
    async def orm_error_exception_handler(request: Request, exc: ORMError):
        raise HTTPException(status_code=500, detail=str(exc))

    @app.exception_handler(ORMIntegrityError)
    async def orm_integrity_error_exception_handler(request: Request, exc: ORMIntegrityError):
        raise HTTPException(status_code=409, detail=str(exc))

    @app.exception_handler(EmailError)
    async def employee_reassignment_error_exception_handler(request: Request, exc: EmailError):
        raise HTTPException(status_code=500, detail=str(exc))
