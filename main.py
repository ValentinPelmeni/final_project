import pygame
from pygame.draw import *

pygame.init()


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, l):
        self.x = x
        self.y = y
        self.l = l
        self.screen = screen

    def draw(self):
        rect(self.screen, (194, 120, 16), (self.x, self.y - 15, self.l, 30))
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

while not finished:
    clock.tick(FPS)

    screen.fill((255, 255, 255))
    image = pygame.image.load('forest1.jpg')
    image.set_colorkey((255, 255, 255))
    image = pygame.transform.scale(image, (1000, 600))
    image.set_alpha(200)
    screen.blit(image, (0, 100))

    pl = Platform(screen, 0, 250, 500)
    pl.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # if event.type == pygame.MOUSEBUTTONDOWN:

    pygame.display.update()

pygame.quit()

'''if __name__ == '__main__':
    main()'''
