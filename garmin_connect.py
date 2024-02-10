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

    garmin_step=pd.DataFrame(garth.DailySteps.list(date.today() - timedelta(days=1)))
    steps_bmr=(garmin_step['total_steps'])
    return (steps_bmr[0])

