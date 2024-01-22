from typing import Any
import pygame as pg 
from stale import *
from sciezka import *
import math
from wrogowie import Wrog
from game import *

class Wieza(pg.sprite.Sprite):
    def __init__ (self, image, mysz_x, mysz_y):
        pg.sprite.Sprite.__init__(self)

        # Specyfikajca wieży

        self.zasieg = 75
        self.wybrana = False
        self.cel = None
        self.koszt = 100

        # Pozycja wieży
        self.mysz_x = mysz_x
        self.mysz_y = mysz_y
        self.x = (self.mysz_x + 0.5) * SIATKA
        self.y = (self.mysz_y + 0.5) * SIATKA
        
        self.sound = pg.mixer.Sound("assets/audio/shot.wav")

        #wyglad
        self.sprite_sheet = image
        self.animation_list = self.zaladuj_zdjecie()
        self.index_klatki = 0
        self.update_time = pygame.time.get_ticks()
        
        self.orig_image = self.animation_list[0]
        self.rect = self.orig_image.get_rect()
        self.rect.center = (self.x, self.y)
        self.isAnimationOn = False
        
        # self.zasieg_obraz_strzal = self.zasieg_obraz
        
        # self.zasieg_obraz_strzal.fill((0,0,0))
        # self.zasieg_obraz_strzal.set_colorkey((0,0,0))
        
        # pg.draw.circle(self.zasieg_obraz_strzal, (0, 255, 0), (self.zasieg, self.zasieg), self.zasieg)
        # self.zasieg_obraz_strzal.set_alpha(150)
        
        # self.zasieg_rect = self.zasieg_obraz.get_rect()
        # self.zasieg_rect.center = self.rect.center
        
        # Wygląd zasięgu wieży
        self.zasieg_obraz = pg.Surface((self.zasieg * 2, self.zasieg * 2))
        self.zasieg_obraz.fill((0, 0, 0))
        self.zasieg_obraz.set_colorkey((0, 0, 0))
        pg.draw.circle(self.zasieg_obraz, (255, 255, 0), (self.zasieg, self.zasieg), self.zasieg)
        self.zasieg_obraz.set_alpha(100)
        self.zasieg_rect = self.zasieg_obraz.get_rect()
        self.zasieg_rect.center = self.rect.center
        
        #updatowanie wygladu
        self.angle = 90
        self.image = pg.transform.rotate(self.orig_image, self.angle)

        #do strzałów
        self.ostatni_strzal = 0
        self.interwal_strzalow = 500


    def postaw_wieze(mouse_pos, kursor_wieza, wieze, game):
        mouse_x = mouse_pos[0] // SIATKA
        mouse_y = mouse_pos[1] // SIATKA
        wieza = Wieza(kursor_wieza, mouse_x, mouse_y)
        for w in wieze:
            if ((w.mysz_x, w.mysz_y) == (wieza.mysz_x, wieza.mysz_y)):
                return
        if [mouse_x, mouse_y] not in koordynatySciezki and game.kasa >= 100:
            wieze.add(wieza)
            game.kasa -= wieza.koszt
    
    def draw(self, powierzchnia):
        self.image = pg.transform.rotate(self.orig_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        powierzchnia.blit(self.image, self.rect)
        if self.wybrana:
            powierzchnia.blit(self.zasieg_obraz, self.zasieg_rect)
    
    def strzal(self, wrogowie, game):
        teraz = pg.time.get_ticks()
        if teraz - self.ostatni_strzal >= self.interwal_strzalow:
            self.ostatni_strzal = teraz
            if self.cel is not None and self.cel.alive == True:
                self.cel.get_harmed(50, 'direct', wrogowie, game)
                self.isAnimationOn = True
                self.sound.play()
                #powierzchnia.blit(self.zasieg_obraz_strzal, self.zasieg_rect)

    
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
    
    def update(self, wrogowie, game):
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
                if self.cel.alive == False:
                    self.cel = None
                    
    def zaladuj_zdjecie(self):
        size = self.sprite_sheet.get_height()
        animation_list = []
        for x in range(8):
            temp_zdjecie = self.sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_zdjecie)
        return animation_list
    
    def wlacz_animacje(self):
        self.orig_image = self.animation_list[self.index_klatki]
        if self.isAnimationOn:
            if pygame.time.get_ticks() - self.update_time > ANIMATION_DELAY:
                self.update_time = pg.time.get_ticks()
                self.index_klatki += 1
                if self.index_klatki >= 8:
                    self.isAnimationOn = False
                    self.index_klatki = 0
