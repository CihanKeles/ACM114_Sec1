from turtle import *

def makeRectangle(myTurtle, x, y):
    myTurtle.forward(x)
    myTurtle.left(90)
    myTurtle.forward(y)
    myTurtle.left(90)
    myTurtle.forward(x)
    myTurtle.left(90)
    myTurtle.forward(y)
    
space = Screen()
corona = Turtle()

color_list = ['red', 'blue', 'black', 'magenta', 'cyan', 'brown', 'lightblue']
for i in range(10):
    next_color = color_list[(i) % len(color_list)]
    corona.pensize(i**1.5)
    corona.color(next_color)
    makeRectangle(corona, 50, 100)
    corona.left(100)
