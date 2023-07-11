# configures and create session factory for interfacing with database (entry point to acquire a Query object)

from sqlalchemy.orm import sessionmaker
from .engine import Engine 

Session = sessionmaker(bind=Engine)