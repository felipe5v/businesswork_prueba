from datetime import date
from os import name
from typing import List, Optional

from pydantic import BaseModel

'''
class DocumentsIn(BaseModel):
    id: int
    owner_id: int
'''

class DocumentsBase(BaseModel):
    name_doc: str
    exp: date
    notif: int
    descrip: str


class DocumentsCreate(DocumentsBase):
    pass


class Documents(DocumentsBase):
    id: int
    name_doc: str
    exp: date
    notif: int
    descrip: str
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    name: str
    last_name: str
    celular: str

class UserIn(BaseModel):
    username    : str
    password    : str


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    username: str
    email: str
    name: str
    last_name: str
    celular: str
    user_password: str
    documents: List[Documents] = []

    class Config:
        orm_mode = True