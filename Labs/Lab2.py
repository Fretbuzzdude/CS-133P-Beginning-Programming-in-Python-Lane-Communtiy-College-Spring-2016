# Purpose:      Lab 2 Chapter 6-Functions
#
# Author:      Heath McConnell
#
# Created:     06/04/2016
# Note:		Although I was able to make it work, I feel even further behind in 
#		my comprehention of what I am doing. I feel more like when I was a
#		kid and would take a tape deck apart and put it back together, just
#		to see how it works and if it would still work after the rebuild.
#-------------------------------------------------------------------------------

#1
#Makes a Square
import turtle

def makeSquare(t,sz):
#makeSquare. It has two parameters — one to tell the function, named makeSquare, which turtle to move around (t) and the other to tell it the size of the square we want drawn (sz).
    for i in range(4):		#I really need to figure out what this means!
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
myrtle = turtle.Turtle()
myrtle.color("red")
myrtle.pensize(3)
myrtle.penup()
myrtle.backward(85)
myrtle.pendown()

for i in range(5):		#Why am I using the "for i in(): statement again?
    makeSquare(myrtle, 20)
    myrtle.penup()
    myrtle.forward(40)
    myrtle.pendown()


wn.exitonclick()              
# getting the pen to start farther left took me forever to get!
#-------------------------------------------------------------------------------

#2
#Make a Square in a square
import turtle

def drawSquare(t, sz):      # drawSquare. It has two parameters — one to tell
                            # the function, named makeSquare, which turtle to
                            # move around (t) and the other to tell it the size
                            # of the square we want drawn (sz).

    for i in range(4):
        myrtle.speed(10)
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")    # Background color

myrtle = turtle.Turtle()        # create turtle
myrtle.pensize(3)               # The line width

drawSquare(myrtle, 20)          # Call the function to draw the square

myrtle.penup()
myrtle.speed(10)
myrtle.goto(-10,-10)
myrtle.pendown()

drawSquare(myrtle,40)           # Draw another square

myrtle.penup()
myrtle.speed(10)
myrtle.goto(-20,-20)
myrtle.pendown()

drawSquare(myrtle,60)           # Draw another square

myrtle.penup()
myrtle.speed(10)
myrtle.goto(-30,-30)
myrtle.pendown()

drawSquare(myrtle,80)           # Draw another square

myrtle.penup()
myrtle.speed(10)
myrtle.goto(-40,-40)
myrtle.pendown()

drawSquare(myrtle,100)           # Draw another square


wn.exitonclick()

# This one reminded me a little of all my years using AutoCAD. Once I got
# the initial goto down, it all flowed.
#------------------------------------------------------------------------------

#3
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

#add user input here instead of hard coding
num=int(input("Sides?"))
size=int(input("Size?"))


wn = turtle.Screen()
wn.bgcolor("lightgreen")
myrtle = turtle.Turtle()
myrtle.pensize(3)


drawPoly(myrtle,num,size)
#drawPoly(myrtle, 8, 50) #Do not hard code like this!


wn.exitonclick()

# I tried to make this create a bigger and bigger polygon, like exercise 2,
# but then realized that was a waste of time. That really wasnt what the
# exercise asked me to do, so I finished it; however, when I got in class, 
# the requirements for this lesson was changed.Glad I didnt turn it in Sunday.
#-------------------------------------------------------------------------------------

#4
#Draw a Multi square design
import turtle

def drawMultiSquare(t, sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['blue','blue','blue','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()             s
wn.bgcolor("lightgreen")

myrtle = turtle.Turtle()          
myrtle.pensize(3)
myrtle.speed(0)

size = 100                        # size of the smallest square
for i in range(20):
    drawMultiSquare(myrtle, size)
    size = size             # increase the size for next time
    myrtle.right(18)               # and give her some extra turn

wn.exitonclick()

#I used a lot of trial and error on the size, number of boxes, and the color.
#-------------------------------------------------------------------------------

#5
#Draw Spiral Stuff
import turtle

def drawSpiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(41):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()      
wn.bgcolor("lightgreen")
guido = turtle.Turtle()    # create guido
guido.color('blue')

guido.penup()           # draw the first spiral #
guido.speed(10)
guido.backward(110)     #move turtle to the left
guido.pendown()

drawSpiral(guido, 90)

guido.penup()           # draw the second spiral #
guido.home()
guido.forward(90)
guido.pendown()

drawSpiral(guido, 89)

wn.exitonclick()

#I had the hardest time trying to get the design on the left to not draw a line to 0,0 when it was done.
#-------------------------------------------------------------------------------

#6
#Draw Triangle
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

def drawEquitriangle(t2, s2):

    drawPoly(t2,3,s2)



wn = turtle.Screen()
wn.bgcolor("lightgreen")
myrtle = turtle.Turtle()
myrtle.pensize(3)

drawEquitriangle(myrtle, 50)

wn.exitonclick()

#this was very simple using previous code from #3
#-------------------------------------------------------------------------------

#9
#Draw a star
import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)
        myrtle.speed(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
myrtle = turtle.Turtle()
myrtle.pensize(3)
myrtle.speed(0)
myrtle.penup()			#Move to left of screen to start
myrtle.backward(210)
myrtle.pendown()		#end that move process

drawFivePointStar(myrtle)

wn.exitonclick()
#I forgot a few important items here, like defining the window.
#-------------------------------------------------------------------------------

#10
#Draw Five Stars
import turtle

def drawFivePointStar(t):
    for i in range(5):
        myrtle.speed(10)
        t.forward(100)
        t.left(216)


wn = turtle.Screen()		# Set up the window and its attributes
wn.bgcolor("lightgreen")	#Background Color
myrtle = turtle.Turtle()	# create myrtle the turtle
myrtle.color('blue')		#Myrtle is Blue
myrtle.penup()			#Move to left of screen to start
myrtle.backward(210)
myrtle.pendown()		#end that move process

drawFivePointStar(myrtle)	#call the Function(?)


myrtle.penup()			# draw the second star #
myrtle.speed(10)
myrtle.forward(350)
myrtle.right(144)
myrtle.pendown()

drawFivePointStar(myrtle)


myrtle.penup()			# draw the third spiral ##
myrtle.speed(10)
myrtle.forward(350)
myrtle.right(144)
myrtle.pendown()

drawFivePointStar(myrtle)

myrtle.penup()			# draw the fourth spiral ##
myrtle.speed(10)
myrtle.forward(350)
myrtle.right(144)
myrtle.pendown()

drawFivePointStar(myrtle)

myrtle.penup()			# draw the fifth spiral ##
myrtle.speed(10)
myrtle.forward(350)
myrtle.right(144)
myrtle.pendown()

drawFivePointStar(myrtle)

wn.exitonclick()

#This exercise took some work to figure out how to move left before drawing anything and then drawing more than one star. 
