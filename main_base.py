from models.entity import *
from models.relations import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from models.class_base import Base, RelationsTables
from pathlib import *

engine = create_engine('sqlite:///sqlite3.db', echo=True)
engine.connect()

Base.metadata.create_all(engine)
RelationsTables.metadata.create_all(engine)

print(engine)

