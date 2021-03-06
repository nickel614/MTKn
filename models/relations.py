from models.entity import *
from models.equipment import *
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from models.class_base import RelationsTables

__all__ = ['SkillsInSituations', 'DowngradeCharacteristicDueToFlaws', 'UpgradeCharacteristicDueToFeatures',
           'ConflictsBetweenFlawsAndFeatures', 'RequiredSpecificationsForFeatures', 'IncreaseSkillsDueToFeatures',
           'CharsSkills', 'CharsSpecifications', 'CharsFeatures', 'CharsFlaws', 'CharsArmor',
           'SpecificationModificationDueToArmor', 'WeaponDamage']


# Применение навыков в особых ситуациях
class SkillsInSituations(RelationsTables):
    id_skill = Column(Integer, ForeignKey(Skills.id), primary_key=True)
    id_situation = Column(Integer, ForeignKey(Situations.id), primary_key=True)


# Снижение характеристики за счет изъяна
class DowngradeCharacteristicDueToFlaws(RelationsTables):
    id_specification = Column(Integer, ForeignKey(Specifications.id), primary_key=True)
    id_flaw = Column(Integer, ForeignKey(Flaws.id), primary_key=True)
    downgrade = Column(Integer, ForeignKey(Dices.size))


# Повышение характеристик за счет черт
class UpgradeCharacteristicDueToFeatures(RelationsTables):
    id_specification = Column(Integer, ForeignKey(Specifications.id), primary_key=True)
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
class IncreaseSkillsDueToFeatures(RelationsTables):
    id_skill = Column(Integer, ForeignKey(Skills.id), primary_key=True)
    id_feature = Column(Integer, ForeignKey(Features.id), primary_key=True)
    needed_dice = Column(Integer, ForeignKey(Dices.size), primary_key=True)


# Навыки персонажа
class CharsSkills(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_skill = Column(Integer, ForeignKey(Skills.id), primary_key=True)


# Характеристики персонажа
class CharsSpecifications(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_specification = Column(Integer, ForeignKey(Specifications.id), primary_key=True)


# Черты персонажа
class CharsFeatures(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_feature = Column(Integer, ForeignKey(Features.id), primary_key=True)


# Изъяны персонажа
class CharsFlaws(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_flaw = Column(Integer, ForeignKey(Flaws.id), primary_key=True)


# Экипировка персонажа
class CharsArmor(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_armor = Column(Integer, ForeignKey(Armor.id), primary_key=True)


# Модификация навыка за счет брони
class SpecificationModificationDueToArmor(RelationsTables):
    id_armor = Column(Integer, ForeignKey(Armor.id), primary_key=True)
    id_specification = Column(Integer, ForeignKey(Specifications.id), primary_key=True)
    spec_modification = Column(Integer)


# Урон оружия
class WeaponDamage(RelationsTables):
    id_weapon = Column(Integer, ForeignKey(Weapon.id), primary_key=True)
    id_dice1 = Column(Integer, ForeignKey(Dices.size))
    dices1_count = Column(Integer)
    id_dice2 = Column(Integer, ForeignKey(Dices.size))
    dices2_count = Column(Integer)
    num_modifier = Column(Integer)


# Вооружение персонажа
class CharsWeapons(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_weapon = Column(Integer, ForeignKey(Weapon.id))


class CharsItems(RelationsTables):
    id_char = Column(Integer, ForeignKey(Chars.id), primary_key=True)
    id_item = Column(Integer, ForeignKey(SimpleItems.id))
