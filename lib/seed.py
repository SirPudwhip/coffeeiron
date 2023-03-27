#!/usr/bin/env python3

# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # drinks = []
    d_1 = Drinks(name="Big Mama", description="caramel, chocolate, and marshmallow flavor", hot=True, size="Large", price=8)
    d_2 = Drinks(name="Gentle Christmas", description="lavendar and mint", hot=True, size="Small", price=7) 
    d_3 = Drinks(name="Matcha Latte", description="matcha", hot=True, size="Small", price=6)

    session.add_all([d_1, d_2, d_3])
    session.commit()
    # drinks.append(d_1)

    # session.query(Game).delete()
    # session.query(Review).delete()

    # fake = Faker()

    session.close()



