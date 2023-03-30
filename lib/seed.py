#!/usr/bin/env python3
from datetime import datetime
# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    
    d_1 = Drinks(name="Big Mama Latte", description="espresso with steamed milk & caramel + chocolate + marshmallow", price=8)
    d_2 = Drinks(name="Gentle Christmas Latte", description="espresso with steamed milk & lavendar + mint", price=7) 
    d_3 = Drinks(name="Matcha Latte", description="steamed milk & matcha", price=7)
    d_4 = Drinks(name="Cappuccino", description="espresso with foam", price=6)
    d_5 = Drinks(name="Americano", description="espresso with hot water", price=5)
    d_6 = Drinks(name="Spicy Pumpkin Latte", description="espresso with steamed milk & cayenne + pumpkin", price=7)
    d_7 = Drinks(name="Latte", description="espresso with steamed milk", price=6)
    d_8 = Drinks(name="Brewed Coffee", description="our daily brew", price=3)
    d_9 = Drinks(name="Mocha", description="espresso with steamed milk & chocolate", price=6)
    d_10 = Drinks(name="Summer Breeze", description="espresso with steamed milk & coconut + vanilla", price=6)



    # a_1 = Add_Drinks(drink_name = 1, size = "M", hot = True)

    # o_1 = Orders(total_price = 10)


    session.query(Orders).delete()
    # session.add_all([d_8, d_7, d_4, d_5, d_9, d_3, d_10, d_6, d_2, d_1])
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





