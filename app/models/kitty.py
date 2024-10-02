from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Basemodel, Basehelpmodel


class Breed(Basehelpmodel):
    """
    Модель породы котят
    """
    kitty=relationship('Kitty', cascade='delete')


class KittyColour(Basehelpmodel):
    """
    Модель цветов котят
    """
    kitty=relationship('Kitty', cascade='delete')


class Kitty(Basemodel):
    """
    Модель котят
    """
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
