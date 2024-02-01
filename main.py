from fastapi import FastAPI
from sqlalchemy.orm import Session
from db import engine, SessionLocal, Base
from routes import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.user)

@app.get("/")
def read_root():
    return {"Hello": "World"}