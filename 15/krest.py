import pygame
pygame.init()
s= input().split()
pygame.display.set_caption("Крест")

if len(s) == 2 and s[0].isnumeric() and s[1].isnumeric():
    w = int(s[0])
    h = int(s[1])
else:
    print("Неправильный формат ввода!")
    exit()

win = pygame.display.set_mode((w, h))
win.fill((12, 12, 12))
pygame.draw.line(win, (255, 255, 255), (0, 0), (w, h), 5)
pygame.draw.line(win, (255, 255, 255), (w, 0), (0, h), 5)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
