# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:21:46 2018

@author: reshmb
"""

# Problem 1.	Write a Python function to sum all the items in a list (Consider the items of integer type).


def Sum_List(lst) :
    total = 0
    for i in lst:
        total += i
    print("Sum = ", total)
    
print ("Please enter items in List ")

lst1 = [int(x) for x in input().split()]

Sum_List(lst1)
    


# Problem 2.	Write a Python function that takes two lists and returns True if they have at least one common member.

def CompareLists( list1, list2) :
    hasCommonItem = False
    for i in lst1:
        for j in lst2:
           
            if j == i:
               hasCommonItem = True
               print("There is a Common member in 2 lists and the number is ", i )
               break
        if hasCommonItem :
            break

    if hasCommonItem == False :
        print("There is no Common member in 2 lists")
         
     
print ("Please enter items in List1 ")

lst1 = [int(x) for x in input().split()]

print ("Please enter items in List2 ")

lst2 = [int(x) for x in input().split()]

CompareLists( lst1, lst2) 

# Problem 3.	Write a Python function to check whether an element exists within a tuple.

def Check_Element( tpl, element) :
    num = False
    for i in tpl:
        if i == element:
            num = True
            print("The element exists in the tuple")
            break
        else:
            continue
    if num == False :
        print("The element does not exist in the tuple")
                         
     
print ("Please enter items in tuple ")

lst1 = (x for x in input().split())

tpl1 = tuple(lst1)

elementToCheck = int(input("Please enter a number to check in tuple "))

Check_Element( tpl1, elementToCheck)


# Problem 4.	Write a Python program to reverse a tuple.

#list 
tpl1 = (10,20,30,40,50)
lstToReverse = []

for item in range(len(tpl1)-1 ,-1,-1):
    lstToReverse.append(tpl1[item])

print(lstToReverse)    

#lst1 = list(tpl1)

length = len(lst1)

lst2 = [1,2,3,4,5]

for i in range (0,length) :
    x = length - i -1
    lst2[i] = lst1[x]

tpl2 = tuple(lst2)

print ("Reversed tuple is ")
print(tpl2)

#Tuple

tpl1 = (10,20,30,40)

tpl2 = reversed(tpl1)

print(tuple(tpl1))
print(tuple(tpl2))



# Problem 5.	Write a Python program to get the maximum and minimum value in a dictionary. 
print("Please enter items for the dictionary: ")
lst5 =[int(x) for x in input().split()]
d = {}
for i in range(0,len(lst5)):   
    d[i]=lst5[i]
    
dictn = {1:45,2:25,3:58,4:258}

Max = dictn[1]
Min = dictn[1]

for i in dictn.values():
        if i > Max :
            Max = i
        if i < Min :
            Min = i

print("\nMaximum value = ", Max, "\nMinimum value = ", Min )
 
    
    
    
    