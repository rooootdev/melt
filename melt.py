from PIL import ImageGrab, Image
import random
import pygame
import time

image = ImageGrab.grab()
pygame.init()

screen = pygame.display.set_mode((image.width, image.height))
clock = pygame.time.Clock()

def surface(image):
	i = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()
	return pygame.transform.scale(i, (2560, 1440))

def melt(image):
	random_column = random.randint(0, image.width)
	c = image.crop((random_column, 0, random_column + random.randint(5, 20), image.height))
	image.paste(c, (random_column, random.randint(1, 3)))

t = 0 # change value for more crazyness 
pg_im = surface(image)
while 1:
	for ev in pygame.event.get(): pass
	screen.blit(pg_im, (0, 0))
	if t % random.randint(2, 5):
		melt(image)
		pg_im = surface(image)
	pygame.display.update()
	clock.tick(120)
	t += 1