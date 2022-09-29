import pygame

pygame.init()
ekran = pygame.display.set_mode((500, 500))

bitti = False
saat = pygame.time.Clock()

renk1 = (255, 0, 0)
renk2 = (0, 255, 0)
renk = renk1
x = 240
y = 240

while not bitti:
    ekran.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bitti = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if renk == renk1:
                renk = renk2
            else:
                renk = renk1
    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] or tus[pygame.K_a]:
        x -= 5
    if tus[pygame.K_RIGHT] or tus[pygame.K_d]:
        x += 5
    if tus[pygame.K_UP] or tus[pygame.K_w]:
        y -= 5
    if tus[pygame.K_DOWN] or tus[pygame.K_s]:
        y += 5

    pygame.draw.rect(ekran, renk, pygame.Rect(x, y, 20, 20))
    pygame.display.flip()
    saat.tick(60)
