from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
# Model = Python class = table in DB
class Order(Base):
    __tablename__ = 'orders'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
