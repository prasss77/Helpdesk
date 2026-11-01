
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.ticket import (
TicketCreate,
TicketUpdate,
TicketResponse
)

from app.services.ticket_service import (
create_ticket_service,
get_ticket_by_id_service,
get_all_tickets_service,
update_ticket_service,
delete_ticket_service
)

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.post("/", 
             response_model=TicketResponse,
             status_code=status.HTTP_201_CREATED
             )
def create_ticket_endpoint(
    ticket_data: TicketCreate,
    db: Session = Depends(get_db),
):
    return create_ticket_service(
        db=db,
        ticket_data=ticket_data,
    )


@router.get("/",
            response_model=list[TicketResponse],
            )
def get_all_tickets_endpoint(
    db: Session = Depends(get_db),
):
    return get_all_tickets_service(db=db)


@router.get("/{ticket_id}",
            response_model=TicketResponse,
            )
def get_ticket_endpoint(
    ticket_id: int,
    db: Session = Depends(get_db),
):
    ticket = get_ticket_by_id_service(
        db=db,
        ticket_id=ticket_id,
    )

    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found",
        )

    return ticket



@router.put("/{ticket_id}",
            response_model=TicketResponse,
            )
def update_ticket_endpoint(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db),
):
    ticket = update_ticket_service(
        db=db,
        ticket_id=ticket_id,
        ticket_data=ticket_data,
    )

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    return ticket


@router.delete("/{ticket_id}")
def delete_ticket_endpoint(
    ticket_id: int,
    db: Session = Depends(get_db),
):
    ticket = delete_ticket_service(
        db=db,
        ticket_id=ticket_id,
    )

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    return {"message": "Ticket successfully deleted"}