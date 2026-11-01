
from fastapi import FastAPI

from app.api.v1.routes import ticket

app = FastAPI(
    title="Helpdesk API",
    version="1.0.0",
)

app.include_router(
    ticket.router,
    prefix="/api/v1",
)
