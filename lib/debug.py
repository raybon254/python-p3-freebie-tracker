#!/usr/bin/env python3
from base import session
from models import Dev, Company, Freebie

if __name__ == '__main__':
    print("\nExploring Seeded Data and Methods")

    # Pick a dev
    dev = session.query(Dev).first()
    print(f"\nDev: {dev.name}")

    print("\nFreebies Collected:")
    for f in dev.freebies:
        print(f"- {f.print_details()}")

    print("\nCompanies they got freebies from:")
    for c in dev.companies:
        print(f"- {c.name}")

    # Received_one
    sample_item = dev.freebies[0].item_name if dev.freebies else 'Sticker'
    print(f"\nDev.received_one('{sample_item}') → {dev.received_one(sample_item)}")

    print(f"Dev.received_one('NonExistentItem') → {dev.received_one('NonExistentItem')}")

    # Create dev to give a freebie to
    receiver = session.query(Dev).filter(Dev.id != dev.id).first()
    if dev.freebies:
        giveaway_item = dev.freebies[0]
        print(f"\nGiving away: {giveaway_item.print_details()}")
        dev.give_away(receiver, giveaway_item)
        session.commit()
        print(f"After giveaway: {giveaway_item.print_details()}")

    # Pick a company
    company = session.query(Company).first()
    print(f"\nCompany: {company.name}, Founded: {company.founding_year}")

    print("\nFreebies Given:")
    for f in company.freebies:
        print(f"- {f.print_details()}")

    print("\nDevs Who Got Freebies from This Company:")
    for d in company.devs:
        print(f"- {d.name}")

    #give_freebie
    print("\nGiving New Freebie:")
    new_freebie = company.give_freebie(receiver, "Debug Mug", 7)
    session.add(new_freebie)
    session.commit()
    print(f"{new_freebie.print_details()}")

    # Test Freebie 
    sample_freebie = session.query(Freebie).first()
    print(f"\nFreebie.print_details(): {sample_freebie.print_details()}")

    #oldest_company 
    oldest = Company.oldest_company(session)
    print(f"\nOldest Company: {oldest.name} (Founded: {oldest.founding_year})")

    import ipdb; ipdb.set_trace()
