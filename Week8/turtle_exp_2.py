from turtle import *

def circle(myTurtle, x, y, radius, color):
    myTurtle.penup()             # Raise the pen
    myTurtle.goto(x, y - radius) # Position the turtle
    myTurtle.fillcolor(color)    # Set the fill color
    myTurtle.pendown()           # Lower the pen
    myTurtle.begin_fill()        # Start filling
    myTurtle.circle(radius)      # Draw a circle
    myTurtle.end_fill()          # End filling
    
space = Screen()
corona = Turtle()

circle(corona, 0, 0, 100, 'red')
circle(corona, -150, -75, 50, 'blue')
circle(corona, -200, 150, 75, 'green')
circle(corona, 150, 150, 50, 'cyan')
circle(corona, 200, -150, 75, 'yellow')

