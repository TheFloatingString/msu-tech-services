from sqlalchemy import Table, Column, Integer, Float, String, MetaData, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash

import bcrypt
import uuid

import random
import datetime
import os
# 
# from src import read_credentials

# get credentials
# keys = read_credentials.return_keys()

engine = create_engine(os.environ["DATABASE_URL"])

meta = MetaData()
Base = declarative_base()

class Discount(Base):
	__tablename__ = "discounts"

	id = Column(Integer, primary_key=True, unique=True, nullable=False, default=random.randint(0,2**30))
	name = Column(String, nullable=False)
	description = Column(String)
	provider = Column(String)
	address = Column(String)
	website = Column(String)
	creator_id = Column(Integer)
	creator_name = Column(String)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)

	def create_discount(name, description, provider, creator_id, creator_name, address=None, website=None):
		self.name = name
		self.description = description
		self.provider = provider
		self.address = address
		self.website = website
		self.creator_id = creator_id
		self.creator_name = creator_name
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, unique=True, nullable=False, default=random.randint(0,2**31))
	username = Column(String)
	first_name = Column(String)
	last_name = Column(String)
	email = Column(String(512))
	password_hash = Column(String(4096))
	description = Column(String)
	creation_date = Column(DateTime)
	modified_date = Column(DateTime)	

	def create_user(self, username, first_name, last_name, email, password, description=None):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		self.description = description
		self.creation_date = datetime.datetime.now()
		self.modified_date = datetime.datetime.now()

if __name__ == "__main__":
	Base.metadata.create_all(engine)