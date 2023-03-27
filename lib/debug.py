#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///drinks.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(Drinks)
    session.delete(x)

    import ipdb; ipdb.set_trace()