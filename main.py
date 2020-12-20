from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://localhost:8081",
]
app.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

########################

@app.post("/login/")
async def auth_user(userAuth: schemas.UserIn, db: Session = Depends(get_db)):
    user_in_db = crud.get_user_by_username(db, username=userAuth.username)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if user_in_db.user_password != userAuth.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return  {"Autenticado": True}

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username no disponible")
    return crud.create_user(db=db, user=user)

##############

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username no disponible")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/documents/", response_model=schemas.Documents)
async def create_document_for_user(
    user_id: int, document: schemas.DocumentsCreate, db: Session = Depends(get_db)
):
    return crud.create_user_document(db=db, document=document, user_id=user_id)

@app.get("/documents/", response_model=List[schemas.Documents])
async def read_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    documents = crud.get_document(db, skip=skip, limit=limit)
    return documents


@app.put("/users/documents/", response_model=schemas.Documents)
async def update_doc(docu: int, document: schemas.Documents, db: Session = Depends(get_db)):
    documento_in = crud.get_documents_id(db, docu)
    documento_in.name_doc=document.name_doc
    documento_in.notif=document.notif
    db.commit()
    return documento_in

'''
    if documento_in == None:
        raise HTTPException(status_code=404, detail="El documento no existe")

    documento_in
    crud.update_document(documento_in)

    document_inn = schemas.Documents(**schemas.DocumentsIn.dict(), docu=documento_in)
    document_inn = 
'''

