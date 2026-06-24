import uvicorn
from fastapi import FastAPI

from ai_contact_hub.entrypoints.http.routes import contact_router
from ai_contact_hub.entrypoints.http.exceptions import register_exception_handlers
from ai_contact_hub.logging_config import setup_logging
from ai_contact_hub.entrypoints.http.middleware import RequestLoggingMiddleware



setup_logging()
app = FastAPI()
app.add_middleware(RequestLoggingMiddleware)
register_exception_handlers(app)
app.include_router(contact_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
