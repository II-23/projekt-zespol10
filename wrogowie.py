import pygame as pg
from pygame.math import Vector2
import math
from dane_wrogow import DANE_WROGOW
from game import Game

class Wrog(pg.sprite.Sprite):
  def __init__(self,typ_wroga, waypoints, images):
    pg.sprite.Sprite.__init__(self)
    self.waypoints = waypoints
    self.pos = Vector2(self.waypoints[0])*50+[25,25]
    self.target_waypoint = 0

    self.typ_wroga = typ_wroga
    #self.hp = DANE_WROGOW.get(typ_wroga)["hp"]
    #self.speed = DANE_WROGOW.get(typ_wroga)["speed"]

    # szybkość z jaką sie porusza w chyba pixelach na klatke
    self.speed = DANE_WROGOW[typ_wroga]["speed"]
    # sumaryczna ilość hp (flat int)
    self.hp = DANE_WROGOW[typ_wroga]["hp"]
    # % odporności na obrażenia fizyczne
    self.armour = DANE_WROGOW[typ_wroga]["armour"]
    # % odporności na obrażenia magiczne
    self.magic_res = DANE_WROGOW[typ_wroga]["magic resistance"]

    self.alive=True
    self.istarget=False
    self.target=None

    self.angle = 0
    self.original_image = images.get(typ_wroga)
    self.original_image = pg.transform.rotate(self.original_image,-90)
    self.original_image = pg.transform.scale(self.original_image, (int(self.original_image.get_width() * 2.5), int(self.original_image.get_height() * 2.5)))
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos

  def death(self,grupa,game):
    self.alive = False
    game.spawned_enemies -= 1
    game.enemy_list.remove(self.typ_wroga)
    grupa.remove(self)

    if(len(grupa) == 0):
      game.wave = min(game.wave + 1, game.max_wave)
      game.process_enemies()

  def update(self,grupa,game):
    self.move(grupa,game)
    self.rotate()

  def move(self,grupa,game):
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
      elif(self.istarget):
        # jak sojusznik i wróg stana na tym samym polu to wróg znika więc ma stac pole przed
        self.pos += (self.movement.normalize()) * (distance - 1)
      else:
        self.pos += (self.movement.normalize()) * distance
    else:
      #czy doszedł
      if(len(self.waypoints)-1==self.target_waypoint):
        #wrog umiera a my tracimy zycie
        self.death(grupa,game)
        #tutaj dodać tracenie życia przez gracza
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

  def get_harmed(self, dmg, type,grupa,game): #grupa to grupa wrogowie z maina
    if (type == 'magic'):
      self.hp = self.hp - (100 - self.magic_res) / 100 * dmg
    if (type == 'direct'):
      self.hp = self.hp - (100 - self.armour) / 100 * dmg
    if (self.hp <= 0):
      self.death(grupa,game)

