import pygame

pygame.init()
n = int(input())
if n % 1 == 0:
    win = pygame.display.set_mode((300, 300))
    win.fill((255, 255, 255))
    pygame.display.update()
    for i in range(0,300//2,300 // (2*n)):
        pygame.draw.ellipse(win, (0, 0, 0), (i, 0, 300 - i * 2, 300), 1)
        pygame.draw.ellipse(win, (0, 0, 0), (0, i, 300, 300 - i * 2), 1)
    pygame.display.update()
else:
    print("Неправильный формат ввода!")
    exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
