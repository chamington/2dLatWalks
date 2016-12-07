import turtle #I understand it's for children, but it's not like this program is really even needed
def walkVisualiser(x):
    #turtle.sety(0)
    #turtle.setx(0)
    turtle.hideturtle()
    turtle.pendown()
    for i in range(0,len(x)):
        y=x[i]
        if y=="U":
            turtle.sety(turtle.ycor()+1)
        if y=="D":
            turtle.sety(turtle.ycor()-1)
        if y=="L":
            turtle.setx(turtle.xcor()-1)
        if y=="R":
            turtle.setx(turtle.xcor()+1)
    #turtle.pu()
    #turtle.clear()
