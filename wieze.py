import pygame as pg 
from stale import *

class Wieza(pg.sprite.Sprite):
    def __init__ (self, image, mysz_x, mysz_y):
        pg.sprite.Sprite.__init__(self)
        self.mysz_x = mysz_x
        self.mysz_y = mysz_y
        self.x = (self.mysz_x + 0.5) * SIATKA
        self.y = (self.mysz_y + 0.5) * SIATKA
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)