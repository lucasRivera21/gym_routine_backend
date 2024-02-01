from sqlalchemy import Column, String, Boolean

from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    gender = Column(String)
    is_active = Column(Boolean, default=True)

    weights = relationship("Weight", back_populates="user")
    routines = relationship("Routine", back_populates="user")