#!/usr/bin/env python3
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///coffeeiron.db')
Session = sessionmaker(bind=engine)
session = Session()

class CLI: 
    def __init__(self, user_input):
        self.drinks = [drink for drink in session.query(Drinks)]
        self.add = [add for add in session.query(Add)]
        # self.customers = [customer for customer in session.query(Customers)]
        self.name = user_input
        self.start()

    def start(self):
        session.add(Add(drink_id = 1, size = "M", hot = False))
        session.commit()

        print(' ')
        print(f'***** Welcome To The Coffee Shop {self.name} *****')
        print(' ')

    @property
    def show_drinks(self):
        print(self.drinks)
    
    @property
    def show_customers(self):
        print(self.customers)
    
    

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    test = CLI(user_input)

import ipdb; ipdb.set_trace()