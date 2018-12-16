# allows us to do more math functions
from math import *
# Working with numbers in Python : one of the most common data types
# Modulus : divide the numbers and spit out the remainder
# my_num = -5
# When you want to print numbers alongside strings
# print(str(my_num) + " is my favorite number")
# function collection of code that does something and we can get info from
# my_num = -5
# absolute value
# print(abs(my_num))
# taking numbers to specific powers
# print(pow(2,12))
# print(max(4,9))
# print(min(3,3.8))

# print(round(3.147489))
# print(floor(3.8))
# print(ceil(4.532))
# print(sqrt(2))

# How to get input from a user, allow user to input info into our program, take that info, store it & do something in
# that variable
# Tells python we want input from user, and python will allow user to type in info
# Have to tell user what we want them to enter
# Taking value user inputs and store it in variable called 'name'
# Getting info from user makes your program more interactive
# name = input("Enter your name:")
# age = input("Enter your age:")
# print("Hello " + name + " You are " + age)

# Getting numbers and inputs from users : Calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# Int: Integer is a whole number, no decimal points; its looking for whole numbers, so using decimal numbers will cause
# error, can also use float for decimal numbers
result = float(num1) + float(num2)
print(result)
# Not quite the answer we're looking for, Python converts it to a string by default. To make them numbers, we have to
# convert the strings from the user into numbers





