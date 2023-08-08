from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db.models import *

engine = create_engine("sqlite:///lib/db/marathon.db")
session = sessionmaker(bind=engine)()


def get_all_runners():
    return session.query(Runner).all()


def find_runner_by_id(id):
    return session.get(Runner, id)


def update_runner_miles(runner, trail):
    workout = get_workout_details(runner)
    if workout:
        runner.miles_run += workout.miles_long

        new_run = Run(
            date=datetime.now(),
            runner_id=runner.id,
            workout_id=workout.id,
            trail_id=trail.id,
        )

        session.add(new_run)
        session.commit()
        return runner
    else:
        return None


def set_runner_to_zero(runner):
    runner.miles_run = 0
    session.query(Run).filter_by(runner_id=runner.id).delete()
    session.commit()
    return runner


def add_runner_to_db(runner):
    new_runner = Runner(
        name=runner,
        miles_run=0,
    )
    session.add(new_runner)
    session.commit()


def runner_workout(runner):
    last_workout = (
        session.query(Workout)
        .join(Run)
        .filter(Run.runner_id == runner.id)
        .order_by(Workout.id.desc())
        .first()
    )
    if last_workout:
        print(
            f"Last workout completed: {last_workout.name} which was {last_workout.type} and {last_workout.miles_long} miles long."
        )
    else:
        print("No workouts have yet been completed. Someone has a lot of work to do!")
    print_workout_details(runner)


def get_workout_details(runner):
    last_workout = (
        session.query(Workout)
        .join(Run)
        .filter(Run.runner_id == runner.id)
        .order_by(Workout.id.desc())
        .first()
    )
    if last_workout:
        workout = (
            session.query(Workout)
            .filter(Workout.id > last_workout.id)
            .order_by(Workout.id)
            .first()
        )
    else:
        workout = None
    return workout


def print_workout_details(runner):
    workout = get_workout_details(runner)
    if workout:
        print(
            f"Today's Workout: {workout.name} will be {workout.type} and you'll be running {workout.miles_long} miles."
        )
    else:
        first_workout = session.query(Workout).order_by(Workout.order).first()
        if first_workout:
            print(
                f"Today's Workout: {first_workout.name} will be {first_workout.type} and you'll be running {first_workout.miles_long} miles."
            )
        else:
            print(
                "Congratulations! You are ready for the marathon. Time to carb load :)"
            )


def get_all_trails():
    return session.query(Trail).all()


def find_trail_by_id(id):
    return session.get(Trail, id)
