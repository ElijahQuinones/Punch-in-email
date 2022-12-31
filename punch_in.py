import win32com.client as client
from datetime import datetime

today = datetime.now()
date = today.strftime('%m-%d-%Y')

if today.strftime("%A") == "Saturday":
    shift_start = "5pm"
elif today.strftime("%A") == "Sunday":
    shift_start = "12pm"
Logon =  today.strftime("%I:%M")
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
message.To = "someone@example.com" #replace someone@example.com with where you would like to send the email here
message.subject = f"Punch in {date} "
message.Body = f"1. Time your shift starts: {shift_start}  \n2.Time you logged in: {Logon}"
