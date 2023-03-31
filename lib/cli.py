#!/usr/bin/env python3
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.markdown import Markdown
from models import *
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
import time
from rich.progress import track

engine = create_engine('sqlite:///coffeeiron.db')
Session = sessionmaker(bind=engine)
session = Session()

MARKDOWN = """
# Welcome to CoffeeIron! 

Please select your desired function by number
1. Create a new order
2. See all open orders
3. Modify an existing order
4. Complete an order
5. Exit
"""

console = Console()
md = Markdown(MARKDOWN)

single_order = """
# Single Order Screen

Please select your desired function by number
1. Show drinks menu
2. List current order items
3. Add a new item
4. Modify an existing item
5. Delete an item 
6. Checkout 

"""

console = Console()
so = Markdown(single_order)

class CLI: 
    def __init__(self):
        self.drinks = [drink for drink in session.query(Drinks)]
        self.add_drinks = [add for add in session.query(Add_Drinks)]
        self.orders = [order for order in session.query(Orders)]
        self.start()

    def start(self):
        exit = False
        while exit == False:
            console.print(md)
            choice = input("Selection: ")
            if choice == "1":
                self.new_order()
            elif choice == "3":
                self.create_table_list()
                order_obj = input("Order #: ")
                order_item = (session.query(Orders).filter(Orders.id == order_obj)).first()
                self.handle_order(order_item, "Modifying Existing Order Number")
            elif choice == "2":
                self.create_table_list()
                input("Done? ")
            elif choice == "4":
                self.create_table_list()
                self.delete_item(Orders)       
            elif choice == "5":
                exit = True


    def create_table_list(self):
        table = Table(title="Current Active Orders", header_style="bold black on white", style="bold black on white", show_lines=False)
        table.add_column("Order", justify="center", style="bold black on white", no_wrap=True)
        table.add_column("Size", justify="center", style="bold black on white")
        table.add_column("Price", justify="center", style="bold black on white")

        query_list_order = [order for order in session.query(Orders)]
        query_list_drink = [drink for drink in session.query(Add_Drinks)]

        for order in query_list_order:
            table.add_row('____________________','____________________', '____________________')
            table.add_row(f'ORDER # {order.id}', 'Sizes:', 'Cost:')
            table.add_row('', '', '')
            for add_drink in query_list_drink:
                if add_drink.order_number == order.id:
                    table.add_row(f'{add_drink.drink_name}', f'{add_drink.size}', f'${add_drink.size_price}')
            table.add_row('', '', f'Total: ${order.total_price}')

        console = Console()
        console.print(table)

    def new_order(self):
        new_order = Orders(total_price = 0)
        session.add(new_order)
        session.commit()
        self.handle_order(new_order, "Serving New Order Number")

    def handle_order(self, new_order, heading):
        exit = False
        while exit == False:
            console.print(so)
            price_list = [drink_obj.size_price for drink_obj in session.query(Add_Drinks).filter(Add_Drinks.order_number == new_order.id)]
        
            price_total = sum(price_list)
            query = session.query(Orders).filter(Orders.id == new_order.id)
            query.update({Orders.total_price: price_total})
            session.commit()

            choice = input("Selection: ")
            if choice == "1":
                self.print_menu()
                input("Done?")
            elif choice == "2":
                self.list_items(new_order)
                print(f"The current total is: ${price_total} ")
                input("Done?")
            elif choice == "3":
                self.add_item(new_order)
                print("Your item has been added!")
            elif choice == "4":
                self.list_items(new_order)
                self.modify_item()
            elif choice == "5":
                self.list_items(new_order)
                self.delete_item(Add_Drinks)
            elif choice == "6":
                self.checkout(price_total)
                input("To Main Menu")
                exit = True
            else:
                exit = True


    def print_menu(self):
        table = Table(title="Coffee Menu", padding=1,header_style="bold black on #C59E6B", style="bold black on #C59E6B")
        table.add_column("Name", justify="center", style="bold black on #C59E6B")
        table.add_column("Description", justify="center", style="bold black on #C59E6B", no_wrap=True)
        table.add_column("Price", justify="center", style="bold black on #C59E6B")

        query_list_drinks = [drink for drink in session.query(Drinks)]
        for drink in query_list_drinks:
            table.add_row(f'{drink.name}',f'{drink.description}',f'${drink.price}')

        console = Console()
        console.print(table)


    def checkout(self, price_total):
        print (f"Your total is : ${price_total}")
        payment = input("cash or credit? ")
        if payment == "cash":
            amount = input("Enter dollar amount: $")
            cash_back = int(amount) - price_total 
            print(f"Change due : ${cash_back}")
        elif payment == "credit":
            for i in track(range(120), description="Processing Payment..."):
                time.sleep(.02)
            print("Payment accepted!")

        print("Thanks for visiting CoffeeIron! Stick around... there's always an afterparty")


    def list_items(self, new_order):
        table = Table(title="Current Item", padding=1,header_style="bold black on #C59E6B", style="bold black on #C59E6B")
        table.add_column("Drink #", justify="center", style="bold black on #C59E6B")
        table.add_column("Name", justify="center", style="bold black on #C59E6B")
        table.add_column("Size", justify="center", style="bold black on #C59E6B")
        table.add_column("Hot / Iced", justify="center", style="bold black on #C59E6B")
        table.add_column("Price", justify="center", style="bold black on #C59E6B")

        drink_list = session.query(Add_Drinks).filter(Add_Drinks.order_number == new_order.id)
        for add_drink in drink_list:
            hot_var = "Hot" if add_drink.hot else "Iced"
            table.add_row(f'{add_drink.id}',f'{add_drink.drink_name}',f'{add_drink.size}',f'{hot_var}',f'{add_drink.size_price}')

        console = Console()
        console.print(table)
                        

    def set_price(self, drink, size):
        query = session.query(Drinks).filter(Drinks.name == drink)
        searched_drink = query.first()
        if size == "medium":
            return searched_drink.price + 1
        elif size =="large":
            return searched_drink.price + 2
        else:
            return searched_drink.price
       

    def add_item(self, new_order):
        print(new_order)
        name = input("Drink name: ")
        size = input("Size: ")
        size_price = self.set_price(name, size)
        hot = input("Hot? (y/n) : ")
        temp = True if hot == "y" else False
        
        session.add(Add_Drinks(drink_name = name, size = size, hot = temp, order_number = new_order.id, size_price = size_price))
        session.commit()

    def modify_item(self):
        selection = input("Drink #: ")
        field = input("Specification to update: ")
        value = input("New specification: ")

        first_query = session.query(Add_Drinks).filter(Add_Drinks.id == selection)
        if field == "size":
            first_query.update({Add_Drinks.size: value})
            print("Item modified")
        elif field == "temp":
            if value.lower() == "hot":
                temp = True
            elif value.lower() == "iced":
                temp = False
            else:
                print("Invalid value for hot field. Please enter 'true' or 'false'.")
            first_query.update({Add_Drinks.hot: temp})
            print("Item modified")
        elif field == "name":
            first_query.update({Add_Drinks.drink_name: value})
            print("Item modified")
        else:
            print("Invalid field. Please enter 'size', 'hot', or 'drink name'.")

        session.commit()

        reconfigure = first_query.first()
        drinks_arg = reconfigure.drink_name
        size_arg = reconfigure.size
        new_price = self.set_price(drinks_arg, size_arg)
        first_query.update({Add_Drinks.size_price: new_price})
        session.commit()

    def delete_item(self, query_type):
        selection = input("ID: ")
        query = session.query(query_type).filter(query_type.id == selection)  
        doomed_item = query.first()
        session.delete(doomed_item)

        if query_type == Orders:
            session.query(Add_Drinks).filter(Add_Drinks.order_number == selection).delete()
        session.commit()

        string_var = "You have deleted the" if query_type == Add_Drinks else "Completed order #:"
        print_var = doomed_item.drink_name if query_type == Add_Drinks else doomed_item.id

        print(f"{string_var} {print_var} ")


    

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # user_input = input("Enter Your Name: ")
    test = CLI()

# import ipdb; ipdb.set_trace()


