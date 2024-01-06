import pygame as pg

class Sojusznik(pg.sprite.Sprite):
    def __init__(self, pozycja, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pozycja

    def move(self):
        self.rect.x += 1