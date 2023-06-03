from fastapi import FastAPI, Depends

from src.applications.router import router_app
from src.auth.base_config import fastapi_users, auth_backend, current_user
from src.users.models import User
from src.users.schemas import UserRead, UserCreate, UserUpdate

app = FastAPI(
    title="Project"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt", tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth", tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users", tags=["Users"],
)

app.include_router(
    router_app,
    prefix="/application", tags=["Applications"],
)


@app.get("/check")
async def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"
