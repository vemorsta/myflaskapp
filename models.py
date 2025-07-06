import sqlalchemy as sa
from sqlalchemy.orm import declarative_base , sessionmaker, relationship


Base = declarative_base()

class user(Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer,primary_key=True)
    username = sa.Column(sa.String(225), nullable= False)
    password = sa.Column(sa.Integer)
    

class Card(Base):
    __tablename__ = "Card"
    id = sa.Column(sa.Integer,primary_key=True)
    name = sa.Column(sa.String(225), nullable= False)
    



engine = sa.create_engine("sqlite:///site.db")
Base.metadata.create_all(engine)

sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()