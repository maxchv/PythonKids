
import turtle

# определение функции
def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

for i in range(4):
    draw_square(50) # вызов функции
    turtle.right(90)
    
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()

draw_square(300)
