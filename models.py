from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATE
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id= Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    celular = Column(String, index=True)
    user_password = Column(String)

    documents = relationship("Documents", back_populates="owner")


class Documents(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name_doc = Column(String, index=True)
    exp = Column(DATE, index=True)
    notif = Column(Integer)
    descrip = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="documents")