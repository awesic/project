import uuid

from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from src.auth.manager import get_user_manager
from src.config import settings
from src.users.models import User

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----\n' + settings.JWT_PUBLIC_KEY + '\n-----END PUBLIC KEY-----'
PRIVATE_KEY = '-----BEGIN PRIVATE KEY-----\n' + settings.JWT_PRIVATE_KEY + '\n-----END PRIVATE KEY-----'


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=PRIVATE_KEY,
        lifetime_seconds=3600,
        algorithm=settings.JWT_ALGORITHM,
        public_key=PUBLIC_KEY,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend]
)

current_user = fastapi_users.current_user(active=True)


async def get_current_user(current: User = Depends(current_user)):
    return current