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
	'speed': 20
}
screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
backgroung_image = pygame.image.load('images/background.png')
hero_image =pygame.image.load('images/hero.png')

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
				print "User pressed up!"
				hero['y'] -= hero['speed']
			elif event.key == keys['down']:
				print "User pressed down!"
				hero['y'] += hero['speed']
			elif event.key == keys['right']:
				print "User pressed right!"
				hero['x'] += hero['speed']
			elif event.key == keys['left']:
			 print "User pressed down!"
			 hero['x'] -= hero['speed']
	# RENDER
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	pygame_screen.blit(backgroung_image, [0,0])

	# draw the hero 
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])


	# clear screen for the next time
	pygame.display.flip()