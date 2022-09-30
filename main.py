import pygame
import sys
import numpy as np

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True


while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    



    pygame.display.flip()



class Panel(pygame.Rect):
    def __init__(self, dimensions, position, label, value):
        self.pos = position
        self.dims = dimensions
        self.label = label
        self.value = value
    
    

