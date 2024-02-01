from pydantic import BaseModel
from datetime import datetime, date

class WeightCreate(BaseModel):
    weight: float
    unite: str
    date: datetime = date.today()

class Weight(BaseModel):
    id: str
    weight: float
    unite: str
    date: datetime

    class Config:
        orm_mode = True