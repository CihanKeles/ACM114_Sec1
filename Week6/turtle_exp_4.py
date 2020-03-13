from turtle import *

space = Screen()
ali = Turtle()

START_X = -200      # Starting X coordinate
START_Y = 0         # Starting Y coordinate
NUM_LINES = 36      # Number of lines to draw
LINE_LENGTH = 400   # Length of each line
ANGLE = 170         # Angle to turn

ali.hideturtle()
ali.penup()
ali.goto(START_X, START_Y)
ali.pendown()

for x in range(NUM_LINES):
    ali.forward(LINE_LENGTH)
    ali.left(ANGLE)
