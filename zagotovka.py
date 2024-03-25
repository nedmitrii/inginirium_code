import pygame

pygame.init()

FPS = 60
W, H = 500, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(FPS)
