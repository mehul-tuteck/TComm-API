#TODO: importing necessary module to create table from model using sql_alchemy ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as ormSession



import os


#creating a database engine by specifying the connection details for POstgreSQL db
engine = create_engine(os.getenv("DB_URI"), echo=True, future=True)
#creating session factory to handle databse sessions
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = ormSession(engine)
