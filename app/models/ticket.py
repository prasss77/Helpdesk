from decimal import Decimal

from sqlalchemy import Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
            String(255),
            nullable=False,
        )

    status: Mapped[str] = mapped_column(
                String(20),
                nullable=False,
                default="open",
            )

    priority: Mapped[str] = mapped_column(
                    String(20),
                    nullable=False,
                )
    


