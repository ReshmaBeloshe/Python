# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:49:00 2018

@author: reshmb
"""

for i in range (1,11):
    j= 29*i
    print(" 29 X %s = %s" %( i , j)  )
    
num = int(input("Please enter a number for multiplication table: "))

for i in range (1,11):
    j= num*i
    print(" %s X %s = %s" %( num, i , j )  )

n = int(input("Please enter a number for multiplication table: "))

for i in range (1,11):
    print (n, 'x', i, '=', n*i )

#****** Assignment 2 *****
N = int(input("Please enter a number number pyramid: "))

x = 1
for i in range (0,N):
    for j in range (0,N-i):
        print(end="\t")
    for j in range (0,i+1): 
        print(x,end="\t")
        print(end="\t")
        x = x+1
    print("\n\n")
    print()
    
#****** Assignment 2 *****

x = "HELLO"
print (x[0])
print (len(x))



text = input("Please enter a word for pyramid: ")
length = len(text)


for i in range (0,length):
   for j in range (0,length-i):
        print(end=" ")
   for j in range (0,i+1): 
        print(text[j],end=" ")
   print()
    


for i in range (0,length):
   for j in range (0,i + 1):
        print(end=" ")
   for j in range (0,length - i): 
        print(text[j],end=" ")
   print()
     

#****** Assignment 3 *****
     
text = "ABCDEFG"
length = len(text)

for i in range (0,length):
   for j in range (0,length - i): 
        print(text[j],end=" ")
   for j in range (0, 2*i -1):
        print(end="  ")
   if(i<1) :
       for j in range (0,length - i-1): 
           y =  length - j - 2 - i
           print(text[y],end=" ")
   else :
       for j in range (0,length - i): 
           y =  length - j - 1 - i
           print(text[y],end=" ")
   print()
