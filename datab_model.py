from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column,Integer,String

Base = declarative_base()
class Product(Base):

     __tablename__ = "product"
     
     id = Column(Integer,index=True,primary_key=True)
     name=Column(String)
     address=Column(String)