from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
# Model = Python class = table in DB
class Category(Base):
    __tablename__ = 'categories'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    product = relationship("Product", back_populates="category")





