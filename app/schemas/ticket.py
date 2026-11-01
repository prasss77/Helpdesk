from pydantic import BaseModel, ConfigDict
from typing import Optional



class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str


class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str

    model_config = ConfigDict(from_attributes=True)
 
