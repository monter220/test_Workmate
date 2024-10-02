from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import kitty_crud, breed_crud
from app.schemas import KittyDB, BreedCreate, BreedDB

router = APIRouter(prefix='/breeds')


@router.post(
    '/',
    response_model=BreedDB,
    response_model_exclude_none=True,
)
async def create_new_breed(
        breed: BreedCreate,
        session: AsyncSession = Depends(get_async_session),
):
    if await breed_crud.name_exist(breed.name, session):
        raise HTTPException(
            status_code=422,
            detail='Такая порода уже есть!',
        )
    new_breed = await breed_crud.create(breed, session)
    return new_breed


@router.get(
    '/',
    response_model=list[BreedDB],
    response_model_exclude_none=True,
)
async def get_breed(
        session: AsyncSession = Depends(get_async_session),
):
    breed = await breed_crud.get_multi(session)
    return breed


@router.get(
    '/{breed_id}/kittys',
    response_model=list[KittyDB],
    response_model_exclude_none=True,
)
async def get_all_breed_kittys(
        breed_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    if await breed_crud.get(breed_id, session):
        raise HTTPException(
            status_code=422,
            detail='Порода не найдена!',
        )
    all_kittys = await kitty_crud.get_breed_kittys(breed_id, session)
    return all_kittys
