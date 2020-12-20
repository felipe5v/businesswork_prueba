from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://ouhmtdlffbgsax:eb19dfabd2e91a0a94272669c2f3369cc5c7dcd14feb18879b4bf2405efc70a1@ec2-34-200-101-236.compute-1.amazonaws.com:5432/d57f1ik60e43kn"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()