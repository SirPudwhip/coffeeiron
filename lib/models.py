from datetime import datetime

from sqlalchemy import create_engine, desc, func
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///coffeeiron.db')
Base = declarative_base()

class Drinks(Base):
    __tablename__ = 'drinks'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    description = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f"Drink ID {self.id}: " \
            + f"{self.name}, " \
            + f"{self.description}," \
            + f"{self.price},"

class Add_Drinks(Base):
    __tablename__ = 'add_drinks'

    id = Column(Integer(), primary_key=True)
    drink_name = Column(String(), ForeignKey('drinks.name'))
    size = Column(String())
    hot = Column(Boolean())
    order_number = Column(Integer(), ForeignKey('orders.id'))
    size_price = Column(Integer())

    def __repr__(self):
        return f"Add ID {self.id}: " +\
            f"{self.drink_name}" +\
            f"{self.size}" +\
            f"{self.hot}" 


class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer(), primary_key=True)
    ordered_at = Column(DateTime(), server_default=func.now())
    total_price = Column(Integer())

    def __repr__(self):
        return f"Orders ID {self.id}: " +\
            f"{self.ordered_at}" +\
            f"{self.total_price}"


# class Customers(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String(), index=True)
#     email = Column(String())
#     phone = Column(Integer())
