from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


engine = create_engine('sqlite:///freebies.db')   
Session = sessionmaker(bind=engine)
session = Session()


# creating table
def create_all():
    Base.metadata.create_all(engine)