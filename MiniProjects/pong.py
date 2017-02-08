import simpleguitk as simplegui

frame = simplegui.create_frame('Pong game', 600, 400)
frame.set_canvas_background('White')

string = ''
center = [0, 0]
speed = 3
def draw(canvas):
    ## canvas.draw_text(text, point, font_size, font_color)
    #canvas.draw_text(string, (20,20), 12, 'Red')
    ## canvas.draw_line(point1, point2, line_width, line_color)
    #canvas.draw_line((10,10), (100, 100), 5, 'White')
    ## canvas.draw_polyline(point_list, line_width, line_color)
    #canvas.draw_polyline([(10, 20), (30, 20), (90, 70)], 12, 'Red')
    #canvas.draw_polyline([[40, 20], [80, 40], [30, 90]], 20, 'Blue')
    ## canvas.draw_polygon(point_list, line_width, line_color, fill_color = color)
    # canvas.draw_polygon([[90, 70], [80, 40], [70, 90], [70, 70]], 12, 'Yellow', 'Orange')

    ## canvas.draw_circle(center_point, radius, line_width, line_color, fill_color=color)
    #canvas.draw_circle([70, 80], 30, 10, 'Yellow', 'Orange')

    ## canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)

    #canvas.draw_circle(center, 20, 1, 'Red', 'Red')
    # canvas.draw_image(image, (image.get_width() // 2, image.get_height() // 2),
    #                          (image.get_width(), image.get_height()), (50, 50), (100, 100), 2)
    # pass
    canvas.draw_image(ball, (ball.get_width()//2, ball.get_height()//2), (ball.get_width(), ball.get_height()), center, (50, 50))

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')
ball = simplegui.load_image('http://s1.iconbird.com/ico/2013/6/355/w128h1281372334742football.png')

def key_handler(key):
    global string
    string += chr(key)

def timer_handler():
    center[0] += speed
    center[1] += speed

frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
timer = simplegui.create_timer(1000//60, timer_handler)
timer.start()
frame.start()