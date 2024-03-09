from PIL import ImageGrab, Image
import winsound
import keyboard
import random
import pygame
import time

pygame.init()

screen_width = 2560
screen_height = 1440
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def surface(image):
    surface = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()
    return pygame.transform.scale(surface, (screen_width, screen_height))

def melt(image):
    random_column = random.randint(0, image.width)
    crop_width = random.randint(5, 20)
    cropped_image = image.crop((random_column, 0, random_column + crop_width, image.height))
    image.paste(cropped_image, (random_column, random.randint(1, 3)))

def sound():
    sounds = ["SystemAsterisk", "SystemExclamation", "SystemExit", "SystemHand", "SystemQuestion"]
    soundchoice = random.choice(sounds)
    winsound.PlaySound(soundchoice, winsound.SND_ALIAS)

def kill():
    return keyboard.is_pressed('win+backspace')

image = ImageGrab.grab()
pg_surface = surface(image)

running = True
ticks = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(pg_surface, (0, 0))

    if ticks % random.randint(2, 5) == 0:
        melt(image)
        pg_surface = surface(image)

    if random.random() < 0.01:  
        sound()

    if kill():
        running = False

    pygame.display.update()
    clock.tick(120)
    ticks += 1

pygame.quit()
