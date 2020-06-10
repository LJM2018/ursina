from ursina import *
app = Ursina()
# initialize cars in the scenario
car1 = Entity(model='cube', color=color.green, scale_y=2, scale_x=1, scale_z=1)
car2 = Entity(model='cube', color=color.green, scale_y=2, scale_x=1, scale_z=1)
car3 = Entity(model='cube', color=color.green, scale_y=2, scale_x=1, scale_z=1)
# Ego car
car = Entity(model='cube', color=color.blue, scale_y=2, scale_x=1, scale_z=1)

def update():
	player.x += held_keys['d']*time.dt
	player.x -= held_keys['a']*time.dt

def input(key):
	if key == 'space':
		player.y += 1
		invoke(setattr, player, 'y', player.y-1, delay=.25)

app.run()