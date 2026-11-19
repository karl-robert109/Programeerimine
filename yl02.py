 # Karl-Robert 19.11.26

# Olümpiarõngad
import turtle

aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad - Karl")

turtle.speed(0)
turtle.pensize(6)

turtle.color("blue")
turtle.up()
turtle.goto(-110,0)
turtle.down()
turtle.circle(50)

turtle.color("black")
turtle.up()
turtle.goto(-0,0)
turtle.down()
turtle.circle(50)

turtle.color("red")
turtle.up()
turtle.goto(110,0)
turtle.down()
turtle.circle(50)

turtle.color("yellow")
turtle.up()
turtle.goto(-55,-55)
turtle.down()
turtle.circle(50)

turtle.color("green")
turtle.up()
turtle.goto(55,-55)
turtle.down()
turtle.circle(50)

turtle.done()