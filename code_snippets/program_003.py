#For getting an alert at triggered time

from datetime import datetime
import pytz
import time
from tkinter import messagebox
import tkinter as tk

def alertMe(trigger_time):
    #Notifying the timezone
    tz_India = pytz.timezone('Asia/Kolkata')
    #Formatting time into string format
    datetime_India = datetime.now(tz_India).strftime("%H:%M:")
    #Formatting, string >> time >> string
    alert_time = datetime.strptime(trigger_time,"%H:%M").strftime("%H:%M:")

    if(datetime_India >= alert_time):
        root = tk.Tk()
        #For removing background window
        root.withdraw()
        messagebox.showinfo("Alert box","New Day!!!")

#Give the time here
time = "00:00"
alertMe(time)
