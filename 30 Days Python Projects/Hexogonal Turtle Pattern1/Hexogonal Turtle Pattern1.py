import turtle 
import random 
screen = turtle.Screen() 
screen.bgcolor("black") 
t = turtle.Turtle() 
t.speed(0) 
t.width(2) 
def draw_spiral(): 
 for _ in range(200): 
  t.pencolor(random.random(), random.random(), random.random()) 
  t.circle(100 + _) 
  t.left(30) 
  screen.bgcolor(random.random(), random.random(), random.random()) 
  t.hideturtle() 
  draw_spiral() 
  screen.mainloop()