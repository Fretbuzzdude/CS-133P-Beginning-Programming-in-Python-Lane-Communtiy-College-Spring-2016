#cs133p
#Chapter 1 and 2 exercises
#
#-----------------------------------------------
#
# question 9: Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.
print("Lets calculate the area of a rectangle by entering the values for width and height")
width = int(input("Width? "))
height = int(input("Height? "))
area = width * height
print("Who would of thought! The area of the rectangle with the width",width, "and the height",height, "would equal", area)
#This one seamed easy enough to accomplish. Its my first program evver...Since my days with my new Commadore VIC20 or my AppleSoft programming class in Highschool.
#
#-----------------------------------------------
#-----------------------------------------------
#
# question 10: Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.
print ('Lets calculate the MPG for a car by entering the miles driven and the gallons used.')
miles = int(input("Total miles driven? "))
gallons = int(input("Total gallons of gas consumed? "))
MPG = miles / gallons
print ("What a peice of junk your driving! Get yourself a YUGO. When you drive", miles,"miles and use", gallons,"gallons of gas, your MPG equals", MPG)
# I had to use my calculator to check my math.
# I also ried adding MPG to the right of the calculated output, but got an error.
# so I skipped it.
#
#-----------------------------------------------
#-----------------------------------------------
#
# Question 11: Write a program that will convert degrees celsius to degrees fahrenheit.
deg_c = int(input("Tell me what the temperature is in Celsius and I'll convert it to fahrenheit? "))
deg_f = deg_c * (9 / 5) + 32
print("The conversion of", deg_c,"celcius to fahrenheit is",deg_f,"degrees")
# this one took a lot of tries!
#-----------------------------------------------
#-----------------------------------------------
#
# Question 12: Write a program that will convert degrees fahrenheit to degrees celsius.
deg_ff = int(input("Tell me what the temperature is in fahrenheit and I'll convert it to celcius? "))
deg_cc = (deg_ff - 32) * 5 / 9
print("The conversion of", deg_ff,"fahrenheit to celcius is",deg_cc,"degrees")
# This just needed the names flipped. it worked fine.
#
#------------------------------------------------
#------------------------------------------------
#
#Question 7:Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08).
#Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
P = 10000
n = 12
r = 0.08
t = int(input("Enter the number of years to calculate the interest for."))
final = P * ( ((1 + (r/n)) ** (n * t)) )
print ("The amount of interest after", t, "years will be $"+ str(round(final,2)))
# it failed at first due to forgetting double **
#
#------------------------------------------------
#------------------------------------------------
#
# Question 8: Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.
r = int(input("Lets calculate the area of a circle, shall we?. Enter the value for the radius"))
height = int(input("what is the Height? "))
area = (r*r) * 3.14
print("The area of your circle, calculated from the radius",r,"and the height",height,"is", area)
#this took a thousand times because of comparing the answer I got to a calculator using a pi function. gave up and just used the non acurate 3.14.
#
#------------------------------------------------
#------------------------------------------------
#
