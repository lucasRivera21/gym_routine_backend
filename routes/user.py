from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import engine, SessionLocal, Base
from schemas import user_schema
from models import user_model
from passlib.context import CryptContext
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user = APIRouter(prefix="/user", tags=["User"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/")
def read_user():
    return {"Hello": "User"}