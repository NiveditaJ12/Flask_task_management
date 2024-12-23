from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///tasklist_db.db',connect_args={'check_same_thread': False})
DBengine = sessionmaker(bind = engine)
session = DBengine()