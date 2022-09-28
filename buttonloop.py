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
        
        flag += 1
        if flag % 200000 == 0:
            print(axes)


except KeyboardInterrupt:
    print("Goodbye")
    j.quit()
    pygame.joystick.quit()