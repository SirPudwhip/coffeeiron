#!/usr/bin/env python3

# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    d_1 = Drinks(name="Big Mama", description="caramel, chocolate, and marshmallow flavor", price=8)
    d_2 = Drinks(name="Gentle Christmas", description="lavendar and mint", price=7) 
    d_3 = Drinks(name="Matcha Latte", description="matcha", price=6)

    a_1 = Add(drink_id = 1, size = "M", hot = True)

    session.add(a_1)
    session.commit()
    session.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # drinks = []


    

# Customers(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String(), index=True)
#     email = Column(String())
#     phone = Column(Integer())

    #customers:
    # c_1 = Customers(name="Mark Twain", email="mark_twain@cloud.com", phone=2234554343)
    # c_2 = Customers(name="Sarah Johnson", email="sarahj@cloud.com", phone=2254545656)
    # c_3 = Customers(name="Blair Rich", email="blair_rich@cloud.com", phone=2234552323)
    

    # session.add(d_1)
    # session.commit()
    # drinks.append(d_1)


    # session.query(Review).delete()

    # fake = Faker()





