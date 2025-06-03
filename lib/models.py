from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from sqlalchemy.orm import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# relations
company_dev = Table('company_dev', Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True)
)


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    devs = relationship('Dev', secondary='company_dev', back_populates='companies')

    def __init__(self,name,founding_year=None):
        self.name = name
        self.founding_year = founding_year if founding_year is not None else datetime.now().year


    # Aggregate methods

    def give_freebie(self, dev, item_name, value):
        if not isinstance(dev, Dev):
            raise ValueError("Expected a Dev instance.")
        freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        return freebie
    
    @classmethod
    def oldest_company(cls,session):
        return session.query(cls).order_by(cls.founding_year.asc()).first()

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    companies = relationship('Company', secondary='company_dev', back_populates='devs')


    def __init__(self,name):
        self.name = name

   
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    
    def give_away(self, dev, freebie):
        if not isinstance(dev, Dev):
            raise ValueError("Dev instance not found.")
        if not isinstance(freebie, Freebie):
            raise ValueError("Freebie instance not found.")
        if freebie.dev != self:
            raise ValueError("Freebie that doesn't belong to this dev can't be given away.")
        freebie.dev = dev


        
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

    def __init__(self,item_name,value,company,dev):
        self.item_name = item_name
        self.value = value
        self.company = company
        self.dev = dev
   
    # Aggregate methods
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."
        
    



