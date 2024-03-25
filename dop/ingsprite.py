import random

import pygame as pg

W, H = 500, 500
win = pg.display.set_mode((W, H))


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img


class Inginirium(pg.sprite.Sprite):
    def __init__(self, image, *group):
        super().__init__(*group)
        self.image = image
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)


all_sprites = pg.sprite.Group()
img = load_img("../ing.png")
for i in range(50):
    Inginirium(img, all_sprites)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    all_sprites.update()
    win.fill((255, 255, 255))
    all_sprites.draw(win)
    pg.display.update()
