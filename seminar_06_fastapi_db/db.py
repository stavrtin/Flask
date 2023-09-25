import databases
import sqlalchemy
from settings import  settings
from fastapi import FastAPI
# from db import DATABASE_URL

# DATABASE_URL = "sqlite:///mydatabase.db"

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
...
engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)




