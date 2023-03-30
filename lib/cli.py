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
        self.orders = [order for order in session.query(Orders)]
        # self.customers = [customer for customer in session.query(Customers)]
        self.name = user_input
        self.start()

    

    def start(self):
        print(' ')
        print(f'***** Welcome To CoffeeIron, {self.name} *****')
        print(' ')
        exit = False
        while exit == False:
            choice = input("Type 'new', 'list', 'modify', 'delete': ")
            if choice.lower() == "new":
                self.new_order()
            elif choice.lower() == "modify":
                order_obj = input("What is the ID of the order you want to modify? ")
                order_item = (session.query(Orders).filter(Orders.id == order_obj)).first()
                self.handle_order(order_item, "Modifying Exiting Order Number")
            elif choice.lower() == "list":
                for order in self.orders:
                    print(f"{order.id}. {order.ordered_at}")
                    for add_drink in self.add_drinks:
                        if add_drink.order_number == order.id:
                            print(f"{add_drink.drink_name}") 
            elif choice.lower() == "delete":
                print(Orders)
                self.delete_item(Orders)       
            elif choice.lower() == "exit":
                exit = True


    def new_order(self):
        new_order = Orders(total_price = 0)
        session.add(new_order)
        session.commit()
        self.handle_order(new_order, "Serving New Order Number")

    def handle_order(self, new_order, heading):
    
        print(' ')
        print(f'***** {heading} {new_order.id} *****')
        print(' ')
        exit = False
        while exit == False:
            price_list = [drink_obj.size_price for drink_obj in session.query(Add_Drinks).filter(Add_Drinks.order_number == new_order.id)]
        
            price_total = sum(price_list)
            query = session.query(Orders).filter(Orders.id == new_order.id)
            query.update({Orders.total_price: price_total})
            session.commit()

            choice = input("Type 'list items', 'show menu', 'add', 'modify','delete' or 'checkout': ")
            if choice.lower() == "show menu":
                for drink in self.drinks:
                    print(f"{drink.name}: {drink.description}")
            elif choice.lower() == "list items":
                self.list_items(new_order)
                print(f"The current total is: ${price_total} ")
            elif choice.lower() == "add":
                self.add_item(new_order)
                print("Your item has been added!")
            elif choice.lower() == "modify":
                self.list_items(new_order)
                self.modify_item()
            elif choice.lower() == "delete":
                self.list_items(new_order)
                self.delete_item(Add_Drinks)
            elif choice.lower() == "checkout":
                self.checkout(price_total)
                exit = True
            else:
                exit = True

            

    # def new_start(self):
    #     print("Building New Order")

    def checkout(self, price_total):
        print (f"Your total is : ${price_total}")
        payment = input("cash or credit? ")
        if payment.lower() == "cash":
            amount = input("Enter dollar amount: $")
            cash_back = int(amount) - price_total 
            print(f"Change due : ${cash_back}")
        elif payment.lower() == "credit":
            print("Payment accepted!")
        print("Thanks for visiting CoffeeIron! We hope to see you again soon")


    def list_items(self, new_order):
        for order in self.orders:
            if order.id == new_order.id:
                print(f"{order.id}. {order.ordered_at}")
                drink_list = session.query(Add_Drinks).filter(Add_Drinks.order_number == new_order.id)
                for add_drink in drink_list:
                    print(f"{add_drink.id}. {add_drink.drink_name}") 
                        

    def set_price(self, drink, size):
        
        query = session.query(Drinks).filter(Drinks.name == drink)
        searched_drink = query.first()
        if size.lower() == "medium":
            return searched_drink.price + 1
        elif size.lower() =="large":
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
        selection = input("Item ID: ")
        field = input("Specification to update: ")
        value = input("New specification: ")

        first_query = session.query(Add_Drinks).filter(Add_Drinks.id == selection)
        if field.lower() == "size":
            first_query.update({Add_Drinks.size: value})
            print("Item modified")
        elif field.lower() == "hot":
            if value.lower() == "true":
                temp = True
            elif value.lower() == "false":
                temp = False
            else:
                print("Invalid value for hot field. Please enter 'true' or 'false'.")
            first_query.update({Add_Drinks.hot: temp})
            print("Item modified")
        elif field.lower() == "drink name":
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
        session.commit()
        string_var = "You have deleted the" if query_type == Add_Drinks else "You deleted order ID:"
        print_var = doomed_item.drink_name if query_type == Add_Drinks else doomed_item.id

        print(f"{string_var} {print_var} ")

    
    
    
    

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    test = CLI(user_input)

# import ipdb; ipdb.set_trace()


