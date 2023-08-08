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


def get_all_runners():
    return session.query(Runner).all()


def find_runner_by_id():
    return session.get(Runner, id)


def runner_workout(runner):
    workout = session.query(Workout).join(Run).filter(Run.runner_id == runner.id)
    return workout.name


def print_workout_details(runner):
    workout = session.query(Workout).join(Run).filter(Run.runner_id == runner.id)
    print(
        f"Today's Workout: {workout.name} will be {workout.type} and you'll be running {workout.miles_long} miles."
    )


def print_runner_info(runner):
    print(
        f"Runner: {runner.name} | Miles Run: {runner.miles_run} | Current Workout: {runner_workout(runner)} | ID: {runner.id}"
    )


def get_runner_ranking(runner):
    pass


def invalid_choice():
    print("Invalid choice. Nice try. Please choose again!")


def get_all_trails():
    return session.query(Trail).all()


def print_make_selection():
    print("Please make a selection:")


def print_goodbye():
    print("Thank you for using the Marathon Manager. Happy Trails!")
