from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import kittycolour_crud
from app.schemas import KittyColourCreate, KittyColourDB

router = APIRouter(prefix='/colour')


@router.post(
    '/',
    response_model=KittyColourDB,
    response_model_exclude_none=True,
)
async def create_new_kittycolour(
        kittycolour: KittyColourCreate,
        session: AsyncSession = Depends(get_async_session),
):
    colour = await kittycolour_crud.name_exist(kittycolour.name, session)
    if not colour:
        raise HTTPException(
            status_code=422,
            detail='Такой цвет уже есть!',
        )
    new_colour = await kittycolour_crud.create(kittycolour, session)
    return new_colour
