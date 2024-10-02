from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.config import settings
from app.models.base import Basemodel


class Breed(Basemodel):
    """
    Модель породы котят
    """
    pass


class KittyColour(Basemodel):
    """
    Модель цветов котят
    """
    pass


class Kitty(Basemodel):
    breed_id = Column(
        Integer,
        ForeignKey('breed.id'),
        comment='Порода',
    )
    colour_id = Column(
        Integer,
        ForeignKey('kittycolour.id'),
        comment='Цвет',
    )
    age = Column(
        Integer,
        nullable=False,
        comment='Возраст в месяцах',
    )
