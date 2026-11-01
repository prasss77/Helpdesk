
from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate


class TicketRepository:

    # CREATE: Membuat tiket baru
    @staticmethod
    def create_ticket(db: Session, ticket_data: TicketCreate):
        new_ticket = Ticket(
            title=ticket_data.title,
            description=ticket_data.description,
            priority=ticket_data.priority,
        )

        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)

        return new_ticket


    # READ: Mengambil semua tiket
    @staticmethod
    def get_all_tickets(db: Session):
        return db.query(Ticket).all()

    # READ: Mengambil tiket berdasarkan ID
    @staticmethod
    def get_ticket_by_id(db: Session, ticket_id: int):
        return db.query(Ticket).filter(
            Ticket.id == ticket_id
        ).first()

    # UPDATE
    @staticmethod
    def update_ticket(
        db: Session,
        ticket_id: int,
        ticket_data: TicketUpdate,
    ):
        ticket = db.query(Ticket).filter(
            Ticket.id == ticket_id
        ).first()

        if ticket is None:
            return None

        update_data = ticket_data.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        for key, value in update_data.items():
            setattr(ticket, key, value)

        db.commit()
        db.refresh(ticket)

        return ticket

    # DELETE
    @staticmethod
    def delete_ticket(db: Session, ticket_id: int):
        ticket = db.query(Ticket).filter(
            Ticket.id == ticket_id
        ).first()

        if ticket is None:
            return None

        db.delete(ticket)
        db.commit()

        return ticket
