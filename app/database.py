
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine("sqlite:///ecommerce.db", connect_args={"check_same_thread": False})
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
