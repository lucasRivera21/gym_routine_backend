from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from db import Base

class Weight(Base):
    __tablename__ = "weights"

    id = Column(String, primary_key=True, index=True)
    weight = Column(Float)
    unite = Column(String)
    date = Column(Date, default=Date.today())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="weights")