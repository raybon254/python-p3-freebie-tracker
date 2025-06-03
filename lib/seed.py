#!/usr/bin/env python
from faker import Faker
from models import Dev,Freebie,Company
from base import session,create_all
import random

fake = Faker()

# Script goes here!
def seed_data():
    print(f"Seeding data")
    create_all()
    companies = []
    for _ in range(10):
        company = Company(
            name=fake.company(),
            founding_year=random.randint(2005,2021)
        )
        companies.append(company)
        session.add(company)

    devs = []
    for _ in range(10):
        dev = Dev(
            name=fake.name()
        )
        devs.append(dev)
        session.add(dev)

    
    # My Junction -> Many to Many table 
    for dev in devs:
        related_companies = random.sample(companies, random.randint(1,5))
        for company in related_companies:
            dev.companies.append(company)
    session.commit()

    items = ['Flask', 'Tshirts', 'FlashDisks', 'Notebook', 'Pens','HardDisks',"Vouchers"]
    for _ in range(15):
        freebie = Freebie(
            item_name=random.choice(items),
            value=random.randint(1,10),
            company=random.choice(companies),
            dev=random.choice(devs)
        )
        session.add(freebie)

    session.commit()
    print(f"Seeding complete.")


if __name__ == "__main__":
    seed_data()
