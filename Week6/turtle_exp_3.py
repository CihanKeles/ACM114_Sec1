from turtle import *

space = Screen()
ali = Turtle()

NUM_CIRCLES = 36    # Number of circles to draw
RADIUS = 100        # Radius of each circle
ANGLE = 10          # Angle to turn

for x in range(NUM_CIRCLES):
    ali.circle(RADIUS)
    ali.left(ANGLE)
