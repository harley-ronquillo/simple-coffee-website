from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
# Model = Python class = table in DB
class User(Base):
    __tablename__ = 'users'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    address = Column(String, nullable=False)




