from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Integer, String, Column, ForeignKey
from utilites.title_to_snake_case import titleToSnakeCase

__all__ = ['Base', 'RelationsTables']


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True)
    name = Column(String)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"



@as_declarative()
class RelationsTables:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        name = titleToSnakeCase(cls.__name__)
        return name


@as_declarative()
class Items:
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    weight = Column(Integer)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"
