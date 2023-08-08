from ipdb import set_trace
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from db.models import *

engine = create_engine("sqlite:///db/marathon.db")
session = sessionmaker(bind=engine)()


def cumulative_miles(runner):
    runner_miles = (
        session.query(func.sum(Workout.miles_long))
        .join(Run)
        .filter(Run.runner_id == runner.id)
        .scalar()
    )
    return runner_miles
