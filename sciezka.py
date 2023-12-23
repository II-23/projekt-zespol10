import pygame
from stale import *

class Kwadrat(pygame.sprite.Sprite):
    def __init__(self, color, size, row, col):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (col * size, row * size)

sciezka = pygame.sprite.Group()

def dodajKwadrat():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // siatka
    row = mouse_y // siatka
            
    kwadrat = Kwadrat((255, 0, 0), siatka, row, col)
    sciezka.add(kwadrat)    

def rysujSciezke(screen):
    sciezka.draw(screen)
    sciezka.update()