import turtle

#Задать переменнюу length (длинна) равную 10 
length = 10

#Задать перемунную zoom равную 1 
zoom = 1

#------------- Функция drawTriangle 
def drawTriangle(length):
    # Повторять 3 раза 
    for i in range(3):
        # Переместить черепашку на расстояние length 
        turtle.forward(length)
        # Повернуть черепашку на 120 градусов влево
        turtle.left(120)

#------------- Функция weaveOneLayer 
def weaveOneLayer():
    global length, zoom
    #Повторить 6 раз 
    for i in range(6):
        # Выполнить функцию drawTriangle 
        drawTriangle(length)
        # Повернуть черепашку на угол 60 градусов влево
        turtle.left(60)
        # Увеличить длинну length на величину length + zoom 
        length = length + zoom

#Повторять 10 раз 
for i in range(10):
    #Вызвать функцию weaveOneLayer
    weaveOneLayer()
    #Изменить переменную zoom на zoom * 1.3 
    zoom *= 1.3
  




