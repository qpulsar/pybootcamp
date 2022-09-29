import pygame

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
saat = pygame.time.Clock()

pygame.init()

devam = True
x = 320
y = 240
r = 5

while devam:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            if event.button == 1:
                r += 1
            elif event.button == 3:
                r -= 1
        elif event.type == pygame.MOUSEBUTTONUP:
            print(event)
        elif event.type == pygame.MOUSEMOTION:
            print(event)
            pos = event.pos
            x = pos[0]
            y = pos[1]

    pygame.draw.circle(screen, (120, 78, 201), (x, y), r)
    pygame.display.flip()
    saat.tick(60)
pygame.quit()
