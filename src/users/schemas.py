import uuid
from typing import Optional

from fastapi_users import schemas

from src.users.models import Role


class UserRead(schemas.BaseUser[uuid.UUID]):
    role: Role


class UserCreate(schemas.BaseUserCreate):
    role: Optional[Role] = Role.USER


class UserUpdate(schemas.BaseUserUpdate):
    pass