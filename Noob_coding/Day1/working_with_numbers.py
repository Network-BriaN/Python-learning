#!/usr/bin/python

print(9-14.787)     #basic maths in print statement
print(3*(4+5))      #even complex equations
print(10 % 3)       #return remainder

my_num = -5
print(my_num+5)

#print(my_num + " is the worst")                #error cant concate num and string
print(str(my_num))                              #numbers inside a string
print(str(my_num) + " is the worst number")     #now we can concate num and string

print(abs(my_num))          #absolute value
print(pow(2,128))           #first number raised to second 2^128
print(max(4,6,10,999))      #returns highest value after comparison
print(min(4,6,10,999))      #returns lowest value after comparison
print(round(4.6))           #number closest

from math import *          #math module gives additional math functions
print(floor(3.3))           #returns lowest integer
print(ceil(3.01))           #returns highest integer
print(sqrt(9))              #square root
