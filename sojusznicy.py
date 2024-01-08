import pygame as pg
from stale import *
from pygame.math import Vector2
import math

class Sojusznik(pg.sprite.Sprite):
    def __init__(self, position, image):
        pg.sprite.Sprite.__init__(self)
        self.position = position

        self.speed = 2

        self.angle = 0
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        if not self.is_already_spawned(self.position):
            self.spawn()
        self.rotate()

    def move(self, destination):
        self.destination = Vector2(destination)
        #ustal jak ma sie poruszac jednostka, aby dotrzeć do celu
        self.movement = self.destination - self.position
        #rusz jednostkę
        distance = self.movement.length()
        if distance != 0:
            if distance > self.speed:
                self.position += (self.movement.normalize()) * self.speed
            else:
                self.position += (self.movement.normalize()) * distance

    #wyszukuje najblizszy spawn point dla podanej pozycji
    def nearest_spawn_point(self, position):
        distances = []
        for spawn_point in ALLIES_SPAWN_POINTS:
            spawn_point = Vector2(spawn_point)
            movement = spawn_point - position
            distance = movement.length()
            distances.append(distance)
        id = distances.index(min(distances))
        return ALLIES_SPAWN_POINTS[id]

    #jednostka po postawieniu idzie do najblizszego spawn pointu
    def spawn(self):
        self.move(self.nearest_spawn_point(self.position))

    def is_already_spawned(self,position):
        if position in ALLIES_SPAWN_POINTS:
            return True
        return False

    #obraca jednostke tak aby patrzyla sie w strone w ktora idzie
    def rotate(self):
        distance = self.destination - self.position
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def attack(self):
        pass
