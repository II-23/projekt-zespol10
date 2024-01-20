import pygame
import game



def pokaz_napis(screen,text,font,color, size,x,y):
    fnt = pygame.font.Font(font, size)


    txt = fnt.render(text, True, color)
    rect = txt.get_rect(center=(x,y))
    screen.blit(txt,rect)

class Napis_czasowy():
    def __init__(self, screen,text,font,color,size,x,y,duration):
        self.screen = screen
        self.text = text
        self.font = font
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.duration = duration
        self.czas_powstania = pygame.time.get_ticks()

    def update(self,game,grupa,aktualny_czas):
        if aktualny_czas - self.czas_powstania < self.duration:
            pokaz_napis(self.screen,self.text,self.font,self.color,self.size,self.x,self.y)
        else:
            game.czy_fala_idzie = True
            grupa.remove(self)

