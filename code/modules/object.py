import pyglet
import random

class Object(pyglet.sprite.Sprite):

    win = None
    def __init__(self, window, *args, **kwargs):
        super(Object, self).__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.gravity = window.height//20.0
        self.start_phase_out = False
        self.win = window

    def check_bounds(self):
        min_x = 0
        min_y = self.win.height /20.0
        max_x = self.win.width
        max_y = self.win.height
        if self.y < min_y:
            self.y = min_y
            self.velocity_y = 0.0
            # start phasing out animation
            self.start_phase_out = True
        else:
            self.velocity_y -= self.gravity

        if self.opacity <= 10:
            self.start_phase_out = False
            self.y = self.win.height*1.2
            self.x = random.randint(0, self.win.width)
            self.opacity = 255

    def phase_out(self, delta):
        if self.start_phase_out:
            self.opacity -= round(delta * 256)


    def update(self, delta):
        #super(Object, self).update(delta)
        self.x += self.velocity_x * delta
        self.y += self.velocity_y * delta
        self.check_bounds()
        self.phase_out(delta)
