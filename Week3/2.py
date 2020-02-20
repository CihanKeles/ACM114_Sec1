import turtle
a = -100
turtle.goto(0, 100)
turtle.goto(a, 0)
turtle.goto(0, 0)

if turtle.speed() > 0:
    turtle.speed(0)

if turtle.xcor() == 0 and turtle.ycor() == 0:
    turtle.goto(-50, -50)
    



