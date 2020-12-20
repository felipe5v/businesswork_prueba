from typing import Dict
from sqlalchemy.orm import Session
'''
import hashlib 
result = hashlib.md5(b'GeeksforGeeks') 
'''
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_documents_id(db: Session, id: int):
    return db.query(models.Documents).filter(models.Documents.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

'''
def update_documents(db:Session, user_id: int, document:schemas.Documents):
    user = db.query(models.Documents).filter(models.Documents.owner_id == user_id).first()
    db_document = models.Documents(name_doc=document.name_doc)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
'''

def create_user(db: Session, user: schemas.UserCreate):
    n_password = user.password
    db_user = models.User(username=user.username, email=user.email, name=user.name, last_name=user.last_name, celular=user.celular, user_password=n_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_document(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Documents).offset(skip).limit(limit).all()



def create_user_document(db: Session, document: schemas.DocumentsCreate, user_id: int):
    db_documemt = models.Documents(**document.dict(), owner_id=user_id)
    db.add(db_documemt)
    db.commit()
    db.refresh(db_documemt)
    
    return db_documemt

'''
database_documents = Dict[str, schemas.Documents]

def get_documents(db: Session, id_doc: int ):
    if(id_doc in database_documents.keys()):
        return database_documents[name_doc]
    else:
        return None


def update_documents(document_db: schemas.Documents):
    database_documents[document_db.id] = document_db
    return document_db
'''