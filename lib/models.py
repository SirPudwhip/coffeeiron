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
            + f"{self.name}, " \
            + f"{self.description}," \
            + f"{self.price},"

class Add_Drinks(Base):
    __tablename__ = 'add_drinks'

    id = Column(Integer(), primary_key=True)
    drink_name = Column(String(), ForeignKey('drinks.name'))
    size = Column(String())
    hot = Column(Boolean())

    def __repr__(self):
        return f"Add ID {self.id},: " +\
            f"{self.drink_name}" +\
            f"{self.size}" +\
            f"{self.hot}" 


# class Orders(Base):
#     __tablename__ = 'orders'
    
#     id = Column(Integer(), primary_key=True)
#     hot = Column(Boolean())
#     size = Column(String())
#     total_price = Column(Integer())
#     drink_id = Column(Integer(), ForeignKey('drinks.id'))
    

# Get the "Drinks" table from the model class
# drinks_table = Drinks.__table__

# # Alter the "description" column to remove it
# drinks_table.c.size.alter(nullable=True)

# # Commit the changes to the database
# session.commit()




# class Customers(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String(), index=True)
#     email = Column(String())
#     phone = Column(Integer())
