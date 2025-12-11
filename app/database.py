from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine("postgresql://user:pass@localhost:5432/ecommerce")
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
