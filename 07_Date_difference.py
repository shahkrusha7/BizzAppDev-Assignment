"""
Date Difference Calculator (Real-World Scenario)

Problem:
Calculate the number of days between two user-provided dates (e.g. birthdate and today's date).

Approach:
1. Accept two dates in dd-mm-yyyy format.
2. Convert the strings into date objects.
3. Subtract the dates and print the number of days between them.
"""

from datetime import datetime

def date_difference(start_date,end_date):
    format="%d-%m-%Y"
    d1=datetime.strptime(start_date,format)
    d2=datetime.strptime(end_date,format)
    diff=abs((d2-d1).days)
    return diff

birthdate=input("Enter your birthdate (dd-mm-yyyy): ")
today=input("Enter today's date (dd-mm-yyyy): ")

days_lived=date_difference(birthdate,today)
print(f"You have lived {days_lived} days.")
