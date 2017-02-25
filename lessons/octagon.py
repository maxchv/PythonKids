## [subcode]

import turtle
# Объявить глобальную переменную count = 9
count = 9
# Объявить глобальную переменную length = 110
length = 100
# Объявить функцию draw_octagon
def draw_octagon():
  # Начать цикл count раз
  for i in range(count):
    # Переместить черепашку на length пикселей 
    turtle.forward(length)
    # Повернуть черепашку на  360 / 8 градусов 
    turtle.right(360//8)
## [subcode]






















c = 0
colors =[ "HotPink", "Red", "Fuchsia", "OrangeRed",
          "DeepPink", "MediumVioletRed", "Crimson", "Tomato" ]

def next_color():
    global curr_color
    turtle.pencolor(colors[c%len(colors)])
    curr_color += 1



















    
## [subcode]

# Начать цикл 30 раз
for i in range(30):    
    next_color()
    # Вызвать функцию draw_octagon
    draw_octagon()
    # Повернуть черепашку на  360 / 30 + 5 градусов
    turtle.right(360//30+5)


    
