## [turtle]
import turtle

turtle.shape('turtle') # задать форму черепашки (arrow, turtle, circle, square)
turtle.pensize(5)  # задтать толщину линии
turtle.pencolor('blue') # цвет линии
turtle.bgcolor('yellow') # цвет фона
turtle.speed(1)

turtle.delay(100)

turtle.forward(100) # перемещение вперед на 100 пикселей
turtle.penup() # поднять перо
turtle.forward(50)
pos = turtle.pos() # получить текущие координаты
x = pos[0]
y = pos[1]
print('x =', x, ' y =', y)
turtle.pendown() # опустить перо
turtle.forward(100)

turtle.left(90) # поворот влево на 90 град
turtle.forward(100)

turtle.right(45) # поворот вправо на 90 град
turtle.backward(100) # двигаться назад на 100 пикселей

turtle.home() # переместиться в точку с координатами (0, 0)

turtle.goto(-100, -150) # переместить в точку с координатами (x = -100, y = -150)

turtle.mainloop()
## [subcode]

import turtle
screen = turtle.Screen()
def key_up():
    turtle.goto(turtle.xcor() , turtle.ycor()+10)
    
def key_down():
    turtle.goto(turtle.xcor(), turtle.ycor()-10)
    
def key_left():
    turtle.backward(10)
    
def key_right():
    turtle.forward(10)
    
screen.onkey(key_up, 'Up')
screen.onkey(key_down, 'Down')
screen.onkey(key_left, 'Left')
screen.onkey(key_right, 'Right')
screen.listen()
turtle.mainloop()

## [subcode]

