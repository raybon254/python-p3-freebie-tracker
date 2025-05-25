from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __init__(self,name,founding_year=None):
        self.name = name
        self.founding_year = datetime.now().year

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        return f'<Dev {self.name}>'
    


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name= Column(String())
    value = Column(Integer())

    company_id = Column(Integer,ForeignKey("companies.id"), nullable=False)
    dev_id = Column(Integer,ForeignKey("devs.id"), nullable=False)

    company = relationship("Company", backref="freebies")
    dev = relationship("Dev", backref="freebies")

    def __init__(self,item_name,value):
        self.item_name = item_name
        self.value = value
    



