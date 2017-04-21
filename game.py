import pygame
from math import fabs
from random import randint
# in order to use py game, we have top use the init method
pygame.init()

screen = {
	"height": 512,
	"width": 480,
}

keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

hero = {
	'x': 100,
	'y': 100,
	'speed': 5,
	'wins': 0
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False,
}


goblin = {
	'x': 300,
	'y': 300,
	'speed': 5,
	'direction': 'N'
}

directions = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']

monster = {
	'x': 150,
	'y': 300,
	'speed': 5,
	'direction': 'E'
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
backgroung_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')

# //////////////MAIN GAME LOOP////////////////
# //////////////MAIN GAME LOOP////////////////
# //////////////MAIN GAME LOOP////////////////
tick = 0

game_on = True
while game_on: 
	tick += 1
	# ---EVENTS!---
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False	
		elif event.type == pygame.KEYDOWN:
			print event.key
			if event.key == keys['up']:
				keys_down['up'] = True
				
			elif event.key == keys['down']:
				keys_down['down'] = True
				
			elif event.key == keys['right']:
				keys_down['right'] = True
				
			elif event.key == keys['left']:
				keys_down['left'] = True
			 
		elif event.type == pygame.KEYUP:
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False


	# HERO MOVE
	if keys_down['up']:
		hero['y'] -= hero['speed']
	if keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['right']:
		hero['x'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']

	if hero['x'] > screen['width']:
		hero['x'] = 0
	elif hero['x'] == 0:
		hero['x'] = screen['width']
	if hero['y'] > screen['height']:
		hero['y'] = 0
	elif hero['y'] < 0:
		hero['y'] = screen['height']



	# COLLISION DETECTION
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if (distance_between < 32):
		# generate a random X > 0, X < screen['width']
		# generate a random Y > 0, Y < screen['height']
		rand_x = randint(0, screen['width'] - 128)
		rand_y = randint(0, screen['height'] - 128)
		goblin['x'] = rand_x
		goblin['y'] = rand_y
		hero['wins'] += 1

	# GOBLIN MOVEMENT

	if goblin['direction'] == 'N':
		goblin['y'] -= goblin['speed']
	elif goblin['direction'] == 'S':
		goblin['y'] += goblin['speed']
	elif goblin['direction'] == 'E':
		goblin['x'] -= goblin['speed']
	elif goblin['direction'] == 'W':
		goblin['x'] += goblin['speed']
	if goblin['direction'] == 'NE':
		goblin['y'] -= goblin['speed']
		goblin['x'] -= goblin['speed']
	if goblin['direction'] == 'NW':
		goblin['y'] -= goblin['speed']
		goblin['x'] += goblin['speed']
	if goblin['direction'] == 'SE':
		goblin['x'] -= goblin['speed']
		goblin['y'] += goblin['speed']
	if goblin['direction'] == 'SW':
		goblin['x'] += goblin['speed']
		goblin['y'] += goblin['speed']

	if (tick % 60 == 0):
		new_dir = randint(0, len(directions)-1)
		goblin['direction'] = directions[new_dir]

	if goblin['x'] > screen['width']:
		goblin['x'] = 0
	elif goblin['x'] == 0:
		goblin['x'] = screen['width']
	if goblin['y'] > screen['height']:
		goblin['y'] = 0
	elif goblin['y'] < 0:
		goblin['y'] = screen['height']

	# goblins_move = randint(1, 5)
	# if goblins_move == 1:
	# 	goblin['y'] -= goblin['speed']
	# elif goblins_move == 2:
	# 	goblin['y'] += goblin['speed']
	# elif goblins_move == 3:
	# 	goblin['x'] -= goblin['speed']
	# elif goblins_move == 4:
	# 	goblin['x'] += goblin['speed']

	# if goblin['x'] < 64 | goblin['y'] < 64 | goblin['x'] > 500 | goblin['y'] > 460:
	# 	goblin['speed'] = 0




	# MONSTER MOVEMENT
	
	if monster['direction'] == 'N':
		monster['y'] -= monster['speed']
	elif monster['direction'] == 'S':
		monster['y'] += monster['speed']
	elif monster['direction'] == 'E':
		monster['x'] -= monster['speed']
	elif monster['direction'] == 'W':
		monster['x'] += monster['speed']
	if monster['direction'] == 'NE':
		monster['y'] -= monster['speed']
		monster['x'] -= monster['speed']
	if monster['direction'] == 'NW':
		monster['y'] -= monster['speed']
		monster['x'] += monster['speed']
	if monster['direction'] == 'SE':
		monster['x'] -= monster['speed']
		monster['y'] += monster['speed']
	if monster['direction'] == 'SW':
		monster['x'] += monster['speed']
		monster['y'] += monster['speed']


	if (tick % 60 == 0):
		new_dir = randint(0, len(directions)-1)
		monster['direction'] = directions[new_dir]

	if monster['x'] > screen['width']:
		monster['x'] = 0
	elif monster['x'] == 0:
		monster['x'] = screen['width']
	if monster['y'] > screen['height']:
		monster['y'] = 0
	elif monster['y'] < 0:
		monster['y'] = screen['height']




	# MUSIC
	# pygame.mixer.music.load('sounds/music.wav')
	# pygame.mixer.music.play(-1)
	# win_sound =
	# lose sound =


	# RENDER
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	pygame_screen.blit(backgroung_image, [0,0])

	# draw hwro wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render(("Wins %d") % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40, 40])

	# draw the hero 
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])

	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])

	pygame_screen.blit(monster_image, [monster['x'], monster['y']])


	# clear screen for the next time
	pygame.display.flip()