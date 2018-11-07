import pyglet
import random
import math
from . import resources, object

def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)

def grayBubbles(window, num_bubbles, player_position, batch=None):
    bubbles = []
    for i in range(num_bubbles):
        bubble_x, bubble_y = player_position
        bubble_x = random.randint(0, 800)
        bubble_y = 700
        new_bubble = object.Object(window, img=resources.gray_bubble,
                            x=bubble_x, y=bubble_y,
                            batch=batch)
        new_bubble.velocity_y = random.uniform(-5.0, -1.0)

        bubbles.append(new_bubble)
    return bubbles

def addGrayBubbles(window, bubbles, number_bubble_to_add, batch=None):
    for i in range(number_bubble_to_add):
        bubble_x = random.randint(0, 800)
        bubble_y = 700
        new_bubble = object.Object(window, img=resources.gray_bubble,
                            x=bubble_x, y=bubble_y,
                            batch=batch)
        new_bubble.velocity_y = random.uniform(-5.0, -1.0)

        bubbles.append(new_bubble)
    return bubbles