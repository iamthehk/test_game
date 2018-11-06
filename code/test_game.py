import pyglet
from modules import load, resources, object, mainobject

game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Test Game", x=10, y=575, batch=main_batch)

resources.scale_image(resources.red_bubble, game_window, 0.05, 0.05)
resources.scale_image(resources.gray_bubble, game_window, 0.05, 0.05)

red_bubble = mainobject.MainObject(img=resources.red_bubble, x=400, y=50, batch=main_batch)
game_window.push_handlers(red_bubble)

gray_bubbles = load.grayBubbles(20, red_bubble.position, main_batch)

game_objects = [red_bubble] + gray_bubbles

def update(delta):
	for obj in game_objects:
		obj.update(delta)
	for gray_bubble in gray_bubbles:
		if red_bubble.collides(gray_bubble):
			exit()


@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()
		

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/240.0)
	pyglet.app.run()