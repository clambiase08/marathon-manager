from ipdb import set_trace
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from db.models import *

# from db.helpers import *

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/marathon.db")
    session = sessionmaker(bind=engine)()
    print("Session Created...")

    # xtina = Runner(name="xtina")

    # big_lakes = Trail(name="big lakes trail", location="Colorado", miles_long=100)

    # sprint = Workout(name="sprint", type="fast", miles_long=5, order=1)

    runner_miles = (
        session.query(func.sum(Workout.miles_long))
        .join(Run)
        .filter(Run.runner_id == 4)
        .scalar()
    )

    set_trace()
