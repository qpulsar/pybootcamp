import pygame
import random

w = 500
h = 500
satir = 20
beyaz = (100, 170, 200)
yesil = (0, 255, 0)
kirmizi = (255, 0, 0)
devam = True


class kup(object):
    global screen, w, h, satir

    def __init__(self, pos, yonx=1, yony=0, renk=yesil, kafa=False):
        self.pos = list(pos)
        self.yonx = yonx
        self.yony = yony
        self.renk = renk
        self.kafa = kafa

    def ciz(self):
        g = w / satir
        x, y = self.pos[0], self.pos[1]
        pygame.draw.rect(screen, self.renk, (g * x + 1, g * y + 1, g - 1, g - 1))
        if self.kafa:
            pygame.draw.circle(screen, kirmizi, (g * x + 12, g * y + 10), 4)
            pygame.draw.circle(screen, kirmizi, (g * x + 12, g * y + 14), 4)


class yilan(object):
    govde = []

    def __init__(self, pos):
        self.pos = list(pos)
        self.yonx = 1
        self.yony = 0
        self.govde.append(kup(pos, kafa=True))
        self.govde.append(kup((pos[0] - 1, pos[1])))
        self.govde.append(kup((pos[0] - 2, pos[1])))

    def ciz(self):
        for k in self.govde:
            k.ciz()

    def uza(self):
        kuyruk = kup(self.govde[1].pos)
        self.govde.append(kuyruk)

    def move(self, yon):
        if yon is None:
            return
        if yon == pygame.K_RIGHT:
            self.yonx = 1
            self.yony = 0
        elif yon == pygame.K_LEFT:
            self.yonx = -1
            self.yony = 0
        elif yon == pygame.K_UP:
            self.yonx = 0
            self.yony = -1
        elif yon == pygame.K_DOWN:
            self.yonx = 0
            self.yony = 1

        for k in range(len(self.govde) - 1, 0, -1):
            self.govde[k].pos[0] = self.govde[k - 1].pos[0]
            self.govde[k].pos[1] = self.govde[k - 1].pos[1]

        self.govde[0].pos[0] += self.yonx
        self.govde[0].pos[1] += self.yony
        # sınırlara gelirse
        if self.govde[0].pos[0] > 19:
            self.govde[0].pos[0] = 0
        if self.govde[0].pos[0] < 0:
            self.govde[0].pos[0] = 19
        if self.govde[0].pos[1] > 19:
            self.govde[0].pos[1] = 0
        if self.govde[0].pos[1] < 0:
            self.govde[0].pos[1] = 19


class elma(object):
    global screen, w, h, satir
    gen = w // satir

    def __init__(self):
        self.at()

    def at(self):
        self.x = random.randrange(0, satir)
        self.y = random.randrange(0, satir)

    def ciz(self):
        pygame.draw.circle(screen, kirmizi,
                           (self.x * self.gen + self.gen // 2,
                            self.y * self.gen + self.gen // 2),
                           10)


def grid():
    global screen, w, h, satir, fonts
    genislik = w / satir
    x = y = 0
    for i in range(satir):
        x += genislik
        y += genislik
        pygame.draw.line(screen, beyaz, (0, y), (w, y))
        pygame.draw.line(screen, beyaz, (x, 0), (x, h))
    x = 1
    for i in range(satir):
        f = fonts["normal"].render(str(i), True, beyaz)
        screen.blit(f, (x + 5, 5, 10, 10))
        screen.blit(f, (6, x + 5, 10, 10))
        x += genislik

def yem_kontrol(y, e):
    if y.govde[0].pos[0] == e.x and y.govde[0].pos[1] == e.y:
        e.at()
        y.uza()

def main():
    global devam, screen, fonts

    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Yılan Oyunu")
    fonts = {"baslik": pygame.font.SysFont("Verdana", 100, True),
             "normal": pygame.font.SysFont("Verdana", 12, True)}
    clock = pygame.time.Clock()
    # yılan
    kobra = yilan((11, 10))
    # yem
    yem = elma()

    yon = None
    while devam:
        screen.fill((0, 0, 0))
        grid()
        yem.ciz()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                devam = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    devam = False
                else:
                    yon = event.key
        yem_kontrol(kobra, yem)
        kobra.move(yon)
        kobra.ciz()
        pygame.display.update()
        clock.tick(5)
    pygame.quit()


if __name__ == '__main__':
    main()
