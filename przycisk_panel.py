import pygame as pg 

class PrzyciskPanel():
    def __init__(self, x, y, obraz, klikniety_raz):
        self.obraz = obraz
        self.rect = self.obraz.get_rect()
        self.rect.topleft = (x,y)
        self.klikniety = False
        self.klikniety_raz = klikniety_raz
    
    def draw(self, powierzchnia):
        czynny = False
        poz = pg.mouse.get_pos()

        if self.rect.collidepoint(poz):
            if pg.mouse.get_pressed()[0] == 1 and self.klikniety == False:
                czynny = True
                if self.klikniety_raz:
                    self.klikniety = True
        if pg.mouse.get_pressed()[0] == 0:
            self.klikniety = False
    
        powierzchnia.blit(self.obraz, self.rect)

        return czynny
