import pygame
import sys
from przycisk import Przycisk

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main')

black = (0, 0, 0)
white = (255, 255, 255)

przycisk_Start = Przycisk(350, 100, 100, 50, "Start")
przycisk_Wyjdz = Przycisk(350, 150, 100, 50, "Wyjdz")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if przycisk_Start.czy_klikniety(pygame.mouse.get_pos())==1:
                    przycisk_Start.akcje()
                if przycisk_Wyjdz.czy_klikniety(pygame.mouse.get_pos())==1:
                    przycisk_Wyjdz.akcje()
                    running=False

    screen.fill(white)
    przycisk_Start.draw(screen)
    przycisk_Wyjdz.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()