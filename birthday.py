"""
birthday.py
Author: Adam Pikielny
Credit: I read the readme
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
monthname = month_name[todaymonth]
print (monthname)
print (todaydate)

name=input("Hello, what is your name? ")
month=input("Hi " + name + ", what was the name of the month you were born in? ")
year=int(input("And what year were you born in, " + name + "? "))
day=input("And the day? ")
if (monthname=="December" or monthname=="January" or monthname=="February"):
    season="winter"
elif (monthname=="March" or monthname=="April" or monthname=="May"):
    season="spring"
elif (monthname=="June" or monthname=="July" or monthname=="August"):
    season="summer"
elif (monthname=="September" or monthname=="October" or monthname=="November"):
    season="fall"
    
if (year>=2000):
    yeartype="two thousands"
elif (year>=1990):
    yeartype="nineties"
elif (year>=1980):
    yeartype="eighties"
else:
    yeartype="stone age"

if (month=="October" and day=="31"):
    print("You were born on Halloween!")
elif (month == monthname and int(day) == todaydate):
    print("Happy birthday!")

print (name+", you are a "+season+" baby of the " + yeartype +".")
