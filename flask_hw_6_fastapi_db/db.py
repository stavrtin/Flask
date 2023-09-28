from sqlalchemy import create_engine

from settings import settings
import databases
import sqlalchemy

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users_tab = sqlalchemy.Table("users", metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("first_name", sqlalchemy.String(50)),
                             sqlalchemy.Column("last_name", sqlalchemy.String(50)),
                             sqlalchemy.Column("email", sqlalchemy.String(128)),
                             sqlalchemy.Column("password", sqlalchemy.String(128)),
                             )

orders_tab = sqlalchemy.Table("orders", metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("first_name", sqlalchemy.String(50)),
                             sqlalchemy.Column("last_name", sqlalchemy.String(50)),
                             sqlalchemy.Column("email", sqlalchemy.String(128)),
                             sqlalchemy.Column("password", sqlalchemy.String(128)),
                             )

prods_tab = sqlalchemy.Table("prods", metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("name", sqlalchemy.String(50)),
                             sqlalchemy.Column("description", sqlalchemy.String(50)),
                             sqlalchemy.Column("price", sqlalchemy.String(128))
                             )


# engine = sqlalchemy.create_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
