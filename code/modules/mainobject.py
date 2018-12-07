import pyglet
import math 
from pyglet.window import key
from pyglet.window import mouse
from . import load

class MainObject(pyglet.sprite.Sprite):

    win = None

    def __init__(self, window, *args, **kwargs):
        super(MainObject, self).__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = window.width//2.0, 0.0
        self.gravity = window.height//10.0
        self.jumping = False
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.win = window

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

    def check_bounds(self):
        min_x = 0
        min_y = self.win.height / 20
        max_x = self.win.width
        max_y = self.win.height
        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x
        if self.y < min_y:
            self.y = min_y
            if self.keys['up'] == False:
                self.jumping = False
                self.velocity_y = 0.0
        elif self.y > max_y:
            self.y = max_y

    def collides(self, other_object):
        collision_distance = self.image.width/3 + other_object.image.width/3
        actual_distance = load.distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)

    #def on_mouse_motion(self, x, y, dx, dy):
    #    #self.x = x
    #    #self.y = y

    def update(self, delta):
        #super(MainObject, self).update(delta)
        if self.keys['left']:
            self.x -= self.velocity_x * delta
        if self.keys['right']:
            self.x += self.velocity_x * delta
        if self.keys['up']:
            if self.jumping == False:
                self.jumping = True
                self.velocity_y = self.win.height * 1.5
        if self.jumping:
            self.velocity_y -= self.gravity
            self.y += self.velocity_y * delta
        self.check_bounds()

