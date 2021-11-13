from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.class_base import Base

__all__ = ['Specifications', 'Skills', 'Situations', 'Features', 'Flaws', 'Chars', 'Dices']


# Характеристики
class Specifications(Base):

    description = Column(String)


# Навыки
class Skills(Base):

    description = Column(String)


# Ситуации
class Situations(Base):

    dice_modifier = Column(Integer, ForeignKey('dices.size'))  # модификатор события (куб)
    num_modifier = Column(Integer)  # численный модификатор (альтернатива модификатору - кубу)
    description = Column(String)


# Черты
class Features(Base):

    description = Column(String)
    nature = Column(String)  # Характер черты (боевая, социальная и пр.)


# Изъяны
class Flaws(Base):

    size = Column(Integer)
    description = Column(String)


# персонажи
class Chars(Base):

    type = Column(String)
    occupation = Column(String)
    status = Column(String)
    size = Column(Integer)


# Кубы
class Dices(Base):

    size = Column(Integer, primary_key=True)
    situations_id = relationship('Situations')
