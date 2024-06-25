import turtle 
turtle.bgcolor("black") 
turtle.pensize(2) 
turtle.speed(0) 
for i in range(7): 
    for colors in ["red ","b lue" ,"gr een" ,'ye llow ','o rang e ','pi nk', 'pur ple' ,'cy an', 'mag enta ', 'white']:
         turtle.color(colors) 
         turtle.circle(100) 
         turtle.left(10) 
turtle.hideturtle()