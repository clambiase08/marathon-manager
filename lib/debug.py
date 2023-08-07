from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import *

# from db.helpers import *

if __name__ == "__main__":
    # engine = create_engine("sqlite:///marathon.db")
    # session = sessionmaker(bind=engine)()
    # print("Session Created...")

    # clear runner records from previous runs
    # session.query(Runner).delete()
    # session.commit()

    xtina = Runner(name="xtina")

    big_lakes = Trail(name="big lakes trail", location="Colorado", miles_long=100)

    sprint = Workout(name="sprint", type="fast", miles_long=5, order=1)

    set_trace()
