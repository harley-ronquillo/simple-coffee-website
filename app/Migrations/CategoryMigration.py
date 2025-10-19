from sqlalchemy import Column, Integer, String, Table
from app.Config.db import meta

categories = Table(
    "categories", meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False),
)