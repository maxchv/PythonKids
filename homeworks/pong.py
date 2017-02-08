import simpleguitk as gui

time = 0 # глобальная переменная

height = 500
frame = gui.create_frame('Game', 600, height)

r = 30  # радиус мяча
point = [20, 20] # центр мяча
acc = [2, 3] # ускорение по гризонтали и вертикали

def draw(canvas):    
    canvas.draw_circle(point, r, 1, 'Red', 'Red')

def timer_handler():
    global time # объявляю для изменения глобальной переменной
    time += 1
    print('timer', time)
    point[0] += acc[0]
    point[1] += acc[1]
    print("point: ", point)
    # пересечение нижней границы холста
    if point[1] + r > height:
        acc[1] = -acc[1]

frame.set_draw_handler(draw)
timer = gui.create_timer(1000//60, timer_handler)

timer.start()
frame.start()
