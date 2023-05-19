from fastapi import FastAPI

from src.applications.router import router_app
from src.auth.base_config import fastapi_users, auth_backend
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
async def root():
    return {"message": "Hello World"}
