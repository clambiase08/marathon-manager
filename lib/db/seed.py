from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Runner, Trail, Workout, Run

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
    session.query(Run).delete()
    session.commit()
    print("Old Runner, Workout, Trail, and Run tables deleted successfully")

    # Initalize faker
    fake = Faker()

    print("Creating new Runner, Workout, Trail, and Run tables...")

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

    # Define the desired number of workouts
    num_workouts = 40

    # Create an empty list for Workouts
    workouts = []
    for order in range(1, num_workouts + 1):
        rand_workout_name = random.choice(workout_names)
        workout = Workout(
            name=rand_workout_name,
            type=random.choice(workout_types),
            miles_long=0 if workout_names == "flex" else random.randint(3, 10),
            order=order,
        )

        session.add(workout)
        session.commit()
        workouts.append(workout)

    # Create a list of trail locations
    def random_trail_length():
        return random.randint(3, 10)

    timberline = Trail(
        name="Timberline Trail",
        location="Mount Hood, OR",
        miles_long=random_trail_length(),
    )
    hudson = Trail(
        name="Hudson River Waterfront Walkway",
        location="New York, NY",
        miles_long=random_trail_length(),
    )
    mont_blanc = Trail(
        name="Tour du Mont Blanc",
        location="Chamonix, FR",
        miles_long=random_trail_length(),
    )
    ouachita = Trail(
        name="Lake Ouachita Vista Trail",
        location="Mountain Pine, AR",
        miles_long=random_trail_length(),
    )
    bled = Trail(
        name="Lake Bled Loop",
        location="Bled, SI",
        miles_long=random_trail_length(),
    )
    kepler = Trail(
        name="Kepler Track",
        location="Fiordland National Park, NZ",
        miles_long=random_trail_length(),
    )
    copper = Trail(
        name="Copper Ridge Loop",
        location="North Cascades National Park, WA",
        miles_long=random_trail_length(),
    )
    hk = Trail(
        name="Hong Kong Trail",
        location="Victoria Peak, HK",
        miles_long=random_trail_length(),
    )
    otter = Trail(
        name="Otter Trail",
        location="Garden Route National Park, SA",
        miles_long=random_trail_length(),
    )
    bosque = Trail(
        name="Bosque Trail",
        location="Albuguergue, NM",
        miles_long=random_trail_length(),
    )
    grand_canyon = Trail(
        name="Grand Canyon Walk",
        location="Greater Blue Mountains, AU",
        miles_long=random_trail_length(),
    )
    tahoe = Trail(
        name="Tahoe Rim Trail",
        location="Tahoe City, CA",
        miles_long=random_trail_length(),
    )
    luxembourg = Trail(
        name="Luxembourg Gardens",
        location="Paris, FR",
        miles_long=random_trail_length(),
    )
    carthew = Trail(
        name="Carthew-Alderson Trail",
        location="Waterton Lakes National Park, CA",
        miles_long=random_trail_length(),
    )
    zion = Trail(
        name="Zion Traverse",
        location="Zion National Park, UT",
        miles_long=random_trail_length(),
    )
    lagunas = Trail(
        name="Lagunas Altas Loop Trail",
        location="Patagonia Park, CL",
        miles_long=random_trail_length(),
    )
    four_pass = Trail(
        name="Four Pass Loop",
        location="Aspen, CO",
        miles_long=random_trail_length(),
    )
    potomac = Trail(
        name="Potomac River to the National Mall",
        location="Washington, D.C.",
        miles_long=random_trail_length(),
    )
    rim = Trail(
        name="Rim-to-Rim-to-Rim",
        location="Grand Canyon National Park, AZ",
        miles_long=random_trail_length(),
    )
    coastal = Trail(
        name="Coastal Trail",
        location="Marin Headlands, CA",
        miles_long=random_trail_length(),
    )
    transcarioca = Trail(
        name="Transcarioca Trail",
        location="Rio De Janerio, BR",
        miles_long=random_trail_length(),
    )
    charles = Trail(
        name="Charles River Path",
        location="Boston, MA",
        miles_long=random_trail_length(),
    )
    dinarica = Trail(
        name="Via Dinarica",
        location="Razdrto, SI",
        miles_long=random_trail_length(),
    )
    teton = Trail(
        name="Teton Crest Trail",
        location="Jackson, WY",
        miles_long=random_trail_length(),
    )
    alta = Trail(
        name="Alta Via 1",
        location="The Dolomites, IT",
        miles_long=random_trail_length(),
    )
    trails = [
        timberline,
        hudson,
        mont_blanc,
        ouachita,
        bled,
        kepler,
        copper,
        hk,
        otter,
        bosque,
        grand_canyon,
        tahoe,
        luxembourg,
        carthew,
        zion,
        lagunas,
        four_pass,
        potomac,
        rim,
        coastal,
        transcarioca,
        charles,
        dinarica,
        teton,
        alta,
    ]

    session.add_all(trails)
    session.commit()

    # Create an empty list for runners
    runners = []
    for _ in range(25):
        runner = Runner(
            name=f"{fake.name()}",
            miles_run=random.randint(0, 200),
        )
        session.add(runner)
        session.commit()
        runners.append(runner)

    # Create an empty list for runs
    runs = []
    for runner in runners:
        run_count = 0
        for _ in range(random.randint(1, 40)):
            run_count += 1
            workout = random.choice(workouts)

            suitable_trails = [
                trail for trail in trails if trail.miles_long >= workout.miles_long
            ]
            if suitable_trails:
                trail = random.choice(suitable_trails)
            else:
                None

            run = Run(
                date=fake.date_this_year(),
                runner_id=runner.id,
                workout_id=run_count,
                trail_id=trail.id if trail else None,
            )
            runs.append(run)

    session.bulk_save_objects(runs)
    session.commit()
    session.close()

    print("Finished seeding all tables. Let's Boogie!")
