from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
# Model = Python class = table in DB
class Product(Base):
    __tablename__ = 'products'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category = relationship("Category", back_populates="product")
    order = relationship("Order", back_populates="product")






