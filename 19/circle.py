import random

import pygame

win = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.is_jump = False
        self.jump_counter = 30
    def move_by_keys(self):
        if self.is_jump == True:
            if self.jump_counter >= -30:
                self.y -= self.jump_counter
                self.jump_counter -= 1
            else:
                self.jump_counter = 30
                self.is_jump = False
                self.color = (
                    random.randrange(0, 256),
                    random.randrange(0, 256),
                    random.randrange(0, 256)
                )
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 6
        elif keys[pygame.K_DOWN]:
            self.y += 6
        if keys[pygame.K_RIGHT]:
            self.x += 6
        elif keys[pygame.K_LEFT]:
            self.x -= 6
        if keys[pygame.K_SPACE]:
            self.is_jump = True

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


circle1 = Circle(250, 455,(255, 255, 255), 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((0,0,0))
    circle1.move_by_keys()
    circle1.draw(win)
    pygame.display.update()
    pygame.time.delay(10)
