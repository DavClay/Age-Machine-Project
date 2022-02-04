#Mostly By DavClay on Github
print("Please use number form such as 2/4/2022")
month = input("What month were you born in ")
print("Thank you")
day = input("What day were you born on ")
print("Thanks")
year = input("What year were you born in ")
month = int(month)
day = int(day)
year = int(year)
#Code from https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/ thanks
from datetime import date
todays_date = date.today()
#Math to caculate how old somebody is (\created by me
age = todays_date.year - year
if month - todays_date.month > 0:
    age -= 1
if month == todays_date.month and todays_date.day - day < 0:
    age -= 1
print(age)
