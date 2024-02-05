import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
x = 0
y = 0
x2 = 0
y2 = 0
x3 = 500
y3 = 0
dirx = 1
diry = 1
dirx2 = 1
diry2 = 1
dirx3 = -1
diry3 = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = x + dirx
    if x > 475:
        dirx = -1
    if x < 0:
        dirx = 1
    x2 = x2 + dirx2
    y2 = y2 + diry2
    if x2 > 475 and y2 > 475:
        dirx2 = -1
        diry2 = -1
    if x2 < 25 and y2 < 25:
        dirx2 = 1
        diry2 = 1
    x3 = x3 + dirx3
    y3 = y3 + diry3
    if x3 > 0 and y3 > 475:
        dirx3 = 1
        diry3 = -1
    if x3 > 475 and y3 < 25:
        dirx3 = -1
        diry3 = 1
    y = y+diry
    if y > 475:
        diry = -1
    if y < 25:
        diry = 1
    win.fill((255,255,255))
    pygame.draw.circle(win, (0,0,0), (250,y), 25)
    pygame.draw.circle(win, (0, 0, 0), (x2, y2), 25)
    pygame.draw.circle(win, (0, 0, 0), (x3, y3), 25)
    pygame.draw.rect(win, (0, 0, 0), (x,250,25,25))
    pygame.display.update()
    pygame.time.delay(3)