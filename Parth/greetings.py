import datetime,time
from speak import speak

def Greeting(name):
       Hour = int(datetime.datetime.now().hour)
       a = time.strftime('%I:%M %p')
       if Hour >= 0 and Hour < 12:
           speak(f'Good Morning mister {name} ! it is {a} \n')
       elif Hour >= 12 and Hour < 18:
           speak(f'Good Afternoon mister {name}! it is {a} \n')
       else:
           speak(f'Good Evening mister {name}! it is {a} \n')
       speak('How may I help')