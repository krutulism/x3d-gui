import pygame
import sys

def main():
    pygame.init()

    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    j = joysticks[0]
    j.init()
    print(j.get_name())

    W = 800
    H = 600
    textSize = 14

    surface = pygame.display.set_mode([W, H])
    pygame.display.set_caption("X3D GUI")
    myfont = pygame.freetype.SysFont('Helvetica', 11)

    running = True
    hatStatus = None

    btnPanes, btnLabels, axisPanes, axisLabels, hatPanes, hatLabels = drawPanes(surface, myfont)

    pygame.display.update()

    while running:
        updateRects = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            # Handle and draw button statuses
            elif event.type == pygame.JOYBUTTONDOWN:
                b = event.button
                pane = btnPanes[b]
                pygame.draw.rect(surface, (0,255,0), pane)
                drawLabel(surface, myfont, pane.center, btnLabels[b], textSize, (0,255,0))

                updateRects.append(pane)
            elif event.type == pygame.JOYBUTTONUP:
                b = event.button
                pane = btnPanes[b]
                pygame.draw.rect(surface, (213,0,42), pane)
                drawLabel(surface, myfont, pane.center, btnLabels[b], textSize, (213,0,42))

                updateRects.append(pane)

            # Handle and draw axis values
            elif event.type == pygame.JOYAXISMOTION:
                a = event.axis
                pane = axisPanes[a]
                text = f'{event.value:.5f}'

                #Draw Label but redraw the entire width of the button
                textRect = myfont.get_rect(text, size=textSize)
                backingRect = pygame.Rect(0, 0, pane.width, textRect.height + 10)
                backingRect.center, textRect.center = pane.center, pane.center
                pygame.draw.rect(surface, (0,255,0), backingRect)
                myfont.render_to(surface, textRect, text, (0,0,255), size=textSize)

                updateRects.append(pane)

            # Handle and draw hat values
            elif event.type == pygame.JOYHATMOTION:
                v = event.value #tuple with -1 to 1 for horiz, then -1 to 1 for vert
                pane = hatPanes[v[0]+1][2-(v[1]+1)]
                text = hatLabels[v[0]+1][2-(v[1]+1)]
                textRect = myfont.get_rect(text, size=textSize)
                pygame.draw.rect(surface, (0,255,0), pane)
                drawLabel(surface, myfont, pane.center, text, textSize, (0,255,0))

                updateRects.append(pane)
                
                if hatStatus is not None:
                    text = hatLabels[hatStatus[0]+1][2-(hatStatus[1]+1)]
                    prevPane = hatPanes[hatStatus[0]+1][2-(hatStatus[1]+1)]
                    textRect = myfont.get_rect(text, size=textSize)
                    pygame.draw.rect(surface, (213,0,42), prevPane)
                    drawLabel(surface, myfont, prevPane.center, text, textSize, (213,0,42))
                    updateRects.append(prevPane)
                hatStatus = (v[0],v[1])
                

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
        pygame.draw.rect(surface, (213,0,42), rect)

        text = f'Button  {i+1}'
        btnLabels.append(text)
        drawLabel(surface, font, rect.center,  text, textSize, (213,0,42))

    axisPanes = []
    axisLabels = []
    for i in range(0,len(hAx)):
        rect = pygame.Rect(vAx, hAx[i], axDims[0], axDims[1])
        axisPanes.append(rect)
        pygame.draw.rect(surface, (213,0,42), rect)

        text = f'Axis {i+1}'
        axisLabels.append(text)
        rectcenter = rect.center
        center = (rectcenter[0],rectcenter[1]-30) #Label the top of the pane  
        drawLabel(surface, font, center, text, textSize, (213,0,42))

    hatPanes = []
    hatLabels = []
    for i in range(0,3):
        hatPanesCol = []
        hatLabelsCol = []
        for j in range(0,3):
            rect = pygame.Rect(vHat[i], hHat[j], hatDims[0], hatDims[1])
            hatPanesCol.append(rect)
            pygame.draw.rect(surface, (213, 0, 42), rect)

            text = f'{i-1},{-(j-1)}'  #Label hat 'axes' in order and by correct value
            hatLabelsCol.append(text)
            drawLabel(surface, font, rect.center, text, textSize, (213,0,42))
        hatPanes.append(hatPanesCol)
        hatLabels.append(hatLabelsCol)

    return btnPanes, btnLabels, axisPanes, axisLabels, hatPanes, hatLabels


def drawLabel(surface, font, center, text, textSize, baseColor):
    textRect = font.get_rect(text, size=textSize)
    textRect.center = center
    pygame.draw.rect(surface, baseColor, textRect)
    font.render_to(surface, textRect, text, (0,0,255), size=textSize)
    return textRect


if __name__=='__main__':
    main()