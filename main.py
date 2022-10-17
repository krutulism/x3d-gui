import pygame
import sys
import numpy as np

def main():

    pygame.init()

    surface = pygame.display.set_mode([500, 500])

    running = True


    rect1 = pygame.Rect(20,40,60,80)
    rect2 = pygame.Rect(120,140,60,80)

    pygame.draw.rect(surface, (0,127,127),rect1)
    pygame.draw.rect(surface, (127,127,0), rect2)

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    pygame.draw.rect(surface, (255,0,0), rect1)
                    pygame.display.update(rect1)
                    pygame.draw.rect(surface, (255,0,0), rect2)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_g:
                    pygame.draw.rect(surface, (0,127,127), rect1)
                    pygame.display.update(rect1)
                    pygame.draw.rect(surface, (127,127,0), rect2)



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