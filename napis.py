import pygame

def pokaz_napis(screen,text,font,color, size,x,y):
    fnt = pygame.font.Font(font, size)


    txt = fnt.render(text, True, color)
    rect = txt.get_rect(center=(x,y))
    screen.blit(txt,rect)