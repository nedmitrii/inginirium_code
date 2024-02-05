from math import sqrt

import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
x = 0
y = 0
color = (0, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # if (x > 400 or x < 100) or (y < 100 or y > 400):
    win.fill((255, 255, 255))
    pygame.draw.circle(win, color, (x, y), 25)
    if 25 < y < 475 and x > 25 and x < 475:
        if sqrt((250 - x) ** 2 + (250 - y) ** 2) > 150:
            h = 1
            color = (255, 0, 0)
        else:
            h = 3
            color = (0, 0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 3
        elif keys[pygame.K_DOWN]:
            y += 3
        elif keys[pygame.K_RIGHT]:
            x += 3
        elif keys[pygame.K_LEFT]:
            x -= 3
        else:
            if 250 - x > 0:
                x += h
            if 250 - x < 0:
                x -= h
            if 250 - y > 0:
                y += h
            if 250 - y < 0:
                y -= h
    else:
        pygame.draw.line(win, (0, 0, 0), (x + 17, y + 17), (x - 17, y - 17), 2)
        pygame.draw.line(win, (0, 0, 0), (x - 17, y + 17), (x + 17, y - 17), 2)

    space = pygame.key.get_pressed()
    if space[pygame.K_SPACE]:
        x = 250
        y = 250

    pygame.display.update()
    pygame.time.delay(10)
