
import tkinter
from tkinter import *
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from datetime import date, timedelta
from datetime import timedelta
from garmin_connect import garmin_connect_class
from cal_burnt import cal_burnt_class
from cal_intake import cal_intake_class


burnt=cal_burnt_class()
intake=cal_intake_class()
connect=garmin_connect_class()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Good Loss")
    root.state('zoomed')

    root.geometry('340x440')
    root.configure(bg='#9d8189')

    def get_value():
        email_=email.get()
        password_=password.get()
        breakfast_=breakfast.get()
        brunch_=brunch.get()
        lunch_=lunch.get()
        snack_=snack.get()
        bmr = burnt.calculate_bmr()
        step=connect.get_steps(email_,password_)
        calories_burnt = burnt.calculate_daily_calories(bmr,step[0])
        calories_ate=(intake.find_food(breakfast_))
        df=step[1]
        
        try:
            calories_ate+=intake.find_food(brunch_)
        except:
            pass
        try:
            calories_ate+=intake.find_food(lunch_)
        except:
            pass
        try:
            calories_ate+=intake.find_food(snack_)
        except:
            pass
        
        print("You have "+ str(calories_burnt-calories_ate)+" calories burning for you!.")
        label1=tkinter.Label(frame, text=f"You have {step[0]} steps working for you!.",bg='#9d8189')
        
        label2=tkinter.Label(frame, text=f"You have eaten {calories_ate} calories!.",bg='#9d8189')
        
        label3=tkinter.Label(frame, text=f"You have {calories_burnt-calories_ate} calories burning for you!.",bg='#9d8189')

        label1.grid(row=6, column=1, columnspan=2, sticky="news")
        label2.grid(row=7, column=1, columnspan=2, sticky="news")
        label3.grid(row=8, column=1, columnspan=2, sticky="news")
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=df["calendar_date"], y=df["total_steps"])
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        plt.xticks(rotation=45)
        plt.xlabel(None)
        plt.ylabel(None)
        plt.title("Daily Steps")
        plt.show()

    frame = tkinter.Frame(bg='#9d8189')
 
        

    project_label = tkinter.Label(
    frame, text="Good Loss", bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    user_email = tkinter.Label(frame, 
                      text = "Email:",bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    password_label = tkinter.Label(frame, 
                      text = "Password:",bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    breakfast_label = tkinter.Label(frame, 
                      text = "breakfast:",bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    brunch_label = tkinter.Label(frame, 
                      text = "brunch:",bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    lunch_label = tkinter.Label(frame, 
                      text = "lunch:",bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    snack_label = tkinter.Label(frame, 
                      text = "snack:",bg='#9d8189', fg="#d4a373", font=("Arial", 30))
    email = tkinter.Entry(frame,font=("Arial", 16)) 
    password = tkinter.Entry(frame, show="*",font=("Arial", 16)) 
    breakfast = tkinter.Entry(frame,font=("Arial", 16)) 
    brunch = tkinter.Entry(frame,font=("Arial", 16)) 
    lunch = tkinter.Entry(frame,font=("Arial", 16)) 
    snack = tkinter.Entry(frame,font=("Arial", 16))


    
    b1 = tkinter.Button(frame, text = 'Final Deficit', bg="#d4a373", fg="#03071e", font=("Arial", 16),command=get_value)

    project_label.grid(row=0, column=1, columnspan=1, sticky="news", pady=40)
    user_email.grid(row=1, column=0)
    email.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password.grid(row=2, column=1, pady=20)
    breakfast_label.grid(row=3, column=0)
    breakfast.grid(row=3, column=1, pady=20)
    brunch_label.grid(row=3, column=3,pady=20)
    brunch.grid(row=3, column=4, pady=20)
    lunch_label.grid(row=4, column=0)
    lunch.grid(row=4, column=1, pady=20)
    snack_label.grid(row=4, column=3,pady=20)
    snack.grid(row=4, column=4, pady=20)
    b1.grid(row=5, column=0, columnspan=2, pady=30)

    frame.pack()
    root.mainloop()