import pygame
from pygame.draw import *

pygame.init()

g = 0


class Hero(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.dx = dx
        self.y = y
        self.dy = dy + g
        self.screen = screen
        self.m = 1
        self.rect = pygame.Rect(self.x + self.dx, self.y + self.dy, 79, 100)

    def draw(self):
        image1 = pygame.image.load('hero1.png')
        image1 = pygame.transform.scale(image1, (79, 100))
        if self.m == -1:
            image1 = pygame.transform.flip(image1, True, False)
        image1.set_colorkey((255, 255, 255))
        screen.blit(image1, (self.x, self.y))
        self.rect = pygame.Rect(self.x + self.dx, self.y + self.dy, 79, 100)


def move(hero, platforms):
    if hero.x < 0 or hero.x + 79 > 1000:
        hero.dx *= (-1)
        hero.m *= (-1)
    for platform in platforms:
        if not pygame.sprite.collide_rect(hero, platform):
            hero.y = hero.y + hero.dy
    hero.x = hero.x + hero.dx


class Platform(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, l):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.l = l
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.l, 15)

    def draw(self):
        rect(self.screen, (194, 120, 16), (self.x, self.y - 15, self.l, 30), border_bottom_left_radius=14,
             border_bottom_right_radius=14)
        points = [(self.x, self.y - 15), (self.x, self.y)]
        k = 1
        for i in range(10, self.l, 10):
            points.append((self.x + i, self.y - k * 5))
            k *= (-1)
        points.append((self.x + self.l, self.y))
        points.append((self.x + self.l, self.y - 15))
        polygon(self.screen, (80, 180, 89), points)


FPS = 20
screen = pygame.display.set_mode((1000, 700))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
platforms = []
hero = Hero(screen, 10, 10, 4, 1)

while not finished:
    clock.tick(FPS)

    screen.fill((255, 255, 255))
    image = pygame.image.load('forest1.jpg')
    image = pygame.transform.scale(image, (1000, 600))
    image.set_alpha(200)
    screen.blit(image, (0, 100))

    pl = Platform(screen, 0, 250, 500)
    platforms.append(pl)
    move(hero, platforms)
    pl.draw()
    hero.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # if event.type == pygame.MOUSEBUTTONDOWN:

    pygame.display.update()

pygame.quit()

'''if __name__ == '__main__':
    main()'''
