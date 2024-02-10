import requests
import json

class cal_intake_class:
  def __init__(self):
    pass
  def find_food(self,query):
    api_url='https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response=requests.get(api_url,headers={'X-Api-Key':'25onGufWLthhgV53EA6jAw==9jEm3CfuKTZX1BD7'})
    food_fetched=json.loads(response.text)
    if food_fetched:
      calorie_ate=(food_fetched[0]['calories'])
      return calorie_ate
      