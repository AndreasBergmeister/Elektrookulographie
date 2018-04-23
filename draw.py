import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300), pygame.FULLSCREEN)
color = (0, 128, 255)
position = (100, 100)
radius = 10

while True:
    pygame.draw.circle(screen, color, position, radius)
