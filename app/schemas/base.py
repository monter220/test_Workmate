from typing import Optional

from pydantic import BaseModel, Field, Extra

from app.core.config import settings


class Base(BaseModel):
    name: str = Field(
        None,
        max_length=settings.max_name_len,
    )
    description: Optional[str]


class BaseCreate(Base):

    class Config:
        extra = Extra.forbid


class BaseDB(Base):

    class Config:
        orm_mode = True
