import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

def scale_image(image, game_window, width_rate, height_rate):
	image.width = game_window.width * width_rate
	image.height = game_window.width * height_rate
	center_image(image)

# Tell pyglet where to find the resources
pyglet.resource.path = ['../resource']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
red_bubble = pyglet.resource.image("red_bubble.png")
gray_bubble = pyglet.resource.image("gray_bubble.png")
