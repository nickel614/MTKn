from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.class_base import Base

__all__ = ['Specifications', 'Skills', 'Situations', 'Features', 'Flaws', 'Chars', 'Dices']

# Характеристики
class Specifications(Base):
    __table_args__ = {'extend_existing': True}
    description = Column(String)


# Навыки
class Skills(Base):

    description = Column(String)
    skillsSituations = relationship('SkillsInSituations')
    downgradeSkillsFlaws = relationship('DowngradeSkillsDueToFlaws')


# Ситуации
class Situations(Base):

    dice_modifier = Column(Integer, ForeignKey('dices.size'))  # модификатор события (куб)
    num_modifier = Column(Integer)  # численный модификатор (альтернатива модификатору - кубу)
    description = Column(String)
    skills_in_situations = relationship('SkillsInSituations')


# Черты
class Features(Base):

    description = Column(String)
    nature = Column(String)  # Характер черты (боевая, социальная и пр.)
    upgrade_skills_due_to_features = relationship('UpgradeSkillsDueToFeatures')


# Изъяны
class Flaws(Base):

    size = Column(Integer)
    description = Column(String)
    downgrade_skills_flaws = relationship('DowngradeSkillsDuetoFlaws')
    conflicts_between_flaws_and_features = relationship('ConflictsBetweenFlawsAndFeatures')


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
    upgrade_skills_due_to_features = relationship('UpgradeSkillsDueToFeatures')
    needed_specifications_for_features = relationship('NeededSpecificationsForFeatures')

    def __repr__(self):
        return f"Dices(name={self.name})"

