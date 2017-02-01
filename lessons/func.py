import turtle

# глобальная переменная
zoom = 1

# Функции
def draw_shape(l, n):
    for i in range(n):
        turtle.forward(l)
        turtle.left(360/n)

#draw_shape(100, 3)
#draw_shape(50, 4)
#draw_shape(80, 5)
#draw_shape(30, 6)

def change_zoom():
    global zoom # использоать глобальную переменную в функции
    print("zoom = ", zoom)
    zoom = 10
    print("zoom = ", zoom)

    
change_zoom()
print("zoom = ", zoom)
