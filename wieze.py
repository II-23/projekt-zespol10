from typing import Any
import pygame as pg 
from stale import *
from sciezka import *
import math

class Wieza(pg.sprite.Sprite):
    def __init__ (self, image, mysz_x, mysz_y):
        pg.sprite.Sprite.__init__(self)

        self.zasieg = 75
        self.wybrana = False
        self.cel = None

        #pozycja
        self.mysz_x = mysz_x
        self.mysz_y = mysz_y
        self.x = (self.mysz_x + 0.5) * SIATKA
        self.y = (self.mysz_y + 0.5) * SIATKA

        #wyglad
        self.orig_image = image
        self.rect = self.orig_image.get_rect()
        self.rect.center = (self.x, self.y)
        self.zasieg_obraz = pg.Surface((self.zasieg * 2, self.zasieg * 2))
        self.zasieg_obraz.fill((0,0,0))
        self.zasieg_obraz.set_colorkey((0,0,0))
        pg.draw.circle(self.zasieg_obraz, (255, 255, 0), (self.zasieg, self.zasieg), self.zasieg)
        self.zasieg_obraz.set_alpha(89)
        self.zasieg_rect = self.zasieg_obraz.get_rect()
        self.zasieg_rect.center = self.rect.center

        #updatowanie wygladu
        self.angle = 90
        self.image = pg.transform.rotate(self.orig_image, self.angle)


    def postaw_wieze(mouse_pos, kursor_wieza, wieze):
        mouse_x = mouse_pos[0] // SIATKA
        mouse_y = mouse_pos[1] // SIATKA
        wieza = Wieza(kursor_wieza, mouse_x, mouse_y)
        if([mouse_x, mouse_y] not in koordynatySciezki):
            wieze.add(wieza)
    
    def draw(self, powierzchnia):
        self.image = pg.transform.rotate(self.orig_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        powierzchnia.blit(self.image, self.rect)
        if self.wybrana:
            powierzchnia.blit(self.zasieg_obraz, self.zasieg_rect)
    
    def wybierz_wieze(mouse_pos, wieze):
        mouse_x = mouse_pos[0] // SIATKA
        mouse_y = mouse_pos[1] // SIATKA
        for wieza in wieze:
            if(mouse_x, mouse_y) == (wieza.mysz_x, wieza.mysz_y):
                return wieza
            
    def usun_range(wieze):
        for wieza in wieze:
            wieza.wybrana = False

    def wybierz_cel(self, wrogowie):
        x = 0
        y = 0
        nowy_cel = None
        for wrog in wrogowie:
            x = wrog.pos[0] - self.x
            y = wrog.pos[1] - self.y
            dystans = math.sqrt(x ** 2 + y ** 2)
            if dystans < self.zasieg:
                nowy_cel = wrog
            self.cel = nowy_cel
            if nowy_cel is not None:
                self.angle = -math.degrees(math.atan2(y, x))
    
    def update(self, wrogowie):
        if self.cel == None:
            self.wybierz_cel(wrogowie)
        else:
            x = self.cel.pos[0] - self.x
            y = self.cel.pos[1] - self.y
            dystans = math.sqrt(x ** 2 + y ** 2)
            if (dystans > self.zasieg):
                self.cel = None
            else:
                self.angle = -math.degrees(math.atan2(y, x))

