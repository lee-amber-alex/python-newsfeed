from app.db import Base
from sqlalchemy import Column, Integer, String
# to validate data before inserting into db
from sqlalchemy.orm import validates
# for password encryption
import bcrypt

# open source software for event-driven IT automation, remote task execution, and configuration management
salt = bcrypt.gensalt()


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates("password")
  def validate_password(self, key, password):
   assert len(password) > 4
  # returns an encrypted version of the password if assert doesn't throw an error.
   return bcrypt.hashpw(password.encode("utf-8"), salt)

# "assert" makes sure email address includes @ character
  @validates("email")
  def validate_email(self, key, email):
   assert "@" in email

   return email 
