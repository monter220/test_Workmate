from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import kitty_crud, kittycolour_crud, breed_crud
from app.schemas import KittyCreate, KittyUpdate, KittyDB

router = APIRouter(prefix='/kittys')


@router.post(
    '/',
    response_model=KittyDB,
    response_model_exclude_none=True,
)
async def create_new_kitty(
        kitty: KittyCreate,
        session: AsyncSession = Depends(get_async_session),
):
    breed = await breed_crud.get(kitty.breed_id, session)
    if breed:
        raise HTTPException(
            status_code=422,
            detail='Такой породы нет!',
        )
    colour = await kittycolour_crud.get(kitty.colour_id,session)
    if colour:
        raise HTTPException(
            status_code=422,
            detail='Такого цвета нет!',
        )
    new_kitty = await kitty_crud.create(kitty, session)
    return new_kitty


@router.get(
    '/',
    response_model=list[KittyDB],
    response_model_exclude_none=True,
)
async def get_all_kittys(
        session: AsyncSession = Depends(get_async_session),
):
    all_kittys = await kitty_crud.get_multi(session)
    return all_kittys


@router.get(
    '/{kitty_id}',
    response_model=KittyDB,
    response_model_exclude_none=True,
)
async def get_kitty(
        kitty_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    kitty = await kitty_crud.get(kitty_id, session)
    if kitty:
        raise HTTPException(
            status_code=422,
            detail='Котенок не найден!',
        )
    return kitty


@router.patch(
    '/{kitty_id}',
    response_model=KittyDB,
    response_model_exclude_none=True,
)
async def partially_update_kitty(
        kitty_id: int,
        obj_in: KittyUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    kitty = await kitty_crud.get(kitty_id, session)
    if kitty:
        raise HTTPException(
            status_code=422,
            detail='Котенок не найден!',
        )

    updated_kitty = await kitty_crud.update(kitty, obj_in, session)
    return updated_kitty


@router.delete(
    '/{kitty_id}',
    response_model=KittyDB,
    response_model_exclude_none=True,
)
async def remove_kitty(
        kitty_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    kitty = await kitty_crud.get(kitty_id, session)
    if kitty:
        raise HTTPException(
            status_code=422,
            detail='Котенок не найден!',
        )
    deleted_kitty = await kitty_crud.remove(kitty, session)
    return deleted_kitty
