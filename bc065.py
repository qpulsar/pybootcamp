import pygame

pygame.init()

ekran = pygame.display.set_mode((300, 300))

bitti = False
saat = pygame.time.Clock()
x = 50
y = 50
w = 30
h = 30
dx = 2
dy = 1
while not bitti:
    ekran.fill((100, 200, 50))
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            bitti = True

    pygame.draw.rect(ekran, (255, 0, 0), pygame.Rect(x, y, w, h))
    x += dx
    y += dy
    if x + w > 300 or x < 1:
        dx = -dx
    if y + h > 300 or y < 1:
        dy = -dy
    pygame.display.flip()
    saat.tick(60)
