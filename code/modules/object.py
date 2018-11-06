import pyglet
import random

class Object(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Object, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

    def check_bounds(self):
    	min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.y < min_y:
        	self.y = max_y
        	self.x = random.randint(0, 800)
        elif self.y > max_y:
        	self.y = min_y

    def update(self, delta):

        #super(Object, self).update(delta)
    	self.x += self.velocity_x * delta
    	self.y += self.velocity_y + delta
    	self.check_bounds()

