from pydantic import BaseModel
from schemas.weight_schema import WeightCreate, Weight
from enum import Enum

class Gender(Enum):
    M = "M"
    F = "F"

class UserCreate(BaseModel):
    email: str
    password: str

class UserRegister(UserCreate, WeightCreate ):
    name: str
    gender: Gender

class User(BaseModel):
    id: str
    name: str
    gender: Gender
    email: str
    is_active: bool
    weights: list[Weight] = []

    class Config:
        orm_mode = True
    

