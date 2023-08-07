# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker
import time

engine = create_engine("sqlite:///marathon.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()


class Runner(Base):
    __tablename__ = "runners"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    miles_run = Column(Integer())
    trail_id = Column(Integer(), ForeignKey("trails.id"))
    workout_id = Column(Integer(), ForeignKey("workouts.id"))

    trail = relationship("Trail", back_populates="runners")
    workout = relationship("Workout", back_populates="runners")

    def __repr__(self):
        output = f"Runner: {self.name} (ID: {self.id})"
        return output


class Trail(Base):
    __tablename__ = "trails"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    miles_long = Column(Integer())

    runners = relationship("Runner", back_populates="trail")

    def __repr__(self):
        output = (
            f"Trail: {self.name}\n"
            f"Location: {self.location}\n"
            f"Length in Miles: {self.miles_long}"
        )

        return output


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String())
    miles_long = Column(Integer())
    order = Column(Integer())

    runners = relationship("Runner", back_populates="workout")

    def __repr__(self):
        output = (
            f"Workout: {self.name}\n"
            f"Type: {self.type}\n"
            f"Length in Miles: {self.miles_long}\n"
            f"Workout Number: {self.order}"
        )
        return output
