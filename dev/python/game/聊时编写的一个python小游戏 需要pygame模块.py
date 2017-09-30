
import sys
import pygame
import math
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("hahsdhf")
myfont = pygame.font.Font(None, 60)

color = 200,80,60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2

piece1 = False
piece2 = False
piece3 = False
piece4 = False

while True:
    for evevt in pygame.event.get():
        if evevt.type == QUIT:
            sys.exit()

        elif  evevt.type == KEYUP:

            if evevt.key == pygame.K_ESCAPE:
                sys.exit()
            elif evevt.key == pygame.K_1:
                piece1 = True
            elif evevt.key == pygame.K_2:
                piece2 = True
            elif evevt.key == pygame.K_3:
                piece3 = True
            elif evevt.key == pygame.K_4:
                piece4 = True

    # clean the screen
    screen.fill((0,0,200))

    # draw the four number
    textImage1 = myfont.render("1", True, color)
    screen.blit(textImage1, (x+radius/2-20, y-radius/2))
    textImage2 = myfont.render("2", True, color)
    screen.blit(textImage2, (x-radius/2, y-radius/2))
    textImage3 = myfont.render("3", True, color)
    screen.blit(textImage3, (x-radius/2, y+radius/2-20))
    textImage4 = myfont.render("4", True, color)
    screen.blit(textImage4, (x+radius/2-20, y+radius/2-20))

    # should the pieces be down
    if piece1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen, color, (x,y), (x+radius,y), width)
    if piece2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
    if piece3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
        pygame.draw.line(screen, color, (x,y), (x,y+radius), width)
    if piece4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x,y), (x,y+radius), width)
        pygame.draw.line(screen, color, (x,y), (x+radius,y), width)

    # is the pie finished?
    if piece1 and piece2 and piece3 and piece4:
        color = 0,250,0

    pygame.display.update()

