import pygame
import sys
from przycisk import Przycisk
from stale import *
from sciezka import *

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main')

przycisk_Start = Przycisk(350, 100, 100, 50, "Start")
przycisk_Wyjdz = Przycisk(350, 150, 100, 50, "Wyjdz")

sciezka = pygame.sprite.Group()

game_status=MENU
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if przycisk_Start.czy_klikniety(pygame.mouse.get_pos())==1 and game_status==MENU:
                    przycisk_Start.akcje()
                    game_status=GRA
                if przycisk_Wyjdz.czy_klikniety(pygame.mouse.get_pos())==1 and game_status==MENU:
                    przycisk_Wyjdz.akcje()
                    running=False
            
            if game_status == GRA:
                dodajKwadrat()

    if game_status==MENU:
        screen.fill(white)
        przycisk_Start.draw(screen)
        przycisk_Wyjdz.draw(screen)
    else:
        screen.fill(white)
        rysujSciezke(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()