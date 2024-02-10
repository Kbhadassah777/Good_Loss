
import tkinter
from tkinter import messagebox
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
    root.configure(bg='#ccd5ae')

    def get_value():
        email_=email.get()
        password_=password.get()
        breakfast_=breakfast.get()
        brunch_=brunch.get()
        lunch_=lunch.get()
        snack_=snack.get()
        bmr = burnt.calculate_bmr()
        step=connect.get_steps(email_,password_)
        calories_burnt = burnt.calculate_daily_calories(bmr,step)
        calories_ate=(intake.find_food(breakfast_))
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
        label1=tkinter.Label(frame, text=f"You have {step} steps working for you!.")
        
        label2=tkinter.Label(frame, text=f"You have {calories_ate} calories working against you!.")
        
        label3=tkinter.Label(frame, text=f"You have {calories_burnt-calories_ate} calories burning for you!.")

        label1.grid(row=6, column=0, columnspan=2, sticky="news")
        label2.grid(row=7, column=0, columnspan=2, sticky="news")
        label3.grid(row=8, column=0, columnspan=2, sticky="news")
        df = pd.DataFrame({'val':[calories_burnt, calories_ate], 'columns':['out', 'in']})
        fig1 = df.plot.bar(x='val', y='columns', rot=0)
        canvas1 = FigureCanvasTkAgg(fig1, frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    frame = tkinter.Frame(bg='#ccd5ae')


    project_label = tkinter.Label(
    frame, text="Good Loss", bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    user_email = tkinter.Label(frame, 
                      text = "Email:",bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    password_label = tkinter.Label(frame, 
                      text = "Password:",bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    breakfast_label = tkinter.Label(frame, 
                      text = "breakfast:",bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    brunch_label = tkinter.Label(frame, 
                      text = "brunch:",bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    lunch_label = tkinter.Label(frame, 
                      text = "lunch:",bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    snack_label = tkinter.Label(frame, 
                      text = "snack:",bg='#ccd5ae', fg="#d4a373", font=("Arial", 30))
    email = tkinter.Entry(frame,font=("Arial", 16)) 
    password = tkinter.Entry(frame, show="*",font=("Arial", 16)) 
    breakfast = tkinter.Entry(frame,font=("Arial", 16)) 
    brunch = tkinter.Entry(frame,font=("Arial", 16)) 
    lunch = tkinter.Entry(frame,font=("Arial", 16)) 
    snack = tkinter.Entry(frame,font=("Arial", 16))


    
    b1 = tkinter.Button(frame, text = 'Final Deficit', bg="#d4a373", fg="#03071e", font=("Arial", 16),command=get_value)

    project_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
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