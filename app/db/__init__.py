from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable

#manages overall connection to db
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

#generates tem connections for CREATE, READ, UPDATE, DELETE
Session = sessionmaker(bind=engine)

#helps map the modelts to real MySQL tables. 
Base = declarative_base()