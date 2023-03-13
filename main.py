import os

import pygame

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

x = 20
y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
W = 500
H = 500
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Множество Жюлиа")
sc.fill(BLACK)

FPS = 30
clock = pygame.time.Clock()

c = complex(-0.2, 0.75)
P = 200
scale = P / 2
n_iter = 100
for y in range(-P, P):
    for x in range(-P, P):
        a = x / scale
        b = y / scale
        z = complex(a, b)
        for n in range(n_iter):
            z = z**2 + c
            if abs(z) > 2:
                break
        else:
           # sc.set_at((x + P, y + P), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            sc.set_at((x + P, y + P), (255, 120, 225))
            #pygame.draw.circle(sc,BLACK, (x + P, y + P), 0)
            pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

pygame.display.update()
clock.tick(FPS)
