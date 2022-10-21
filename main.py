import pygame
import sys
import numpy as np

def main():

    pygame.init()

    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    j = joysticks[0]
    j.init()
    print(j.get_name())

    W = 800
    H = 600
    surface = pygame.display.set_mode([W, H])
    pygame.display.set_caption("X3D GUI")
    myfont = pygame.freetype.SysFont('Helvetica', 11)

    running = True

    btnPanes, btnLabels, axisPanes, axisLabels, hatPanes, hatLabels = drawPanes(surface, myfont)

    pygame.display.update()

    while running:
        updateRects = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.JOYBUTTONDOWN:
                b = event.button
                pane = btnPanes[b]
                print(f'Button {b+1} depressed')
                pygame.draw.rect(surface, (0,255,0), pane)
                updateRects.append(pane)

            elif event.type == pygame.JOYBUTTONUP:pass

            elif event.type == pygame.JOYAXISMOTION:pass


            elif event.type == pygame.JOYHATMOTION:pass

        pygame.display.update(updateRects)

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

    textSize = 14

    btnPanes = []
    btnLabels = []
    for i in range(0,len(hBtn)):
        rect = pygame.Rect(vBtn, hBtn[i], btnDims[0], btnDims[1])
        btnPanes.append(rect)
        pygame.draw.rect(surface, (127,127,0), rect)

        text = f'Button  {i+1}'
        btnLabels.append(text)
        drawLabel(surface, font, rect.center,  text, textSize)

    axisPanes = []
    axisLabels = []
    for i in range(0,len(hAx)):
        rect = pygame.Rect(vAx, hAx[i], axDims[0], axDims[1])
        axisPanes.append(rect)
        pygame.draw.rect(surface, (127,127,0), rect)

        text = f'Axis {i+1}'
        axisLabels.append(text)
        rectcenter = rect.center
        center = (rectcenter[0],rectcenter[1]-30) #Label the top of the pane  
        drawLabel(surface, font, center, text, textSize)

    hatPanes = []
    hatLabels = []
    for i in range(0,3):
        for j in range(0,3):
            rect = pygame.Rect(vHat[i], hHat[j], hatDims[0], hatDims[1])
            hatPanes.append(rect)
            pygame.draw.rect(surface, (0, 127, 127), rect)

            text = f'{i-1},{-(j-1)}'  #Label hat 'axes' in order and by correct value
            hatLabels.append(text)
            drawLabel(surface, font, rect.center, text, textSize)

    return btnPanes, btnLabels, axisPanes, axisLabels, hatPanes, hatLabels


def drawLabel(surface, font, center, text, textSize):
    textRect = font.get_rect(text, size=textSize)
    textRect.center = center
    font.render_to(surface, textRect, text, (0,0,255), size=textSize)


if __name__=='__main__':
    main()