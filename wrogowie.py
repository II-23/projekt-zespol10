import pygame as pg

class Wrog(pg.sprite.Sprite):
  def __init__(self, pos, image):
    pg.sprite.Sprite.__init__(self)
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def update(self):
    self.move()
  def move(self):
    self.rect.x += 1