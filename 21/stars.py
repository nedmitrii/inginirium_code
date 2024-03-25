import random

import pygame

pygame.init()

FPS = 25
W, H = 500, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Starry Sky")


class Star:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.color = (255,) * 3

    def draw(self, root):
        if self.color[0] >= 0:
            pygame.draw.circle(root, self.color, (self.x, self.y), 5)
            self.color = (self.color[0] - 1,) * 3


stars = []
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for _ in range(5):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        pygame.draw.circle(win, (75,) * 3, (x, y), 1)
    if pygame.mouse.get_pressed()[0]:
        stars.append(Star())
    for s in stars:
        s.draw(win)
    if len(stars) > 0:
        if stars[0].color[0] < 0:
            stars.pop(0)
    pygame.display.update()
    clock.tick(FPS)
    print(len(stars))
