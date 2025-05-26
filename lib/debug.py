#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

from models import Company, Dev, Freebie

# utilities
def get_dev(name):
    return session.query(Dev).filter_by(name=name).first()


if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    company1 = Company("TechCorp", founding_year=1995)
    dev1 = Dev("Alice")
    freebie1 = company1.give_freebie(dev1, "Laptop Sticker", 5)

    session.add_all([company1, dev1, freebie1])
    session.commit()

    print("Freebie Created:", freebie1.print_details()) 

    company2 = Company("OldCo", founding_year=1980)
    session.add(company2)
    session.commit()
    print("Oldest Company:", Company.oldest_company(session))

    dev2 = Dev("Bob")
    session.add(dev2)
    session.commit()

    dev1.give_away(dev2, freebie1)
    session.commit()
    print("After Giveaway:", freebie1.print_details())

    print("\nAll Freebies:")
    for f in session.query(Freebie).all():
        print(f.print_details())
    
    

    import ipdb; ipdb.set_trace()
