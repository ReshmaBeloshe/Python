# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:13:44 2018

@author: reshmb
"""

bool_one = False and False
print("bool_one = %s" % bool_one)

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5
print("bool_two = %s" % bool_two)

bool_three = 19 % 4 != 300 / 10 / 10 and False
print("bool_three = %s" % bool_three)

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2
print("bool_four = %s" % bool_four)

bool_five = True and True
print("bool_five = %s" % bool_five)

bool_six = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'
print("bool_six = %s" % bool_six)

bool_seven = True or False
print("bool_seven = %s" % bool_seven)

bool_eight = 100 ** 0.5 >= 50 or False
print("bool_eight = %s" % bool_eight)

bool_nine = True or True
print("bool_nine = %s" % bool_nine)

bool_ten = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1
print("bool_ten = %s" % bool_ten)

bool_eleven = not True
print("bool_eleven = %s" % bool_eleven)

bool_twelve = not 3 ** 4 < 4 ** 3
print("bool_twelve = %s" % bool_twelve)

bool_thirteen = not 10 % 3 <= 10 % 2
print("bool_thirteen = %s" % bool_thirteen)

bool_fourteen = not 3 ** 2 + 4 ** 2 != 5 ** 2
print("bool_fourteen = %s" % bool_fourteen)

bool_fifteen = not not False
print("bool_fifteen = %s" % bool_fifteen)

bool_sixteen = False or not True and True
print("bool_sixteen = %s" % bool_sixteen)

bool_seventeen = False and not True or True
print("bool_seventeen = %s" % bool_seventeen)

bool_eighteen = True and not (False or False)
print("bool_eighteen = %s" % bool_eighteen)

bool_nineteen = not not True or False and not True
print("bool_nineteen = %s" % bool_nineteen)

bool_twenty = False or not (True and True)
print("bool_twenty = %s" % bool_twenty)

bool_twentyone = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!
print("bool_twentyone = %s" % bool_twentyone)

bool_twentytwo = (2 <= 2) and "Alpha" != "Bravo"
print("bool_twentytwo = %s" % bool_twentytwo)

bool_twentythree = (2 >= 2) and "Alpha" == "Bravo"
print("bool_twentythree = %s" % bool_twentythree)

bool_twentyfour = (2 >= 2) and "Alpha" != "Bravo"
print("bool_twentyfour = %s" % bool_twentyfour)

bool_twentyfive = (2 <= 2) and "Alpha" != "Bravo"
print("bool_twentyfive = %s" % bool_twentyfive)
