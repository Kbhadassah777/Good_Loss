import garth
import pandas as pd
from datetime import date, timedelta
GARTH_HOME = "Desktop/calorie_tracker/garth"

from garth.exc import GarthException
from getpass import getpass

class garmin_connect_class:
  def __init__(self):
     pass
  def get_steps(self,email,password):
    try:
          garth.resume(GARTH_HOME)
          garth.client.username
    except (FileNotFoundError, GarthException):

      email = input("Email: ")
      password = getpass("Password: ")
      garth.client.login(email,password)

    garth.save(GARTH_HOME)
    Daily_steps = garth.DailySteps.list(period=28)
    df = pd.DataFrame(Daily_steps).sort_values("calendar_date")

    
    
    year = 365 * 3
    steps_year=pd.DataFrame(garth.DailySteps.list(period=year))
    steps_year.set_index("calendar_date", inplace=True)
    steps_year.rename(columns={"value": "steps"}, inplace=True)
    garmin_step=pd.DataFrame(garth.DailySteps.list(date.today() - timedelta(days=1)))
    steps_bmr=(garmin_step['total_steps'])
    return ([steps_bmr[0],df])
