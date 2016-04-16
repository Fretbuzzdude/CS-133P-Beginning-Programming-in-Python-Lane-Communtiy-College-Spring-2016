#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Name:   
# Class:	CS 133P: Beginning Programming in Python
# School:	Lane Community College
# Term:		Spring 2016
# Book:		How To Think Like A Computer Scientist
# What:		Week/Lab 3, Chapters 7 (Functions) and 8 (Selection)
# Created:	04/16/2016
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 6 (Functions)-Exercise 7 

# Write a fruitful function sumTo(n) that returns the
# sum of all integer numbers up to and including n. So sumTo(10) would be
# 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.

# define a function
def sumTo(n):
    """Sum from 0 to given numbers"""
    sum = int((n * (n + 1)) / 2)
    return sum
# end of function

# Says what we are going to solve
print("Finally, let's calculate the sum of the integers from 0 to the given number. Follow the directions.\n")
# the formula applied to the variables
sum_this = int(input("Enter a number: "))
# the answer output
print("The sum of the integers from 0 to",sum_this,"is",sumTo(sum_this),".\n")

#---To check your work ----------------------------------------------------
# If we enter a number: 4
# The sum of the integers from 0 to 4 is 10
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-Chapter 6 (Functions)-Exercise 8

# Write a function areaOfCircle(r) which returns the area of a circle of radius 
# r. Make sure you use the math module in your solution.

import math
# define a function
def areaOfCircle(r):
    """Compute the area of a circle of radius r"""
    area = round(math.pi * r**2, 2)
    return area
# end of function

# Says what we are going to solve
print("Next, we can calculate the area of a circle of a given radius. Follow the directions.\n")
# asks the user to input of variable
radius = float(input("Enter the radius of a circle: "))
# the answer output
print("The area of a circle of radius",radius,"is about",areaOfCircle(radius),"square units.\n")

#---To check your work-----------------------------------------------------
# Enter the radius of a circle: 3
# The area of a circle of radius 3 is about 28.27 square units.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-Question#1

# Write a function that calculates the area of a rectangle.  The function should
# take 2 parameters, length and width.  The function should return the area.  Use
# your function in a program that asks the user to enter the length and width and 
# then displays the area of the rectangle on the screen.

# Says what we are going to solve
print("Next it will calculate the area of a rectangle, given a length and width.")
# asks the user to input of variable
length = float(input("Enter the length of the rectangle: "))
# asks the user to input of variable
width = float(input("Enter the width of the rectangle: "))
# the formula applied to the variables
area = length*width
# the answer output
print("The area of a rectangle of length",length,"units and width",width,"units is",area,"square units.\n")

#---To check your work-----------------------------------------------------
# >>>Next it will calculate the area of a rectangle, given a length and width.
# >>>Enter the length of the rectangle: 20 [<-user input]
# >>>Enter the width of the rectangle: 10 [<-user input]
# >>>The area of a rectangle of length 20.0 units and width 10.0 units is 200.0 square units.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-Question#2

# Write a function that calculates the miles per gallon used by an automobile.  
# The function should take 2 parameters, miles driven and gallons used.  The 
# function should return mpg.  Use your function in a program that asks the user 
# to enter the miles and gallons and then displays the mpg on the screen.

# Says what we are going to solve
print("Now, let's calculate MPG given miles driven and gallons consumed.")
# asks the user to input of variable
distance = float(input("Enter the distance driven: "))
# asks the user to input of variable
gas = float(input("Now enter the number of gallons consumed: "))
# the formula applied to the variables
mpg = round((distance/gas), 2)
# the answer output
print("If you drove",distance,"on",gas,", you are getting about",mpg,"mpg.\n")

#---To check your work-----------------------------------------------------
# if you enter the distance driven: 33
# and then enter the number of gallons consumed: 2 
# your answer if you drove 33miles on 2 gal , you are getting about 16.5 mpg.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-Question#3

# Write a function that converts celsius temperature to fahrenheit.  The function
# should take 1 parameter, a celsius temperature.  The function should return the
# equivalent fahrenheit temperature.  Use your function in a program that asks the
# user to enter the celsius temperature and displays the fahrenheit temperature on
# the screen.

# Says what we are going to solve
print("Lets convert from Celsius to Fahrenheit.")
# asks the user to input fahrenheit temp.
degc = float(input("Enter the temperature in degrees Celsius: "))
# formula applied to the users input
degf = round((degc*9/5) + 32, 2)
# printing the answer to the problem
print(degc,"degrees Celsius is about",degf,"degrees in Fahrenheit.\n")

#---To check your work-----------------------------------------------------
# If I entered: The temperature in degrees Celsius: 0
# 0.0 degrees in Celsius is about 32.0 degrees in Fahrenheit.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-Question#4

# Write a function that converts fahrenheit temperature to celsius.  The function
# should take 1 parameter, a fahrenheit temperature.  The function should return 
# the equivalent celsius temperature.  Use your function in a program that asks 
# the user to enter the fahrenheit temperature and displays the celsius temperature
# on the screen.

# Says what we are going to solve
print("Now let's convert a temperature in Fahrenheit to Celsius.")
# asks the user to input fahrenheit temp.
degf = float(input("Enter the temperature in degrees Fahrenheit: "))
# formula applied to the users input
degc = round((degf-32)*5/9, 2)
# printing the answer to the problem
print(degf,"degrees in Fahrenheit is about",degc,"degrees in Celsius.\n")

