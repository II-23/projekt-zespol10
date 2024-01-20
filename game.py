import pygame
import random
from dane_wrogow import DANE_FAL

class Game():
    def __init__(self):

        self.wave = 1
        self.max_wave = len(DANE_FAL)
        self.enemy_list = []
        self.spawned_enemies = 0


    def process_enemies(self):
        enemies = DANE_FAL[self.wave-1]
        for enemy_type in enemies.keys():
            for enemy in range(enemies[enemy_type]):
                self.enemy_list.append(enemy_type)
        random.shuffle(self.enemy_list)