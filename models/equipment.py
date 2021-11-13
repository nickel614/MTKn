from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.class_base import Base
from models.entity import *
from models.class_base import Items

__all__ = ['Armor', 'Weapon', 'SimpleItems']


# Броня
class Armor(Items):

    armor = Column(Integer)
    protection_mod = Column(Integer)


# Оружие
class Weapon(Items):

    distance = Column(String)
    piercing = Column(Integer)  # бронебойность
    notes = Column(String)


# Обычные вещи
class SimpleItems(Items):

    notes = Column(String)
