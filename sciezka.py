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
waypoints = [[12,0]]
kwadrat1 = Kwadrat((255, 0, 0), siatka, waypoints[0][1], waypoints[0][0])
sciezka.add(kwadrat1)
kwadrat1 = Kwadrat((255, 0, 0), siatka, 9, 0)
sciezka.add(kwadrat1)

def dodajKwadrat():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // siatka
    row = mouse_y // siatka

    if (waypoints[-1][0]==col or waypoints[-1][1]==row) and [col,row] not in waypoints and [0,9] not in waypoints:
        waypoints.append([col, row])
        print(waypoints)
        kwadrat = Kwadrat((255, 0, 0), siatka, row, col)
        sciezka.add(kwadrat)

def wypelnienieSciezki():
    for i in range(len(waypoints) - 1):
        start_col, start_row = waypoints[i]
        end_col, end_row = waypoints[i + 1]

        if start_row == end_row:
            for col in range(min(start_col, end_col), max(start_col, end_col) + 1):
                kwadrat = Kwadrat((255, 0, 0), siatka, start_row, col)
                sciezka.add(kwadrat)

        elif start_col == end_col:
            for row in range(min(start_row, end_row), max(start_row, end_row) + 1):
                kwadrat = Kwadrat((255, 0, 0), siatka, row, start_col)
                sciezka.add(kwadrat)    
        
    if [0,9] in waypoints:
        print("Pelna sciezka")

def rysujSciezke(screen):
    sciezka.draw(screen)
    sciezka.update()