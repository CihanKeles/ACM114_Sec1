from turtle import *

def square(myTurtle, x, y, width, color):
    myTurtle.penup()            # Raise the pen
    myTurtle.goto(x, y)         # Move to (X,Y)
    myTurtle.fillcolor(color)   # Set the fill color
    myTurtle.pendown()          # Lower the pen
    myTurtle.begin_fill()       # Start filling
    for count in range(4):      # Draw a square
        myTurtle.forward(width)
        myTurtle.left(90)
    myTurtle.end_fill()         # End filling

space = Screen()
corona = Turtle()

square(corona, 100, -200, 50, 'red')
square(corona, -200, -150, 200, 'blue')
square(corona, -175, 100, 75, 'green')
square(corona, 125, 125, 100, 'cyan')
square(corona, 150, -100, 150, 'yellow')

