from sqlalchemy import Column, Integer, String, Table, ForeignKey, Text
from app.Config.db import meta

products = Table(
    "products", meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False),
    Column('description', Text, nullable=True),
    Column('image_url', String(255), nullable=False),
    Column('price', Integer, nullable=False),
    Column('category_id', Integer, ForeignKey('categories.id'), nullable=False),
)