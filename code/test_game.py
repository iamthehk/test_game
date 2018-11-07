import pyglet
from modules import load, resources, object, mainobject

screen_width = 800
screen_height = 600
game_window = pyglet.window.Window(screen_width, screen_height)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Test Game", x=10, y=575, batch=main_batch)

resources.scale_image(resources.red_bubble, game_window, 0.05, 0.05)
resources.scale_image(resources.gray_bubble, game_window, 0.05, 0.05)

red_bubble = mainobject.MainObject(game_window, img=resources.red_bubble, x=screen_width/2, y=screen_height/10, batch=main_batch)
game_window.push_handlers(red_bubble)

gray_bubbles = load.grayBubbles(game_window, 20, red_bubble.position, main_batch)

game_objects = [red_bubble] + gray_bubbles
game_time = 0
prev_time = 0

def update(delta):
    global game_time
    global prev_time
    global gray_bubbles
    global game_objects

    game_time += delta
    for obj in game_objects:
        obj.update(delta)
    for gray_bubble in gray_bubbles:
        if red_bubble.collides(gray_bubble):
            exit()
    if (round(game_time /10) > prev_time):
        print("Add more bubbles")
        prev_time = round(game_time /10)
        gray_bubbles = load.addGrayBubbles(game_window, gray_bubbles, 10, main_batch)
        game_objects = [red_bubble] + gray_bubbles

@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()
		

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/240.0)
	pyglet.app.run()