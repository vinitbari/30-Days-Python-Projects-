import turtle 
arrow= turtle.Turtle() 
arrow.pencolor("red") 
screen = turtle.Screen() 
screen.bgcolor("black") 
arrow.speed(0) 
arrow.penup() 
arrow.goto(0,150) 
arrow.pendown() 
forw = 0 
right = 0 
while True: arrow.forward(forw) 
arrow.right(right) 
forw += 2 
right += 1 
turtle.done()