import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Przycisk:
    def __init__(self, x, y, szerokosc, wysokosc, text_input):
        self.rect=pygame.Rect(x, y, szerokosc, wysokosc)
        self.color=WHITE
        self.font = pygame.font.Font('res/czcionki/FFFFORWA.TTF', 48)
        self.text_input=text_input


        self.base_color = WHITE
        self.hovering_color = (255,53,90)

        #self.text = self.font.render(self.text_input, True, self.base_color)

    def zmien_kolor(self, position):

        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return self.font.render(self.text_input, True, self.hovering_color)
        else:
            return self.font.render(self.text_input, True, self.base_color)

    def draw(self, surface,position):
        #pygame.draw.rect(surface, self.color, self.rect)

        text = self.zmien_kolor(position)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)



    def klikniety(self, pos):
        return self.rect.collidepoint(pos)
    
    def akcje(self):
        print("Klikniety przycisk " + self.text_input)
