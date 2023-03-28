from datetime import datetime

from sqlalchemy import create_engine, desc
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
            + f"{self.name}, " 


class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer(), primary_key=True)
    hot = Column(Boolean())
    size = Column(String())
    total_price = Column(Integer())
    drink_id = Column(Integer(), ForeignKey('drinks.id'))
    






# class Customers(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String(), index=True)
#     email = Column(String())
#     phone = Column(Integer())
