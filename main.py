import pygame
import sys
import numpy as np

def main():

    pygame.init()

    surface = pygame.display.set_mode([500, 500])

    running = True


    rect = pygame.Rect(20,40,60,80)
    pygame.draw.rect(surface, (0,127,127),rect)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            

        



        pygame.display.flip()



class Panel(pygame.Rect):
    def __init__(self, pos, dims, label, value, baseColor, activeColor):
        super().__init__(pos, dims)
        self.label = label
        self.value = value
        self.baseColor = baseColor
        self.activeColor = activeColor
        self.color = baseColor

    def depressed(self):
        pass

if __name__=='__main__':
    main()