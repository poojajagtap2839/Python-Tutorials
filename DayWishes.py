# time is built in module in python

import time
fullTime=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
name=input("Enter your good name: ").title()

if(hour>5 and hour<12):
    print("Hello, very Good Morning ",name)
elif(hour>12 and hour<17):
    print("Hello, very Good Afternoon ", name)
else:
    print("Hello, very Good Evening ", name)