#---To check your work-----------------------------------------------------
# If I entered: The temperature in degrees Fahrenheit: 32
# 32.0 degrees in Fahrenheit is about 0.0 degrees in Celsius.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 7 (Selection)-Exercise 3

# Write a function which is given an exam mark, and it returns a string — the 
# grade for that mark — according to this scheme:
# Mark 	Grade
# >= 90 	A
# [80-90) 	B
# [70-80) 	C
# [60-70) 	D
# < 60 	F
# The square and round brackets denote closed and open intervals. A closed 
# interval includes the number, and open interval excludes it. So 79.99999 
# gets grade C , but 80 gets grade B.
# Test your function by printing the mark and the grade for a number of different
# marks.

# Function to convert mark to grade
def grade(mark):
    if mark >= 90:
        return "A"
    else:
        if mark >= 80:
            return "B"
        else:
            if mark >= 70:
                return "C"
            else:
                if mark >= 60:
                    return "D"
                else:
                    return "F"
# end of function

# ask user for mark number
mark = int(input("Enter the grade mark number and I will convert it to a letter grade"))
# print answer
print( "Mark:", str(mark), "Grade:", grade(mark))

# You will be asked to enter a grade mark integer.
# As a check, if you enter '79', your Grade will equal a 'C'
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 7 (Selection)-Exercise 6

# Write a function findHypot. The function will be given the length of two sides 
# of a right-angled triangle and it should return the length of the hypotenuse.
# (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math

# Function to square the numbers
def findHypot(length):
    square = length * length
    print ("The square of a side is: ", square)
    return square
# end of function

# Function to calculate Pythagorean theorem
def pythagorean(aside, bside):
    HypotenuseSquared  = aside + bside
    hypotenuse = math.sqrt(HypotenuseSquared)
    print("The hypotenuse of the 2 sides is: ", hypotenuse)
# end of function

# Get the length of the sides from the user and hold
firstside = float(input("Enter the first side: "))
secondside = float(input("Enter the second side: "))

# Get the squares of 2 sides and print them
firstsidesquared = findHypot(firstside)
secondsidesquared = findHypot(secondside)
print("The firstside variable is: ", firstside)
print("The secondside variable is: ", secondside)

# Put the squares into the Pythagorean function
pythagorean(firstsidesquared, secondsidesquared)

#This exercise took me about 2 hours to figure out. I went over and over and 
# over and over it. Finally I got it all to work. I am quite sure there is an
# easier way to do this!
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 7 (Selection)-Exercise 7
# Write a function called is_even(n) that takes an integer as an argument and 
# returns True if the argument is an even number and False if it is odd.

# Function to divide by 2
def isEven(n):
  if (n%2 == 0):
     return True
  else:
     return False
# end of function

# ask user for the n 
n = int(input("Enter n number and I will tell you TRUE if it's even and FALSE if it's odd"))
# answer printed
print( "number entered:", str(n), "Is it even?:", isEven(n))

# I created a function to divide a number by 2. If the output left no remainder, 
# then the return would be true. If there was a remainder, then the return would
# be false.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 7 (Selection)-Exercise 8
# Now write the function is_odd(n) that returns True when n is odd and False
# otherwise.

# Function to divide by 2
def is_odd(n):
  if (n%2 == 0):
     return False
  else:
     return True
# end of function

# ask user for input of n
n = int(input("Enter n number and I will tell you FALSE if it's even and TRUE if it's odd"))
# answer printed
print( "number entered:", str(n), "Is it odd?:", is_odd(n))

# This is just a copy of exercise 7, but with True and false flipped and the
# function renamed.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 7 (Selection)-Exercise 10
# Write a function is_rightangled which, given the length of three sides of a
# triangle, will determine whether the triangle is right-angled. Assume that the
# third argument to the function is always the longest side. It will return True
# if the triangle is right-angled, or False otherwise.

#Hint: floating point arithmetic is not always exactly accurate, so it is not 
# safe to test floating point numbers for equality. If a good programmer wants
# to know whether x is equal or close enough to y, they would probably code it 
# up as:

# Create the function
def is_somewhat_right_angled(a, b, c):
    a, b, c = sorted([a, b, c])
    return abs(a * a + b * b - c * c) < 0.0001
# end of function

# get the user input
a = int(input("enter side a, side c will be the longest side: "))
b = int(input("enter side b, side c will be the longest side: "))
c = float(input("enter side c, side c will be the longest side: "))   
# use floating point for decimal

# Put the sides into the function
print (is_somewhat_right_angled(a, b, c))

# If I entered:
#       Side a= 3
#       Side b= 3
#       Side c= 4.24264069
# then the answer should be TRUE.

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Lab3-chapter 7 (Selection)-Exercise 12
# Extend the above program so that the sides can be given to the function in any
# order.


# Create the function
def is_somewhat_right_angled(a, b, c):
    a, b, c = sorted([a, b, c])
#    return abs(a * a + b * b - c * c) < 0.001

#adding function so long side can be a, b, or c. replace the above line with below.
    if a > b and a > c:
        is_somewhat_right_angled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_somewhat_right_angled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_somewhat_right_angled = abs(a**2 + b**2 - c**2) < 0.001
    return is_somewhat_right_angled
# end of function

# get the user input
a = float(input("enter side a: "))
b = float(input("enter side b: "))
c = float(input("enter side c: "))   #use floating point for decimal

# Put the sides into the function 
print (is_somewhat_right_angled(a, b, c))

# If I entered:
#       Side a= 4.24264069
#       Side b= 3
#       Side c= 3
# then the answer should be TRUE.
