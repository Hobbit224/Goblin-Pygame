import pygame

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
	'speed': 5
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
	'speed': 5
}


screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
backgroung_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')

# //////////////MAIN GAME LOOP////////////////
# //////////////MAIN GAME LOOP////////////////
# //////////////MAIN GAME LOOP////////////////


game_on = True
while game_on: 
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



	if keys_down['up']:
		hero['y'] -= hero['speed']
	if keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['right']:
		hero['x'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	# RENDER
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	pygame_screen.blit(backgroung_image, [0,0])

	# draw the hero 
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])

	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])


	# clear screen for the next time
	pygame.display.flip()