import pyglet
import random

class Object(pyglet.sprite.Sprite):

    win = None
    def __init__(self, window, *args, **kwargs):
        super(Object, self).__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.win = window

    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = self.win.width
        max_y = self.win.height
        if self.y < min_y:
            self.y = max_y
            self.x = random.randint(0, 800)
            self.velocity_y = random.uniform(-5.0, -1.0)
        elif self.y > max_y:
            self.y = min_y

    def update(self, delta):
        #super(Object, self).update(delta)
        self.x += self.velocity_x * delta
        self.y += self.velocity_y + delta
        self.check_bounds()

