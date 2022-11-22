import win32com.client as client

date = input("what is todays date")
shift_start = input("What time did your shift start?")
Logon =  input ("What time did you log on?")
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
message.To = "someone@example.com" #replace someone@example.com with where you would like to send the email here
message.subject = f"Punch in {date} "
message.Body = f"1. Time your shift starts: {shift_start}  \n2.Time you logged in: {Logon} "
