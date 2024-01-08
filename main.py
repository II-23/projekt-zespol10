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
przycisk_Test = Przycisk(350, 200, 100, 50, "skip to the game (nie chce mi sie robic ciagle tej sciezki)")

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
        przycisk_Test.draw(screen)

    if game_status == KREATOR_SCIEZKI:
        screen.fill(WHITE)
        rysujSciezke(screen)

    if game_status == GRA:
        screen.fill(WHITE)
        rysujSciezke(screen)

        #aktualizuj grupy
        sojusznicy.update()

        #wyswietl grupy
        sojusznicy.draw(screen)

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
                        game_status = KREATOR_SCIEZKI
                    if przycisk_Wyjdz.klikniety(pygame.mouse.get_pos()):
                        przycisk_Wyjdz.akcje()
                        running = False
                    if przycisk_Test.klikniety(pygame.mouse.get_pos()):
                        game_status = GRA
                        continue

        #eventy w kreatorze sciezki
        if game_status == KREATOR_SCIEZKI:
            if event.type == pygame.MOUSEBUTTONDOWN:
                dodajKwadrat()
                wypelnienieSciezki()
            if czy_koniec_sciezki():
                game_status = GRA
                continue

        #eventy w grze
        if game_status == GRA:
            if event.type == pygame.MOUSEBUTTONDOWN:
                sojusznik = Sojusznik(pygame.mouse.get_pos(), sojusznik_image)
                sojusznicy.add(sojusznik)

        #eventy po zakonczeniu gry
        if game_status == GAME_OVER:
            pass

    #aktualizuj ekran
    pygame.display.flip()

pygame.quit()
sys.exit()
