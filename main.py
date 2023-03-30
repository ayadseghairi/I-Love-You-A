import turtle
# create a turtle object
t = turtle.Turtle()
# set the turtle's speed
t.speed(6)
# move the turtle to the starting position
t.penup()
t.goto(0, -100)
t.pendown()
# draw the heart shape
t.color('red')
t.begin_fill()
t.left(45)
t.forward(150)
t.circle(75, 180)
t.right(90)
t.circle(75, 180)
t.forward(150)
t.end_fill()
# write "I Love You" in the center of the heart
t.penup()
t.goto(0, 50)
t.color('white')
t.write("I Love You", align="center", font=("Arial", 20, "bold"))
# move the turtle to the center of the heart
t.penup()
t.goto(0, 25)
t.pendown()
# draw the letter "A" in the center of the heart
t.color('white')
t.pensize(5)
t.penup()
t.goto(-30, -20)
t.pendown()
# Draw the letter "A"
t.goto(0, 50)
t.goto(30, -20)
t.penup()
t.goto(-15, 13)
t.pendown()
t.goto(15, 13)
# hide the turtle
t.hideturtle()
# keep the turtle window open until it is manually closed
turtle.done()


