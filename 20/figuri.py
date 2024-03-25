from random import choice, randint, choices, random

import pygame

win = pygame.display.set_mode((500, 500))


class Figura:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.col = col
        self.dir = [random(), random()]

    def move(self):
        self.x += self.dir[0] * 3
        self.y -= self.dir[1] * 3
        if self.x > 500 or self.x < 0:
            self.dir[0] *= -1
        if self.y > 500 or self.y < 0:
            self.dir[1] *= -1

    def draw(self, root):
        pygame.draw.polygon(root, self.col, ((self.x, self.y),))


class Circle(Figura):
    def __init__(self, x, y, col, rad):
        super().__init__(x, y, col)
        self.rad = rad

    def draw(self, root):
        pygame.draw.circle(root, self.col, (self.x, self.y), self.rad)


class Rect(Figura):
    def __init__(self, x, y, col, w, h):
        super().__init__(x, y, col)
        self.w = w
        self.h = h

    def draw(self, root):
        pygame.draw.rect(root, self.col, (self.x, self.y, self.w, self.h))


objects = [choice((
    Circle(randint(0, 500), randint(0, 500), choices(range(256), k=3), randint(15, 30)),
    Rect(randint(0, 500), randint(0, 500), choices(range(256), k=3), randint(10, 50), randint(10, 50))
)) for _ in range(24)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    for figura in objects:
        figura.draw(win)
        figura.move()
    pygame.display.update()
    pygame.time.delay(10)
