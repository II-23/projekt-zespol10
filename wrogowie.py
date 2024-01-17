import pygame as pg
from pygame.math import Vector2
import math
from dane_wrogow import DANE_WROGOW

class Wrog(pg.sprite.Sprite):
  def __init__(self,typ_wroga, waypoints, images):
    pg.sprite.Sprite.__init__(self)
    self.waypoints = waypoints
    self.pos = Vector2(self.waypoints[0])*50+[25,25]
    self.target_waypoint = 0

    #self.hp = DANE_WROGOW.get(typ_wroga)["hp"]
    #self.speed = DANE_WROGOW.get(typ_wroga)["speed"]

    # szybkość z jaką sie porusza w chyba pixelach na klatke
    self.speed = 1
    # sumaryczna ilość hp (flat int)
    self.hp = 100
    # % odporności na obrażenia fizyczne
    self.armour = 0
    # % odporności na obrażenia magiczne
    self.magic_res = 0

    self.alive=True
    self.istarget=False
    self.target=None

    self.angle = 0
    self.original_image = images.get(typ_wroga)
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos

  def update(self):
    self.move()
    self.rotate()

  def move(self):
    if(self.istarget==False):
      destination=self.waypoints[self.target_waypoint]
      self.destination = Vector2(destination)*50+[25,25]
    else:
      destination=self.target.position
      self.destination = Vector2(destination)
    # ustal jak ma sie poruszac jednostka, aby dotrzeć do celu
    self.movement = self.destination - self.pos
    # rusz jednostkę
    distance = self.movement.length()
    if distance != 0:
      if distance > self.speed:
        self.pos += (self.movement.normalize()) * self.speed
      else:
        self.pos += (self.movement.normalize()) * distance
    else:
      #czy doszedł
      if(len(self.waypoints)-1==self.target_waypoint):
        #worg umiera a my tracimy zycie
        self.alive=False
      else:
        self.target_waypoint+=1

  def rotate(self):
    distance = self.destination - self.pos
    self.angle = math.degrees(math.atan2(-distance[1], distance[0]))
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos

  def targeted(self,sojusznik):
    self.target=sojusznik
    self.istarget=True

  def get_harmed(self, dmg, type):
    if (type == 'magic'):
      self.hp = self.hp - (100 - self.magic_res) / 100 * dmg
    if (type == 'direct'):
      self.hp = self.hp - (100 - self.armour) / 100 * dmg
    if (self.hp <= 0):
      self.alive = False
