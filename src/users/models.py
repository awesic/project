from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from enum import Enum as PyEnum

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Role(PyEnum):
    ADMIN = "admin"
    WORKER = "worker"
    USER = "user"


class User(SQLAlchemyBaseUserTableUUID, Base):
    role: Mapped[Role] = mapped_column(Enum(Role), nullable=False, default=Role.USER)


user = User.__table__