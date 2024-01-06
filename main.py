import pygame
import sys
from przycisk import Przycisk
from sojusznicy import Sojusznik
from stale import *
from sciezka import *

#inicjalizuj pygame
pygame.init()

#stworz okno gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gra')

#zaladuj assety
sojusznik_image = pygame.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

#stworz grupy
sojusznicy = pygame.sprite.Group()
sojusznik = Sojusznik((0,100),sojusznik_image)
sojusznicy.add(sojusznik)

sciezka = pygame.sprite.Group()

#zegar
clock = pygame.time.Clock()

#stworz przyciski
przycisk_Start = Przycisk(350, 100, 100, 50, "Start")
przycisk_Wyjdz = Przycisk(350, 150, 100, 50, "Wyjdz")

game_status = MENU
running = True

##################
# GLOWNA PETLA GRY
##################

while running:

    clock.tick(FPS)

    ###################################
    # WYSWIETLANIE ELEMENTOW NA EKRANIE
    ###################################

    if game_status == MENU:
        screen.fill(WHITE)
        przycisk_Start.draw(screen)
        przycisk_Wyjdz.draw(screen)

    if game_status == GRA:
        screen.fill(WHITE)
        rysujSciezke(screen)

        #wyswietl grupy
        sojusznicy.draw(screen)
        sojusznik.move()

    ######################
    # ZARZADZANIE EVENTAMI
    ######################
    for event in pygame.event.get():

        #wyjscie z gry przez wcisniecie x
        if event.type == pygame.QUIT:
            running = False

        #eventy w menu
        if game_status == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if przycisk_Start.klikniety(pygame.mouse.get_pos()):
                        przycisk_Start.akcje()
                        game_status = GRA
                    if przycisk_Wyjdz.klikniety(pygame.mouse.get_pos()):
                        przycisk_Wyjdz.akcje()
                        running = False

        #eventy w grze
        if game_status == GRA:
            if event.type == pygame.MOUSEBUTTONDOWN:
                dodajKwadrat()
                wypelnienieSciezki()

        #eventy po zakonczeniu gry
        if game_status == GAME_OVER:
            pass

    #aktualizuj ekran
    pygame.display.flip()

pygame.quit()
sys.exit()
