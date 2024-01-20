import pygame
import sys
from stale import *

#inicjalizuj pygame
pygame.init()

#stworz okno gry
screen = pygame.display.set_mode((WIDTH + PANEL_PRZYCISKI, HEIGHT))
pygame.display.set_caption('PWI - Tower Defense')


from przycisk import Przycisk
from sojusznicy import Sojusznik
from sciezka import *
from wieze import Wieza
from wrogowie import *
from game import Game
from przycisk_panel import PrzyciskPanel
import random
from napis import *



#zmienne
stawianie_wiez = False
wybrana_wieza = None

#zaladuj assety
bg = pygame.image.load('res/tlo/space.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (int(bg.get_width() * 0.19), int(bg.get_height() * 0.2)))
sojusznik_image = pygame.image.load('assets/images/enemies/enemy_1.png').convert_alpha()
kursor_wieza = pygame.image.load('res/wieze/wieza_1.png').convert_alpha()
nowe_wymiary = (200,200)
nowe_wymiary_2 = (130, 130)
kursor_wieza = pygame.transform.scale(kursor_wieza, nowe_wymiary_2)
wrog_image = {
    "a":    pygame.image.load('res/wrogowie/wrog1.png').convert_alpha(),
    "b":    pygame.image.load('res/wrogowie/wrog2.png').convert_alpha(),
    "c":    pygame.image.load('res/wrogowie/wrog3.png').convert_alpha(),
    "d":    pygame.image.load('res/wrogowie/wrog4.png').convert_alpha()
}
kup_wieze = pygame.image.load('res/przyciski/kup_wieze.png').convert_alpha()
kup_wieze = pygame.transform.scale(kup_wieze, nowe_wymiary)
cancel = pygame.image.load('res/przyciski/cancel.png').convert_alpha()
cancel = pygame.transform.scale(cancel, nowe_wymiary)

#       !!!stawianie wiezy powinno być funkcją clasy wierza!!!
#       !!! ok szefito, zmienione !!!



#stworz grupy
sojusznicy = pygame.sprite.Group()
wieze = pygame.sprite.Group()

sciezka = pygame.sprite.Group()
wrogowie = pygame.sprite.Group()
napisy = []

#wrogowei
czas_spawnu_wroga = pygame.time.get_ticks()


#zegar
clock = pygame.time.Clock()

#stworz przyciski
przycisk_Start = Przycisk(450, 300, 180, 80, "Start")
przycisk_Wyjdz = Przycisk(450, 400, 180, 80, "Wyjdz")
przycisk_Menu =  Przycisk(420, 500, 240, 80, "Wyjdz do menu")

przycisk_Wieza = PrzyciskPanel(WIDTH + 28, 170, kup_wieze, True)
przycisk_Cancel = PrzyciskPanel(WIDTH + 28, 230, cancel, True)

game_status = MENU
running = True

def restart_gry():

    print("restart!")

##################
# GLOWNA PETLA GRY
##################
while running:

    clock.tick(FPS)

    ###################################
    # WYSWIETLANIE ELEMENTOW NA EKRANIE
    ###################################

    if game_status == MENU:
        screen.blit(bg,(0,0))
        pokaz_napis(screen,"PWI - Tower Defense",'res/czcionki/FFFFORWA.TTF',(255,50,93),72,525,100)

        for przycisk in [przycisk_Start,przycisk_Wyjdz]:
            przycisk.draw(screen,pygame.mouse.get_pos())



    if game_status == KREATOR_SCIEZKI:
        screen.fill(BLACK)

        panel = pygame.Rect(WIDTH, 0, PANEL_PRZYCISKI, HEIGHT)
        screen.fill(BLUE, panel)
        rysujSciezke(screen)

        pokaz_napis(screen, "Narysuj trakt dla jednostek wroga", 'res/czcionki/FFFFORWA.TTF', WHITE, 16, 190,30)

    if game_status == GRA:

        screen.fill(BLACK)
        panel = pygame.Rect(WIDTH, 0, PANEL_PRZYCISKI, HEIGHT)
        screen.fill(BLUE, panel)
        pokaz_napis(screen, "HP: " + str(game.hp_gracza), 'res/czcionki/FFFFORWA.TTF', WHITE, 32, 950,40)
        pokaz_napis(screen, str(game.kasa) + " $", 'res/czcionki/FFFFORWA.TTF', WHITE, 32, 900, 90)
        rysujSciezke(screen)


        #wyswietl przyciski z boku
        if przycisk_Wieza.draw(screen):
            stawianie_wiez = True
        if stawianie_wiez == True:
            kursor_rect = kursor_wieza.get_rect()
            kursor_poz = pygame.mouse.get_pos()
            kursor_rect.center = kursor_poz
            if kursor_poz[0] < WIDTH:
                screen.blit(kursor_wieza, kursor_rect)
            if przycisk_Cancel.draw(screen):
                stawianie_wiez = False

        #aktualizuj grupy
        for i in sojusznicy:
            if(i.alive):
                i.update(wrogowie,game)
            else:
                sojusznicy.remove(i)

        for wrog in wrogowie:
            wrog.update(wrogowie,game)
        wieze.update(wrogowie, game)


        #wyswietl wieze
        for wieza in wieze:
            wieza.draw(screen)
            wieza.strzal(wrogowie, game)
        
        if wybrana_wieza:
            wybrana_wieza.wybrana = True

        #wyswietl grupy
        sojusznicy.draw(screen)
        wrogowie.draw(screen)
        for napis in napisy:
            napis.update(game,napisy,pygame.time.get_ticks())

        #spawnuj wrogow
        if game.czy_fala_idzie == True:
            random.seed(czas_spawnu_wroga)
            if pygame.time.get_ticks() - czas_spawnu_wroga > 500 + random.randint(1,300) : #500 to stun miedzy spawnowaniem kolejnych wrogow
                if game.spawned_enemies < len(game.enemy_list):
                    typ = game.enemy_list[game.spawned_enemies]

                    enemy = Wrog(typ, waypoints, wrog_image)
                    wrogowie.add(enemy)

                    game.spawned_enemies += 1
                    czas_spawnu_wroga = pygame.time.get_ticks()

        else:
            if len(napisy) == 0:
                n = Napis_czasowy(screen,"Fala " + str(game.wave),"res/czcionki/FFFFORWA.TTF","#603fef",80,400,300,40*FPS)
                napisy.append(n)



        
        #narysuj napisy
        pokaz_napis(screen, "Kup i postaw jednostki obronne,", 'res/czcionki/FFFFORWA.TTF', WHITE, 16, 190,
                    30)
        pokaz_napis(screen, "pokonaj mroczne poczwary!", 'res/czcionki/FFFFORWA.TTF', WHITE, 16, 180,
                    60)

        if game.win == -1:
            game_status = GAME_OVER

        elif game.win == 1:
            game_status = WIN

    if game_status == GAME_OVER:
        #rysuje wszystko ale nie update'uje
        screen.fill(BLACK)
        panel = pygame.Rect(WIDTH, 0, PANEL_PRZYCISKI, HEIGHT)
        screen.fill(BLUE, panel)
        pokaz_napis(screen, "HP: " + str(game.hp_gracza), 'res/czcionki/FFFFORWA.TTF', WHITE, 32, 950,40)
        pokaz_napis(screen, str(game.kasa) + " $", 'res/czcionki/FFFFORWA.TTF', WHITE, 32, 900, 90)
        rysujSciezke(screen)
        #wyswietl grupy
        sojusznicy.draw(screen)
        wrogowie.draw(screen)

        pokaz_napis(screen, "Koniec Gry", 'res/czcionki/FFFFORWA.TTF', "#d21f3c", 100, 550, 300)
        pokaz_napis(screen, "Kosmici zniszczyli wszystko...", 'res/czcionki/FFFFORWA.TTF', "#d21f3c", 48, 550, 420)

        przycisk_Menu.draw(screen,pygame.mouse.get_pos())

    if game_status == WIN:
        # rysuje wszystko ale nie update'uje
        screen.fill(BLACK)
        panel = pygame.Rect(WIDTH, 0, PANEL_PRZYCISKI, HEIGHT)
        screen.fill(BLUE, panel)
        pokaz_napis(screen, "HP: " + str(game.hp_gracza), 'res/czcionki/FFFFORWA.TTF', WHITE, 32, 950, 40)
        pokaz_napis(screen, str(game.kasa) + " $", 'res/czcionki/FFFFORWA.TTF', WHITE, 32, 900, 90)
        rysujSciezke(screen)
        # wyswietl grupy
        sojusznicy.draw(screen)
        wrogowie.draw(screen)

        pokaz_napis(screen, "Epicki Koniec!", 'res/czcionki/FFFFORWA.TTF', "#d21f3c", 100, 550, 300)
        pokaz_napis(screen, "Wiktoria na skale Uniwersum", 'res/czcionki/FFFFORWA.TTF', "#d21f3c", 48, 550, 420)

        przycisk_Menu.draw(screen, pygame.mouse.get_pos())

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

        #eventy w kreatorze sciezki
        if game_status == KREATOR_SCIEZKI:
            if event.type == pygame.MOUSEBUTTONDOWN:
                dodajKwadrat()
                wypelnienieSciezki()
            if czy_koniec_sciezki():
                game_status = GRA
                game = Game()
                game.process_enemies()

                continue

        #eventy w grze
        if game_status == GRA:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]<800:
                    sojusznik = Sojusznik(pygame.mouse.get_pos(), sojusznik_image)
                    sojusznicy.add(sojusznik)


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                mouse_pos = pygame.mouse.get_pos()
                #sprawdzam czy myszka jest na mapie
                if mouse_pos[0] < WIDTH and mouse_pos[1] < HEIGHT:
                    wybrana_wieza = None
                    Wieza.usun_range(wieze)
                    if stawianie_wiez == True:
                        Wieza.postaw_wieze(mouse_pos, kursor_wieza, wieze)
                    else:
                        wybrana_wieza = Wieza.wybierz_wieze(mouse_pos, wieze)





        #eventy po zakonczeniu gry
        if game_status == GAME_OVER:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if przycisk_Menu.klikniety(pygame.mouse.get_pos()):
                        przycisk_Menu.akcje()

                        #resetuje wszystkie wazne zmienne
                        # stworz grupy
                        sojusznicy = pygame.sprite.Group()
                        wieze = pygame.sprite.Group()

                        sciezka = pygame.sprite.Group()
                        wrogowie = pygame.sprite.Group()
                        napisy = []

                        # wrogowei
                        czas_spawnu_wroga = pygame.time.get_ticks()

                        game_status = MENU


        if game_status == WIN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if przycisk_Menu.klikniety(pygame.mouse.get_pos()):
                        przycisk_Menu.akcje()

                        #resetuje wszystkie wazne zmienne
                        # stworz grupy
                        sojusznicy = pygame.sprite.Group()
                        wieze = pygame.sprite.Group()

                        sciezka = pygame.sprite.Group()
                        wrogowie = pygame.sprite.Group()
                        napisy = []

                        # wrogowei
                        czas_spawnu_wroga = pygame.time.get_ticks()

                        game_status = MENU

    #aktualizuj ekran
    pygame.display.flip()



pygame.quit()
sys.exit()

