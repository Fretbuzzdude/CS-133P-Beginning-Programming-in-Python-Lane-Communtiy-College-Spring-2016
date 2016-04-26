#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Name:   Janis
# Class:	CS 133P: Beginning Programming in Python
# School:	Lane Community College
# Term:		Spring 2016
# Book:		How To Think Like A Computer Scientist
# What:		Week/Lab 4, Chapters 7 (Functions) and 8 (Selection)
# Created:	04/25/2016
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


# Question 1
  """"chapter 7 review - calculatePay.  Write a function called calculatePay.  The 
 function should take 2 parameters, the hours worked and the pay rate.  It should
 calculate the total pay, including overtime if the user worked more than 40 
 hours.  Overtime is calculated at 1.5 * pay rate.  Test your function with at 
 least 2 values.  THEN write a program that asks the user to enter both hours 
 worked and pay rate.  The program should use your function to calculate the 
 total pay for the user and then should display that value to the screen.""""

#Problem
##calculate the total pay, including overtime if the user worked more than 40 hours.


#creating the function
def calculatePay(h, r):
# if-else required
        if h <=40:
            return h * r
        else:
            return 40 * r + ((h-40) * (r*1.5))

# User Input			
hours = int(input('Enter hours worked: '))
wage = int(input('Enter dollars paid per hour: '))
total = calculatePay(hours, wage)

# The calculated output
print ("Your gross pay would be $", total)

# Notes about this problem are being typed here and I feel good about that.

#________________________________________________________________________

#Or you could do it this way:

'''if-else example:  calculate weekly wages -- alternate version'''

def calculatePay(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''

    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
    else:
        overtime = totalHours - 40
        regularHours = 40

#Formula
    return hourlyWage*regularHours + (1.5*hourlyWage)*overtime

def main():
    hours = int(input('Enter hours worked: '))
    wage = int(input('Enter dollars paid per hour: '))
    total = calculatePay(hours, wage)
    print ("Your gross pay would be $", total)

main()

#________________________________________________________________________
#________________________________________________________________________

# Question 2

 '''chapter 8 problem 2 - Write a function triNumber.  The function should take 
 an integer,n, which represents the number in the sequence you want to calculate 
 as it's parameter and should return the "nth" triangular number.  Write a 
 program that asks the user how many triangular numbers to print and then prints 
 an attractively formatted table like the one illustrated in your text.'''

#The Function
def triNumber(n):
# The Formula
    return n * (n+1) / 2

# The variable	 requested
num = int(input("How many triNumbers would you like to print?:"))

#formating the columns
print(" N","   ","TriNum")
print("___","   ","________")

for i in range(1, num + 1):
    print (i,'\t','\t', int(triNumber(i)))

#_________________________________________________________________________
#_________________________________________________________________________

# Question 3

"""chapter 8 chart practice - Write a function called calculateArea.  The function should take a parameter that represents the radius of a circle and should return the area of the circle.  Write a program that asks the user to enter the number of circles.  The program should then display a chart that lists the radius of the circle and it's area beginning at 1 and continuing up to and including the number entered by the user."""

import math

#The Function
def calculateArea(r):
# The Formula
    return r ** 2 * math.pi
# The variable	 requested
num = int(input("How many circles would you like to find the radius for?:"))

# Formating the columns
print("Radius"," ","  Area  ")
print("______"," ","________")

for i in range(1, num + 1):
    print (i,'\t','\t', calculateArea(i))

# ok, I got this to work, however, I could not figure out how to get float
# to work. So, the answers are correct to the left of the decimal,
# because everything to the right of the decimal is dropped.
# changed the output to float after trial and error in class on monday.

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Question 4
	"""chapter 8 problem 3 - Write a function isPrime.  The function should take an integer,n. which represents the number you want to check for "primeness" and should return true or false.  Write a program that asks the user how many numbers to check for primeness and then prints an attractively formatted table that lists each number between 2 and the number entered by the user and whether or not that number is prime."""

# The Function
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
# User input
num = int(input("How many numbers should primeness be checked for?:"))

# Formating the columns
print("Prime#","  ","Prime or Not Prime  ")
print("______","  ","_______________")

# start at 2, take the user input, and add one, then change "num" to "i",
#put it in the formula above and print in a column with three space gap.
for i in range(1, num + 1):
    print (i,'\t','\t','\t', is_prime(i))

# basically i took the code from the answer. I then figured out how to get an answer,
# however the true/false column gave me numbers (1=T, 2=F). I then removed the 
# parenthesis from around "is_prime(i)" in the last line and it gave me the
# True/False answer format I sought.

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Question 5

"""
Write a function countDigits.  The function should take an integer, n, which 
represents the number for which you want to count digits and should return an 
integer representing the number of digits in the number.  Write a program that 
asks the user to enter a number and prints out the number of digits in the number.
  The program should then ask the user if he/she wants to enter another number 
  and should allow him/her to answer 1 to continue and 0 to stop.  If the user
  enters a 1, the process should repeat.
"""
# Function
def countDigits(n):
    """Count the number of digits in a given number "n". """
    num = len(str(abs(n)))
    return num

num_to_count = int(input("Count how many digits are in the number of: "))
print("There are",countDigits(num_to_count),"digits in the number",num_to_count,"\n")
"""
again = 1

while again == 1:

    print (call+
    again = int(input(" 1 or a 0"))

"""
# This is as far as I got on this question (and it was the last question i did in this lab), then we had class and went over it, but that made me really confused.

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Question 6

"""
Write a program that allows the user to play a guess my number game.  The computer 
should generate a random number between 1 and 100.  The user should guess the number 
until he/she guesses the number generated by the computer.  Each time the user 
guesses the computer should display "Too High", "Too low".  When the user guesses 
correctly, the computer should display, "You got it" and the number of guesses 
that the user made.
"""
# Import the random module.
import random

# Stores the number of guesses the player has made. using 0 for no choice.
guessesTaken = 0
# Asks the user for a name and stores it
print('Hello! What is your name?')
myName = input()                    #user enters name and it is stored for later.

# Using random module to generate a randome number between 1 and 100 and store it.
number = random.randint(1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

# Loop for the guessed number.
while guessesTaken < 100:              # Number of guesses allowed is 100.
	print('Take a guess.')
	guess = input()                    # User input of their guess
	guess = int(guess)                 # Guess equals the integer of the guess

	guessesTaken = guessesTaken + 1    # tracks the Number of guesses.

	if guess < number:
		print('Your guess is too low.') # There are eight spaces in front of print.

	if guess > number:
		print('Your guess is too high.')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Thants the number, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number)

# Taking a set of code snippets and breaking them down to where I understand what
# its doing is what I did here. I learned: 1)I learned that there is a module
# named "random". 2) I learned that I can use the + variable + to join two outer
# strings into one with the variable entered within. 3)I learned I can set the
# range that I wanted the random number to randomly be chosen from. 4)using the
# WHILE function will repeat until the expression equals false. 5) I also learned
# that I could set a limit on the number of guesses entered. 
#

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Question 7
"""
Write a function to remove all the red from an image.
"""

import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        newred = 0
        green = p.getGreen()
        blue = p.getBlue()

        newpixel = image.Pixel(newred, green, blue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()

# newred = 0 removes all the red.
