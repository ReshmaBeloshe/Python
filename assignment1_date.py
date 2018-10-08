# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:36:40 2018

@author: reshmb
"""
from datetime import date
date1=date.today();
print(date1.strftime("%d-%m-%y"));
#from datetime import date
year = int(input("Enter a year \n"))
month = int(input("Enter a month \n"))
day = int(input("Enter a day \n"))
DOB = date(year, month, day)

print(DOB.strftime("The Date of Birth=%d/%m/%y"))

Years = date1.year-DOB.year;
Months = date1.month-DOB.month;
Days = date1.day-DOB.day;



print("Age is = %s %s %s" % (Years,Months,Days))
#print(a)




import datetime

from datetime import date
today=date.today()

year = int(input('Enter a birth year '))
month = int(input('Enter a birth month '))
day = int(input('Enter a birth day '))
dob = datetime.date(year, month, day)

age = today - dob

print(" \n Todays date is " )
print(today)

print(" \n date of birth is " )
print(dob)

print(" \n Age is " )
print(age)  # in days

# ********* problem 2 *********

print ("Twinkle, twinkle, little star \n \t How I wonder what you are ! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky.")

# ********* problem 3 *********
 
r = float(input("Please enter Radius of a cone: "))
h = float(input("Please enter height of a cone: "))

import math

slant_h = math.sqrt(r * r + h * h)
area = 3.14 * r * r + 3.14 * r * slant_h

volume = 1/3 * 3.14 * r * r * h

print(" Area of a cone is " )
print (area)

print(" Volume of a cone is " )
print (volume)



r = float(input("Please enter Radius of a cone: "))
h = float(input("Please enter height of a cone: "))

import math

slant_h = math.sqrt(r * r + h * h)
area = math.pi * r * r + math.pi * r * slant_h

area = math.pi * r**2 + math.pi * r * slant_h

volume = 1/3 * math.pi * r * r * h

print(" Area of a cone is %s " % area)

print(" Volume of a cone is %s " % volume)