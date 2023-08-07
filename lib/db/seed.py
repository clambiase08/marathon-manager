from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Runner, Trail, Workout

if __name__ == "__main__":
    print("Starting seeding...")
    engine = create_engine("sqlite:///marathon.db")
    session = sessionmaker(bind=engine)()
    print("Session created...")

    # clear records from previous runs
    print("Clearing previous records...")
    session.query(Runner).delete()
    session.query(Trail).delete()
    session.query(Workout).delete()
    session.commit()
    print("Old Runner, Workout, and Trail tables deleted successfully")

    # Initalize faker
    fake = Faker()

    print("Creating new Runner, Workout, and Trail tables...")

    # Create a list of workout names
    workout_names = [
        "flex",
        "reg run",
        "easy run",
        "as you feel",
        "fartlek",
        "intervals",
        "tempo run",
        "long run",
    ]

    # Create a list of workout types
    workout_types = ["easy", "medium", "hard"]

    # Create an empty list for runners
    runners = []
    for _ in range(20):
        runner = Runner(
            name=f"{fake.first_name()} {fake.last_name()}",
            miles_run=random.randint(0, 200),
        )
    session.add(runner)
    session.commit()
    runners.append(runner)

    # Create an empty list for Workouts
    # workouts = []

    # for runner in runners:
    #     for _ in range(20):
