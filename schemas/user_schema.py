from pydantic import BaseModel
from schemas.weight_schema import WeightCreate, Weight

class UserCreate(BaseModel):
    email: str
    password: str

class UserRegister(UserCreate, WeightCreate):
    name: str
    gender: str

class User(BaseModel):
    id: str
    name: str
    gender: str
    email: str
    is_active: bool
    weights: list[Weight] = []

    class Config:
        orm_mode = True
    

