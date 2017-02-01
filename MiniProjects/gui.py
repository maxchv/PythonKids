# http://www.codeskulptor.org/docs.html

import simpleguitk as gui

points = []
frame = gui.create_frame('hello', 0, 0)
#frame.set_canvas_background('Blue')
label = frame.add_label("Label")
label.set_text("new text")


def input_handler(text):
    print("text: ", text)
    pass


input = frame.add_input("input", input_handler, 200)
input.set_text('text')


def handler():
    print(input.get_text())
    print("clicked")


lbl2 = frame.add_button("Button", handler, 100)


def keydown(key):
    print(key)


frame.set_keydown_handler(keydown)


def draw_handler(canvas):
    for point in points:
        canvas.draw_circle(point, 20, 1, 'Green', "Red")


frame.set_draw_handler(draw_handler)


def mouse_handler(mouse):
    print(mouse)
    global points
    points.append(mouse)


frame.set_mouseclick_handler(mouse_handler)
frame.start()
