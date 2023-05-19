import datetime
import random
from enum import Enum as PyEnum

from fastapi_users_db_sqlalchemy import UUID_ID, GUID
from sqlalchemy import Integer, Enum, String, Text, TIMESTAMP, func, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.auth.base_config import get_current_user
from src.database import Base


class Status(PyEnum):
    PENDING = "pending"
    RECEIVED = "received"
    COMPLETED = "completed"


class Corpus(PyEnum):
    UCHEBKA = "Учебный корпус"
    ADMINKA = "Административный корпус"
    BC = "Бизнес центр"
    LK = "Лабораторный корпус"
    SPORT_COMPLEX = "Спорт комплекс"


class Application(Base):
    __tablename__ = "application"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, default=random.randint(1000, 9999))
    corpus: Mapped[Corpus] = mapped_column(Enum(Corpus), nullable=False)
    auditorium: Mapped[str] = mapped_column(String, nullable=False)
    incident_category: Mapped[str] = mapped_column(String, nullable=False)
    problem: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False, default=Status.PENDING)

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    customer_id: Mapped[UUID_ID] = mapped_column(GUID, ForeignKey("user.id"), default=get_current_user())


application = Application.__table__