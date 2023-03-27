#!/usr/bin/env python3

# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///drinks.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    drinks = []
    d_1 = Drinks(name="Big Mama", description="caramel, chocolate, and marshmallow flavor", hot=True, size="Large", price=8)
# d_2 = Drinks(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
# d_3 = Drinks(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)

    session.add(d_1)
    session.commit()
    drinks.append(d_1)

    # session.query(Game).delete()
    # session.query(Review).delete()

    # fake = Faker()

    session.close()
# id = Column(Integer(), primary_key=True)
#     name = Column(String(), index=True)
#     description = Column(String())
#     hot = Column(Boolean())
#     size = Column(String())
#     price = Column(Integer())



