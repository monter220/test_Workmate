from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Kitty, KittyColour, Breed

breed_crud = CRUDBase(Breed)
kittycolour_crud = CRUDBase(KittyColour)


class CRUDKitty(CRUDBase):

    async def get_breed_kittys(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.breed_id == obj_id
            )
        )
        return db_obj.scalars().all()


kitty_crud = CRUDKitty(Kitty)
