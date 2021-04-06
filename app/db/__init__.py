from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()


# connect to database using env variable

#manages overall connection to db

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

#generates tem connections for CREATE, READ, UPDATE, DELETE
Session = sessionmaker(bind=engine)

#helps map the models to real MySQL tables. 
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)

#function that returns new session-connection object. Functions saves current connection on g object if its not already there.
def get_db():
    if "db" not in g:
        g.db = Session()

    return g.db

def close_db(e=None):
    #pop() finds and remove db from g object.  If db exists(doesn't === None) then db.close()
    db = g.pop("db", None)

    if db is not None:
      db.close()