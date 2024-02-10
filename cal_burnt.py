class cal_burnt_class:
  def __init__(self):
    pass
  def calculate_bmr(self,height=66,weight=135,age=26,sex='female'):
    if sex == "male":
        cal = 660 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        cal = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return cal
  def calculate_daily_calories(self,basic_cal,step):
    if step<=5000:
        calories = basic_cal * 1.2
    elif step<=7500:
        calories = basic_cal * 1.375
    elif step<=10000:
        calories = basic_cal * 1.55
    else:
        calories = basic_cal * 1.725
    return calories