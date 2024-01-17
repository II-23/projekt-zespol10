import pygame as pg
from stale import *
from pygame.math import Vector2
import math

class Sojusznik(pg.sprite.Sprite):
    def __init__(self, position, image):
        pg.sprite.Sprite.__init__(self)
        self.position = position

        #staty zawodnika (basic)
        # szybkość z jaką sie porusza w chyba pixelach na klatke
        self.speed = 2
        # sumaryczna ilość hp (flat int)
        self.hp=100
        # % odporności na obrażenia fizyczne
        self.armour=0
        # % odporności na obrażenia magiczne
        self.magic_res=0
        # zasięg w jakim szuka wrogów (promień okręgu w którym ich szuka) w pixelach
        self.radius=25
        # mam nadzieje że ułatwienie kiedy sojusznik umiera po prostu zmienia się alive na False i usunie się go z listy sojuszników
        # ewentualnie można zrobić custom event jako ally_died i on by to robił ale no
        self.alive=True


        self.angle = 0
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self,enemy_sprite_group):
        if not self.is_already_spawned(self.position):
            self.spawn()
        self.rotate()
        target=self.serch_target(enemy_sprite_group)
        if(target==None):
            # nie ma wroga w pobliżu
            pass
        else:
            self.attack(target)

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

    def get_harmed(self,dmg,type):
        if(type=='magic'):
            self.hp=self.hp-(100-self.magic_res)/100*dmg
        if(type=='direct'):
            self.hp=self.hp-(100-self.armour)/100*dmg
        if(self.hp<=0):
            self.alive=False
        pass
    def serch_target(self,enemy_sprite_group):
        # iteracja po wszystkich wrogach i sprawdzenie czy są w odpowiendniej odległości
        for ene in enemy_sprite_group:
            distance=ene.pos - self.position
            # warunek czy wróg znajduje sie w okręgu wyznaczonym przez self.radius i środku w self.position
            if(distance[0]**2+distance[1]**2<=self.radius):
                # tu przydała by się jakaś funkcja wroga typu tageted żeby przestał iść do waypointa tylko zaczął do sojusznika i zaczeli się bić np ene.targeted(sojusznik)
                ene.targeted(self)
                # Jeśli jakiegoś napotka będzie do niego podchodził
                return ene
        return None
    def attack(self,target):
        #musi jakos sie odwolac do danego wroga...
        print('uderzylem go')
        pass
