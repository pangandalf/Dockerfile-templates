import os
import datetime

print("Current dir is: ", os.getcwd())

for entry in os.listdir('.'):
    print(entry)

print("Date: ", datetime.datetime.now())
