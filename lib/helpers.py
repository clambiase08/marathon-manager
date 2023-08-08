from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from db.models import *

engine = create_engine("sqlite:///lib/db/marathon.db")
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


def find_runner_by_id(id):
    return session.get(Runner, id)


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


def print_workout_details(runner):
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
        if workout:
            print(
                f"Today's Workout: {workout.name} will be {workout.type} and you'll be running {workout.miles_long} miles."
            )
        else:
            print(
                "Congratulations! You are ready for the marathon. Time to carb load :)"
            )


def print_runner_info(runner):
    print(f"Runner: {runner.name} | Miles Run: {runner.miles_run} | ID: {runner.id}")


# Current Workout: {runner_workout(runner)}


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
