import pygame
from pygame.draw import *
import random
pygame.init()

g = 1
width=1000 #ширина окна
heigth=600 # высота окна

class Portals(pygame.sprite.Sprite):
    def __init__(self, screen, x, y,orientation,link):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.x =x
        self.y =y
        self.images=[pygame.transform.scale(pygame.image.load('blueportal.png'), (79, 100)),
                     pygame.transform.scale(pygame.image.load('redportal.png'), (79, 100)),
                     pygame.transform.scale(pygame.image.load('yellowprotal.png'), (79, 100))]
        self.orientation=orientation
        self.link=link
        self.rect = self.images[self.link].get_rect()
        self.rect.center=(self.x+40,self.y+50)
    def draw(self):
        if self.orientation:
            self.images[self.link].set_colorkey((255, 255, 255))
            screen.blit(self.images[self.link], (self.x, self.y))
        else:
            image = pygame.transform.flip(self.images[self.link], True, False)
            image.set_colorkey((255, 255, 255))
            screen.blit(image, (self.x, self.y))



class Hero(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, dx=0, dy=0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.dx = dx
        self.y = y
        self.dy = dy
        self.screen = screen
        self.m = 1
        self.n = 0
        self.rect = pygame.Rect(self.x, self.y, 79, 100)
        self.time = 0
        self.images = []

    def draw(self):
        if hero.dx != 0 and timer % 5 == 0:
            self.n = timer % len(self.images)
        if self.m == -1:
            image = pygame.transform.flip(self.images[self.n], True, False)
            image.set_colorkey((255, 255, 255))
            screen.blit(image, (self.x, self.y))
        else:
            self.images[self.n].set_colorkey((255, 255, 255))
            screen.blit(self.images[self.n], (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, 79, 100)
        self.time += 1



class Platform(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, l):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.l = l
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y - 15, self.l, 30)

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


def move(hero, platforms):
    k = False
    for platform in platforms:
        if pygame.sprite.collide_rect(hero, platform):
            k = True
            hero.dy = 0
            hero.y = platform.y - 115
    if hero.y + 100 > 700:
        hero.y = 600
        k = True
    if not k and hero.y < 600:
        hero.y += hero.dy
        hero.dy += g
    if hero.x < 0 or hero.x + 79 > 1000:
        if hero.x < 0:
            hero.x = 0
        if hero.x + 79 > 1000:
            hero.x = 1000 - 79
    else:
        hero.x += hero.dx



def PlatformGenerator():
    print()
    sectorx=int(width/20)
    sectory=int(heigth/10)
    shablon1=[(0*sectorx,3*sectory,8*sectorx),
              (12*sectorx,3*sectory,8*sectorx),
              (4*sectorx,6*sectory,12*sectorx),
              (0*sectorx, 7*sectory, 2*sectorx),
              (18*sectorx, 7*sectory, 2*sectorx),
              (0*sectorx,10*sectory,20*sectorx)]
    shablon2=[(3*sectorx,5*sectory,14*sectorx),(0*sectorx,10*sectory,20*sectorx)]
    for i in shablon2:
        platforms.append(Platform(screen,i[0],i[1],i[2]))
def transpos(object): # телепортация через портал объекта
    for start_portal in portals:
        if start_portal.rect.colliderect(object.rect): #проверка на пересечение границ спрайтов(пересечение грацниц)
            print(1)
            for end_portal in portals:
                if (start_portal!=end_portal)and(start_portal.link==end_portal.link):#проверяет то что разные порталы но одинаковая связь( цвет)
                    print(2)
                    object.y=object.y-object.rect.bottom+end_portal.rect.bottom
                    if end_portal.orientation:
                        object.x=end_portal.x-object.rect[2]-10 #вычитаем 10 чтобы  было время на реагирование после телерортации
                    else:
                        object.x=end_portal.x+object.rect[2]+10 #-||-
                    if (start_portal.orientation!=end_portal.orientation)and():



FPS = 20
screen = pygame.display.set_mode((width, heigth))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
platforms = []
timer = 0
portals=[]
#temp=pygame.image.load('777.bpm'),
portals.append(Portals(screen,300,450,False,2))
portals.append(Portals(screen,500,450,False,2))

hero = Hero(screen, 0, 35)
hero.images.append(pygame.transform.scale(pygame.image.load('hero1.png'), (79, 100)))
hero.images.append(pygame.transform.scale(pygame.image.load('hero2.png'), (79, 100)))
PlatformGenerator()

while not finished:
    clock.tick(FPS)
    print(hero.rect)

    screen.fill((255, 255, 255))
    image = pygame.image.load('forest1.jpg')
    image = pygame.transform.scale(image, (1000, 600))
    image.set_alpha(200)
    screen.blit(image, (0, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.dx = -4
                hero.m = (-1)
            if event.key == pygame.K_RIGHT:
                hero.dx = 4
                hero.m = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.dx = 0
            if event.key == pygame.K_RIGHT:
                hero.dx = 0

    #pl = Platform(screen, 0, 250, 500)
    #platforms.append(pl)
    #platforms.append(Platform(screen,400,50,500))
    move(hero, platforms)
    transpos(hero)
    for i in platforms:
        i.draw()
    hero.draw()
    portals[0].draw()
    portals[1].draw()
    #pygame.draw.rect (screen, (0,0,0),portals[0].rect)

    timer += 1

    pygame.display.update()

pygame.quit()

'''if __name__ == '__main__':
    main()'''
