
from sqlalchemy.orm import Session

from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import (
TicketCreate,
TicketUpdate
)


def create_ticket_service(
    db: Session,
    ticket_data: TicketCreate,
):
    return TicketRepository.create_ticket(
        db=db,
        ticket_data=ticket_data,
    )

# READ ALL
def get_all_tickets_service(db: Session):
    return TicketRepository.get_all_tickets(db=db)


def get_ticket_by_id_service(
    db: Session,
    ticket_id: int,
):
    return TicketRepository.get_ticket_by_id(
        db=db,
        ticket_id=ticket_id,
    )


# UPDATE
def update_ticket_service(
    db: Session,
    ticket_id: int,
    ticket_data: TicketUpdate,
):
    return TicketRepository.update_ticket(
        db=db,
        ticket_id=ticket_id,
        ticket_data=ticket_data,
    )


# DELETE
def delete_ticket_service(
    db: Session,
    ticket_id: int,
):
    return TicketRepository.delete_ticket(
        db=db,
        ticket_id=ticket_id,
    )