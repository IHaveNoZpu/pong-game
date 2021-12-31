import pygame

class Score:
    def __init__(self):
        self.__font = pygame.font.Font('freesansbold.ttf', 32)
        self.__color = (200,200,200)
        self.p1 = 0
        self.p2 = 0
    
    def update(self, p):
        if p == 1:
            self.p1 += 1
        if p == 2:
            self.p2 += 1

    def draw(self, win):
        text = self.__font.render(str(self.p1), False, self.__color)
        textB = self.__font.render(str(self.p2), False, self.__color)
        win.blit(text, (pygame.display.get_surface().get_width() / 2.2, 20))
        win.blit(textB, (pygame.display.get_surface().get_width() / 1.925, 20))