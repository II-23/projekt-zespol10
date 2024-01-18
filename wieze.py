import pygame as pg 
from stale import *
from sciezka import *

class Wieza(pg.sprite.Sprite):
    def __init__ (self, image, mysz_x, mysz_y):
        pg.sprite.Sprite.__init__(self)

        self.zasieg = 65
        self.wybrana = False

        #pozycja
        self.mysz_x = mysz_x
        self.mysz_y = mysz_y
        self.x = (self.mysz_x + 0.5) * SIATKA
        self.y = (self.mysz_y + 0.5) * SIATKA

        #wyglad
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.zasieg_obraz = pg.Surface((self.zasieg * 2, self.zasieg * 2))
        self.zasieg_obraz.fill((0,0,0))
        self.zasieg_obraz.set_colorkey((0,0,0))
        pg.draw.circle(self.zasieg_obraz, (255, 255, 0), (self.zasieg, self.zasieg), self.zasieg)
        self.zasieg_obraz.set_alpha(89)
        self.zasieg_rect = self.zasieg_obraz.get_rect()
        self.zasieg_rect.center = self.rect.center


    def draw(self, powierzchnia):
        powierzchnia.blit(self.image, self.rect)
        powierzchnia.blit(self.zasieg_obraz, self.zasieg_rect)

    def postaw_wieze(mouse_pos, kursor_wieza, wieze):
        mouse_x = mouse_pos[0] // SIATKA
        mouse_y = mouse_pos[1] // SIATKA
        wieza = Wieza(kursor_wieza, mouse_x, mouse_y)
        if([mouse_x, mouse_y] not in koordynatySciezki):
            wieze.add(wieza)
    
    def wybierz_wieze(mouse_pos, wieze):
        mouse_x = mouse_pos[0] // SIATKA
        mouse_y = mouse_pos[1] // SIATKA
        for wieza in wieze:
            if(mouse_x, mouse_y) == (wieza.mysz_x, wieza.mysz_y):
                return wieza
