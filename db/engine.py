# creates SQLAlchemy engine (core interface to the DB) that reacts with our DB 

from sqlalchemy import create_engine

Engine = create_engine('sqlite:///database.db', echo=True)