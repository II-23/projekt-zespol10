import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Przycisk:
    def __init__(self, x, y, szerokosc, wysokosc, text):
        self.rect=pygame.Rect(x, y, szerokosc, wysokosc)
        self.color=WHITE
        self.text=text

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def czy_klikniety(self, pos):
        return self.rect.collidepoint(pos)
    
    def akcje(self):
        print("Klikniety przycisk " + self.text)