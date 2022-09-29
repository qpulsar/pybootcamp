import pygame

pygame.init()
ekran = pygame.display.set_mode((400, 400))

bitti = False

while not bitti:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            bitti = True
    pygame.display.flip()
