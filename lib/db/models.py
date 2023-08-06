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

    def __repr__(self):
        output = f"Runner: {self.name} (ID: {self.id})"
        words = output.split()
        for word in words:
            for char in word:
                print(char, end="", flush=True)
                if char != " ":
                    time.sleep(0.009)
            print(" ", end="", flush=True)
        print()
        return ""


class Trail(Base):
    __tablename__ = "trails"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    miles_long = Column(Integer())

    def __repr__(self):
        output = (
            f"Trail:\t{self.name}\n"
            f"Location:\t{self.location}\n"
            f"Length in Miles:\t{self.miles_long}"
        )
        lines = output.split("\n")
        for line in lines:
            for char in line:
                print(char, end="", flush=True)
                if char != " ":
                    time.sleep(0.009)
            print("\n", end="", flush=True)
        return ""


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String())
    miles_long = Column(Integer())
    order = Column(Integer())

    def __repr__(self):
        output = (
            f"Workout:\t{self.name}\n"
            f"Type:\t{self.type}\n"
            f"Length in Miles:\t{self.miles_long}\n"
            f"Workout Number:\t{self.order}"
        )
        lines = output.split("\n")
        for line in lines:
            for char in line:
                print(char, end="", flush=True)
                if char != " ":
                    time.sleep(0.009)
            print("\n", end="", flush=True)
        return ""
