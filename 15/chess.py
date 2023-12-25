import pygame
pygame.init()
s = input().split()
pygame.display.set_caption("Шахматное поле")

if len(s) == 2 and s[0].isnumeric() and s[1].isnumeric():
    a = int(s[0])
    n = int(s[1])
else:
    print("Неправильный формат ввода!")
    exit()
if a % n == 0:
    win = pygame.display.set_mode((a, a))
    win.fill((255, 255, 255))
    pygame.display.update()
    for i in range(n):
        for j in range (n):
            if (i+j) % 2 == 0:
                pygame.draw.rect(win, (0, 0, 0), (i*a//n,j*a//n,a//n,a//n))
    pygame.display.update()
else:
    print("Неправильный формат ввода!")
    exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
