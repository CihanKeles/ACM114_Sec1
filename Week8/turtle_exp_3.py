from turtle import *

def line(myLine, startX, startY, endX, endY, color):
    myLine.penup()              # Raise the pen
    myLine.goto(startX, startY) # Move to the starting point
    myLine.pendown()            # Lower the pen
    myLine.pencolor(color)      # Set the pen color
    myLine.goto(endX, endY)     # Draw a square

space = Screen()
corona = Turtle()

TOP_X = 0
TOP_Y = 100
BASE_LEFT_X = -100
BASE_LEFT_Y = -100
BASE_RIGHT_X = 100
BASE_RIGHT_Y = -100
line(corona, TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
line(corona, TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
line(corona, BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')
