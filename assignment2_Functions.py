# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:37:27 2018

@author: reshmb
"""




def GradeCalc(marks):
    if marks >= 90 :
        print("Passed with Grade A")
    elif (marks < 90 and marks >= 80) :  # 90 > marks >= 80 is also right
        print("Passed with Grade B")
    elif (marks < 80 and marks >= 70) :
        print("Passed with Grade C")
    elif (marks < 70 and marks >= 65) :
        print("Passed with Grade D")
    else :
        print("Failed")
    
M1 = int(input('Enter the marks '))
GradeCalc(M1)

GradeCalc(85)


*********** Assignment problem 2 *********

from datetime import date
today=date.today()

#year = int(input('Enter a birth year '))
#month = int(input('Enter a birth month '))
#day = int(input('Enter a birth day '))
#dobirth = date(year, month, day)

#print(" \n date of birth is %s" %dobirth)

print(" \n Todays date is %s" %today)

def AgeCalc (dob) :
    age_y = today.year - dob.year
    
    age_m = today.month - dob.month
    
    age_d = today.day - dob.day
    
    if (today.month < dob.month or (today.month == dob.month and today.day < dob.day)):
        age_y -= 1
        age_m = 12 + age_m
        
    if (today.month <= dob.month and today.day < dob.day):
        age_m -= 1
    
    if(today.day < dob.day):
        age_d = 30 + age_d
        
    print(" \n Age is %s years, %s months and %s days" %(age_y , age_m , age_d))
    
#AgeCalc(dobirth)

AgeCalc(date(1982,2,18))

AgeCalc(date(1989,11,14))

AgeCalc(date(1990,8,14))

AgeCalc(date(1990,8,22))

************* Assignment problem 3 **************
import math


def CalcArea(r,h):
    slant_h = math.sqrt(r * r + h * h)
    area = math.pi * r**2 + math.pi * r * slant_h
    print(" Area of a cone is %s " % area)
    
def CalcVolume(r,h): 
    volume = 1/3 * math.pi * r * r * h
    print(" Volume of a cone is %s " % volume)
    
CalcArea(2,8)    
CalcVolume(2,8)   