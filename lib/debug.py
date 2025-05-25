#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    company1 = Company("MediTech")
    dev1 = Dev("Brian")
    freebie1 = Freebie("Water bottle", 1000)
    freebie1.company = company1
    freebie1.dev = dev1

    # session.add_all([company1,dev1,freebie1])
    # session.commit()

    print(freebie1.dev)
    print(freebie1.company)
   
    
    

    # import ipdb; ipdb.set_trace()
