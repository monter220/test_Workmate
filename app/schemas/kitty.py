from app.schemas.base import BaseCreate, Base, BaseDB


class BreedCreate(BaseCreate):
    """
    Схема для создания породы котят
    """


class BreedDB(BaseDB):
    """
    Схема для получения породы котят
    """
    pass


class KittyColourCreate(BaseCreate):
    """
    Схема для создания цветов котят
    """
    pass


class KittyColourDB(BaseDB):
    """
    Схема для отображения цветов котят
    """
    pass


class KittyCreate(BaseCreate):
    """
    Схема для создания котят
    """
    breed_id: int
    colour_id: int
    age: int


class KittyUpdate(Base):
    """
    Схема для обновления котят
    """
    breed_id: int
    colour_id: int
    age: int


class KittyDB(BaseDB):
    """
    Схема для получения котят
    """
    breed_id: int
    colour_id: int
    age: int
