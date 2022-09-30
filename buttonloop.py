import pygame
import numpy as np

pygame.init()
#pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

j = joysticks[0]
j.init()
print(j.get_name())

# Event loop demo

flag = 0
axes = np.zeros(4)

try:
    while True:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                b = event.button
                print(f'{b}Button Pressed')
            elif event.type == pygame.JOYBUTTONUP:
                print('Button Released')
            elif event.type == pygame.JOYAXISMOTION:
                axes[event.axis] = event.value
            elif event.type == pygame.JOYHATMOTION:
                #Horiz axis at index [0]. -1 for L. 1 for R.
                #Vert axis at index [1]. -1 for D. 1 for U.
                print(event.value)
        
        flag += 1
        if flag % 200000 == 0:
            pass
            #print(axes)


except KeyboardInterrupt:
    print("Exiting")
    j.quit()
    pygame.joystick.quit()