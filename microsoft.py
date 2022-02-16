
import turtle
HEIGHT,WEIDTH=500,500


turtle.Screen()
turtle.setup(HEIGHT,WEIDTH)






#first square
soft=turtle.Turtle()

soft.fillcolor('sky blue')
soft.begin_fill()
soft.forward(100)
soft.left(90)
soft.forward(100)
soft.left(90)
soft.forward(100)
soft.left(90)
soft.forward(100)
soft.left(-90)
soft.end_fill()
soft.penup()

soft.forward(15)
soft.pendown()
soft.begin_fill()
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.end_fill()
soft.penup()
soft.forward(15)
soft.pendown()
soft.begin_fill()
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.left(90)
soft.end_fill()
soft.penup()
soft.forward(15)
soft.pendown()
soft.begin_fill()
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.forward(100)
soft.left(-90)
soft.left(90)
soft.end_fill()




soft.penup()
soft.goto(-300,200)


while True:
    turtle.update()
