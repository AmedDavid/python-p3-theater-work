from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    auditions = relationship('Audition', backref=backref('role'))

    def __repr__(self):
        return f'<Role id={self.id} character_name={self.character_name}>'

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired = [audition for audition in self.auditions if audition.hired]
        return hired[0] if hired else 'no actor has been hired for this role'

    def understudy(self):
        hired = [audition for audition in self.auditions if audition.hired]
        return hired[1] if len(hired) > 1 else 'no actor has been hired for understudy for this role'

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return f'<Audition id={self.id} actor={self.actor} hired={self.hired}>'

    def call_back(self):
        self.hired = True