import pygame
import random
from dane_wrogow import DANE_FAL
from napis import *

class Game():
    def __init__(self):
        self.hp_gracza = 1000
        self.kasa = 1000
        self.wave = 1
        self.max_wave = len(DANE_FAL)
        self.enemy_list = []
        self.spawned_enemies = 0
        self.czy_fala_idzie = False
        self.win = 0 #0 - wciaz gra -1 - przegral 1 - wygral

    def end(self): #zakończ gre pozytywnie
        self.win = 1

    def new_wave(self):
        self.czy_fala_idzie = False
        self.wave += 1
        if self.wave <= self.max_wave:
            self.process_enemies()
        else:
            print("Wiktoria")
            self.win = 1

    def process_enemies(self):
        enemies = DANE_FAL[self.wave-1]
        for enemy_type in enemies.keys():
            for enemy in range(enemies[enemy_type]):
                self.enemy_list.append(enemy_type)
        random.shuffle(self.enemy_list)


