import pygame
import math

class Ball:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 200
        self.xVel = -self.speed
        self.yVel = self.speed
        self.rec = pygame.Rect(x, y, w, h)
        self.__tick = 0

    def __reset(self):
        self.x = pygame.display.get_surface().get_width() / 2 - self.w / 2
        self.y = pygame.display.get_surface().get_height() / 2 - self.h / 2
        self.yVel = self.speed
        self.xVel = -self.xVel
    
    def update(self, dt, players, score):
        self.__tick += 1

        self.x += self.xVel * dt
        self.y += self.yVel * dt

        if self.y < 0 or self.y + self.h > pygame.display.get_surface().get_height():
            self.yVel = -self.yVel
        
        if self.x < 0 :
            self.__reset()
            score.update(1)

        if self.x + self.w > pygame.display.get_surface().get_width():
            self.__reset()
            score.update(2)
        
        if self.rec.colliderect(players[0].rec):
            self.xVel = -self.speed

        if self.rec.colliderect(players[1].rec):
            self.xVel = self.speed

        if math.floor(self.__tick) % 500 == 0:
            self.speed += 5
            print(f"Speed Up! {self.speed}")

    def draw(self, win):
        self.rec = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.ellipse(win, (200, 200, 200), self.rec)