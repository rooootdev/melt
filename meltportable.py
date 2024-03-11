import random, pygame
from PIL import ImageGrab

pygame.init()
w, h = 2560, 1440
screen = pygame.display.set_mode((w, h))
def surface(i): return pygame.image.fromstring(i.tobytes(), i.size, i.mode).convert_alpha()
def melt(i):
    c, w = random.randint(0, i.width), random.randint(5, 20)
    i.paste(i.crop((c, 0, c + w, i.height)), (c, random.randint(1, 3)))
i = ImageGrab.grab()
p = surface(i)
r, t = True, 0
while r:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: r = False
    screen.blit(p, (0, 0))
    if t % random.randint(2, 5) == 0: melt(i); p = surface(i)
    pygame.display.update(); t += 1
pygame.quit()
