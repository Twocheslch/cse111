#function types:
#there are four types
#First type: built in functions: input(), len(), or int()
#second type: standard library function. Ex: import math, import random, 
#third type: third-party library function. Ex: flask?
#fourth type: user-defined functions. Ex: my_function()

#user defined function with no parameters:

def my_func():
    print("hello from my_func()")

my_func()

#function with parameters:



def my_func_with_prams(first, last):
    print(f"hello, {first} {last}")

fname = "Marty"
lname = "McFly"

my_func_with_prams(fname, lname)

#optional arguments and named arguments
#Ex: with open(filename.txt, mode = "rt") as file
#no camel case


def my_func_with_opt_params(first, last, punc="!"):
    print(f"hello {first} {last}{punc}")

my_func_with_opt_params(fname, lname)
my_func_with_opt_params(fname, lname, "?")
my_func_with_opt_params(fname, lname, "!!")

#calling a function from a module

import math

number = 25
sqrt = math.sqrt(number)

print(f"the square root of {number} is {sqrt}")

#Calling a method

name = "John"

print(type(name))
print(name.upper())

#returning a value or list form a function

def return_a_value(num1, num2):
    return num1 * num2

def return_a_list(num1, num2):
    return [num1, num2]

num1 = 3
num2 = 5

product = return_a_value(num1, num2)
print(product)

num_list = return_a_list(num1, num2)
print(num_list)

from datetime import datetime

month = datetime.now().month
print (month)


#example of bad solution:

one = "January"
two = "February"
three = "March"
four = "April"
five = "May"
six = "June"

def month_func():
    month = ["January", "Febrary", "March"]
    
    value = int(input("Please enter the month as a number: "))
    print(f"The month is {month[value-1]}")
    if value == 1:
        print(f"The month is {one}")
    elif value == 2:
        print(f"The month is {two}")
    elif value == 3:
        print(f"The month is {three}")
    elif value == 4:
        print(f"The month is {four}")
    elif value == 5:
        print(f"The month is {five}")
    elif value == 6:
        print(f"The month is {six}")
    elif value == 7:
        print(f"The month is July")
   
        
#month_func()
#def month_func():

num1 = 10.030
num2 = 10.035
precision = 0.01

if math.isclose(num1, num2, abs_tol=precision):
    print(f"{num1} and {num2} with a difference of {abs(num1 - num2):.3f} are close enough with the absolute tolerance of {precision}")
else:
    print(f"{num1} and {num2} with a difference of {abs(num1 - num2):.3f} are NOT close enough with the absolute tolerance of {precision}")
