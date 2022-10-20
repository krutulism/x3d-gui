import pygame
import sys
import numpy as np

def main():

    pygame.init()

    W = 800
    H = 600

    surface = pygame.display.set_mode([W, H])
    pygame.display.set_caption("X3D GUI")

    myfont = pygame.freetype.SysFont('Helvetica', 11)
    text = "Hello World"
    textSize = 11

    textRect = myfont.get_rect(text, size = textSize)
    textRect.center = (W // 2, H // 2)

    myfont.render_to(surface, textRect, text, (0,0,255), size=textSize)



    running = True
    # rect1 = pygame.Rect(20,40,60,80)
    # rect2 = pygame.Rect(120,140,60,80)

    # pygame.draw.rect(surface, (0,127,127),rect1)
    # pygame.draw.rect(surface, (127,127,0), rect2)

    drawPanes(surface)

    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN: pass
                # if event.key == pygame.K_g:
                #     pygame.draw.rect(surface, (255,0,0), rect1)
                #     pygame.display.update(rect1)
                #     pygame.draw.rect(surface, (255,0,0), rect2)
                #     pygame.display.update(rect2)
            elif event.type == pygame.KEYUP: pass
                # if event.key == pygame.K_g:
                #     pygame.draw.rect(surface, (0,127,127), rect1)
                #     pygame.display.update(rect1)
                #     pygame.draw.rect(surface, (127,127,0), rect2)
                #     pygame.display.update(rect2)

def drawPanes(surface, font):
    #Coordinates to help draw grid of indicators
    hBtn = [*range(10,561,50)]
    vBtn = 60
    btnDims = (200, 30)
    hAx = [80, 200, 320, 440]
    vAx = 320
    axDims = (160, 80)
    hHat = [180, 270, 360]
    vHat = [530, 615, 700]
    hatDims = (60, 60)

    btnPanes = []
    for i in range(0,len(hBtn)):
        rect = pygame.Rect(vBtn, hBtn[i], btnDims[0], btnDims[1])
        btnPanes.append(rect)
        pygame.draw.rect(surface, (127,127,0), rect)

    axPanes = []
    for i in range(0,len(hAx)):
        rect = pygame.Rect(vAx, hAx[i], axDims[0], axDims[1])
        axPanes.append(rect)
        pygame.draw.rect(surface, (127,127,0), rect)

    hatPanes = []
    for i in range(0,3):
        for j in range(0,3):
            rect = pygame.Rect(vHat[i], hHat[j], hatDims[0], hatDims[1])
            hatPanes.append(rect)
            pygame.draw.rect(surface, (0, 127, 127), rect)


if __name__=='__main__':
    main()