from pydantic import BaseModel
from datetime import datetime

class WeightCreate(BaseModel):
    weight: float
    unite: str
    date: datetime.date = datetime.date.today()

class Weight(BaseModel):
    id: str
    weight: float
    unite: str
    date: datetime.date

    class Config:
        orm_mode = True