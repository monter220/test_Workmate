from sqlalchemy import Column, String, Text

from app.core.config import settings
from app.core.db import Base


class Basemodel(Base):
    name = Column(
        String(settings.max_name_len),
        unique=True,
        nullable=False,
    )
    description = Column(
        Text,
        nullable=True,
        comment='Описание',
    )

    __abstract__ = True
