# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Runner(Base):
    __tablename__ = "runners"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    miles_run = Column(Integer())

    runs = relationship("Run", back_populates="runner")

    def __repr__(self):
        output = f"Runner: {self.name} (ID: {self.id})"
        return output


class Trail(Base):
    __tablename__ = "trails"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    miles_long = Column(Integer())

    runs = relationship("Run", back_populates="trail")

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

    runs = relationship("Run", back_populates="workout")

    def __repr__(self):
        output = (
            f"Workout: {self.name}\n"
            f"Type: {self.type}\n"
            f"Length in Miles: {self.miles_long}\n"
            f"Workout Number: {self.order}"
        )
        return output


class Run(Base):
    __tablename__ = "runs"

    id = Column(Integer(), primary_key=True)
    date = Column(DateTime())
    runner_id = Column(Integer(), ForeignKey("runners.id"))
    workout_id = Column(Integer(), ForeignKey("workouts.id"))
    trail_id = Column(Integer(), ForeignKey("trails.id"))

    runner = relationship("Runner", back_populates="runs")
    workout = relationship("Workout", back_populates="runs")
    trail = relationship("Trail", back_populates="runs")

    def __repr__(self):
        output = (
            f"Date: {self.date}\n"
            f"Runner: {self.runner_id}\n"
            f"Workout: {self.workout_id}\n"
            f"Trail: {self.trail_id}"
        )
        return output
