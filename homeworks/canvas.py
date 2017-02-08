import simpleguitk as gui

frame = gui.create_frame('Game', 600, 500)

point = [20, 20]

def down():
    point[1] += 10

btn_down = frame.add_button('Вниз', down)

def draw(canvas):
    print("update")
    canvas.draw_text("Hello SimpleGUI", point,
                     20, "Red")

frame.set_draw_handler(draw)

frame.start()
