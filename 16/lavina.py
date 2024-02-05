import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
x = 0
y = 0
e = int(input())
dirx = [i for i in range(1, e+1)]
x = [1]*e
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for i in range(e):
        if x[i] > 475:
            dirx[i] = -1*(i+1)
        if x[i] < 0:
            dirx[i] = 1*(i+1)
        x[i] += dirx[i]
        pygame.draw.circle(win, (0, 0, 0), (x[i], (500//e)*i), 25)
    pygame.display.update()

    win.fill((255,255,255))
    pygame.time.delay(20)
