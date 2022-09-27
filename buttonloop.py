import pygame

pygame.init()
#pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

j = joysticks[0]
j.init()
print(j.get_name())

# Event loop demo

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                b = event.button
                print(f'{b}Button Pressed')
            elif event.type == pygame.JOYBUTTONUP:
                print('Button Released')

except KeyboardInterrupt:
    print("Goodbye")
    j.quit()
    pygame.joystick.quit()