from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base


class ExerciseUser(Base):

    __tablename__ = "exercises_user"

    id = Column(String, primary_key=True, index=True)
    exercise_id = Column(String, ForeignKey("exercise.id"))
    routine_id = Column(String, ForeignKey("routines.id"))
    weight = Column(Float)
    reps = Column(Integer)
    unite = Column(String)

    exercise = relationship("Exercise", back_populates="exercises_user")
    routines = relationship("Routine", back_populates="exercises_user")