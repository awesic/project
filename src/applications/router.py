from typing import List, Mapping

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.applications.models import Application
from src.applications.schemas import ReadApplication, ApplicationBase, CreatApplication
from src.auth.base_config import current_user
from src.database import get_async_session
from src.users.models import User

router_app = APIRouter()


@router_app.get('', response_model=List[ReadApplication])
async def get_all_applications(session: AsyncSession = Depends(get_async_session)):
    stmt = await session.execute(select(1))
    return stmt.all()


@router_app.get('/{app_id}', response_model=ApplicationBase)
async def get_one_application(app_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = select(Application).where(app_id == Application.id)
        result = await session.execute(stmt)
        return result.first()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Some problems")


@router_app.post('')
async def creat_application(
        app: CreatApplication,
        session: AsyncSession = Depends(get_async_session),
        cur_user: User = Depends(current_user)
):
    new_app = app.dict()
    new_app.update({'customer_id': cur_user.id})
    stmt = insert(Application).values(**new_app)
    await session.execute(stmt)
    await session.commit()
    return f'The application was sent successfully'