import pygame

class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 500
        self.rec = pygame.Rect(x, y, w, h)
    
    def move(self, dt, x):
        if x:
           self.y += self.vel * dt
        else:
            self.y -= self.vel * dt
        
        if self.y < 0:
            self.y = 0
        if self.y + self.h > pygame.display.get_surface().get_height():
            self.y = pygame.display.get_surface().get_height() - self.h

    def draw(self, win):
        self.rec = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win, (200, 200, 200), self.rec)