from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)  # Telegram ID
    role = Column(String(50), default="employee")  # "admin" или "employee"
