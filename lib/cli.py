#!/usr/bin/env python3
from models import *
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///coffeeiron.db')
Session = sessionmaker(bind=engine)
session = Session()

class CLI: 
    def __init__(self, user_input):
        self.drinks = [drink for drink in session.query(Drinks)]
        self.add_drinks = [add for add in session.query(Add_Drinks)]
        # self.customers = [customer for customer in session.query(Customers)]
        self.name = user_input
        self.start()

    def start(self):
        # session.add(Add_Drinks(drink_name = "Big Mama", size = "M", hot = False))
        # session.commit()

        print(' ')
        print(f'***** Welcome To The Coffee Shop {self.name} *****')
        print(' ')
        exit = False
        while exit == False:
            choice = input("Type 'list', 'add', 'modify', or 'delete': ")
            if choice == "list":
                for drink in self.drinks:
                    print(f"{drink.name}: {drink.description}")
            elif choice == "add":
                self.add_item()
                print("Your item has been added!")
            elif choice == "modify":
                self.modify_item()
                print("You modified your item!")
            elif choice == "delete":
                self.delete_item()
                print("delete item")
            else:
                choice == "exit"
                exit = True

    def add_item(self):
        name = input("Drink name: ")
        size = input("Size: ")
        hot = input("Hot? (y/n) : ")
        temp = True if hot == "y" else False
        
        session.add(Add_Drinks(drink_name = name, size = size, hot = temp ))
        session.commit()

    def modify_item(self):
        
        selection = input("Item ID: ")
        field = input("Specification to update: ")
        value = input("New specification: ")

        first_query = session.query(Add_Drinks).filter(Add_Drinks.id == selection)
        first_query.update({Add_Drinks.size: value})
        session.commit()

        # stmt = (
        #     update(Add_Drinks)
        #     .where(Add_Drinks.id == selection)
        #     .values(field=value)
        #     )

        # print(stmt)
        
        print("item modified")

    def delete_item(self):
        print("item deleted")

    
    
    
    

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    test = CLI(user_input)

# import ipdb; ipdb.set_trace()