from models.entity import *
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from models.class_base import RelationsTables

__all__ = ['SkillsInSituations', 'DowngradeCharacteristicDueToFlaws', 'UpgradeCharacteristicDueToFeatures',
           'ConflictsBetweenFlawsAndFeatures', 'RequiredSpecificationsForFeatures']


# Применение навыков в особых ситуациях
class SkillsInSituations(RelationsTables):
    id_skill = Column(Integer, ForeignKey(Skills.id), primary_key=True)
    id_situation = Column(Integer, ForeignKey(Situations.id), primary_key=True)


# Снижение характеристики за счет изъяна
class DowngradeCharacteristicDueToFlaws(RelationsTables):
    id_skill = Column(Integer, ForeignKey(Skills.id), primary_key=True)
    id_flaw = Column(Integer, ForeignKey(Flaws.id), primary_key=True)
    downgrade = Column(Integer, ForeignKey(Dices.size), primary_key=True)


# Повышение характеристик за счет черт
class UpgradeCharacteristicDueToFeatures(RelationsTables):
    id_skill = Column(Integer, ForeignKey(Skills.id), primary_key=True)
    id_features = Column(Integer, ForeignKey(Features.id), primary_key=True)
    upgrade = Column(Integer, ForeignKey(Dices.size), primary_key=True)


# конфликтующие черты и изъяны
class ConflictsBetweenFlawsAndFeatures(RelationsTables):
    id_flaw = Column(Integer, ForeignKey(Flaws.id), primary_key=True)
    id_features = Column(Integer, ForeignKey(Features.id), primary_key=True)


# Требуемые для черты характеристики
class RequiredSpecificationsForFeatures(RelationsTables):
    id_specification = Column(Integer, ForeignKey(Specifications.id), primary_key=True)
    id_features = Column(Integer, ForeignKey(Features.id), primary_key=True)
    needed_dice = Column(Integer, ForeignKey(Dices.size), primary_key=True)

# Прирост навыка за счет черты
#class IncreaseSkillsDueToFeatures(Base)
