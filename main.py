# Imports
import pygame
import sys

from Games.ball import Ball
from Games.player import Player
from Games.score import Score

# Init
pygame.init()

# Settings and setup windows
fps = 60
width = 700
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Main
def main():
    clock = pygame.time.Clock()
    ball = Ball(width / 2 - 7.5, height / 2 - 7.5, 15, 15)
    players = [Player(width - 20, height / 2 - 50, 10, 100), Player(10, height / 2 - 50, 10, 100)]
    score = Score()

    while True:
        dt = clock.tick(fps)
        win.fill(pygame.Color("grey12"))

        # Event Handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Visuals
        ball.draw(win)
        pygame.draw.aaline(win, (200, 200, 200), (width / 2, 0), (width / 2, height))
        for ply in players:
            ply.draw(win)
        score.draw(win)

        # Player Control
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_d]:
            players[0].move(dt / 1000, False)

        if keys[pygame.K_s] or keys[pygame.K_f]:
            players[0].move(dt / 1000, True)

        if keys[pygame.K_UP] or keys[pygame.K_j]:
            players[1].move(dt / 1000, False)

        if keys[pygame.K_DOWN] or keys[pygame.K_k]:
            players[1].move(dt / 1000, True)

        # Update
        ball.update(dt / 1000, players, score)
        pygame.display.update()

# Run
if __name__ == "__main__":
    main()