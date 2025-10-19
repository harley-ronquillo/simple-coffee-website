from sqlalchemy import Column, Integer, String, Table
from app.Config.db import meta, engine

users = Table(
    "users", meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False),
    Column('email', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('contact_number', String(20), nullable=False),
    Column('address', String(255), nullable=False),
)