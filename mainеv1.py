import pygame
import random
from pygame.draw import *
width=1000 #ширина окна
heigth=700 # высота окна
pygame.init()
g = 1

class Portals(pygame.sprite.Sprite):
    def __init__(self, screen, x, y,orientation,link):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.x =x
        self.y =y
        self.timer_image_portal=0
        self.timer_image_portal_temp=random.randint(0,11)
        self.images=[[
                     pygame.transform.scale(pygame.image.load('blueportal1.png'), (79, 100)),
                     pygame.transform.scale(pygame.image.load('blueportal2.png'), (79, 100)),
                     pygame.transform.scale(pygame.image.load('blueportal3.png'), (79, 100)),
                     pygame.transform.scale(pygame.image.load('blueportal4.png'), (79, 100))],
                     [
                      pygame.transform.scale(pygame.image.load('redportal1.png'), (79, 100)),
                      pygame.transform.scale(pygame.image.load('redportal2.png'), (79, 100)),
                      pygame.transform.scale(pygame.image.load('redportal3.png'), (79, 100)),
                      pygame.transform.scale(pygame.image.load('redportal4.png'), (79, 100))],
                     [
                      pygame.transform.scale(pygame.image.load('yellowprotal1.png'), (79, 100)),
                      pygame.transform.scale(pygame.image.load('yellowportal2.png'), (79, 100)),
                      pygame.transform.scale(pygame.image.load('yellowportal3.png'), (79, 100)),
                      pygame.transform.scale(pygame.image.load('yellowportal4.png'), (79, 100))
                     ]]
        self.orientation=orientation#определяет оринтацию портала вправо или влево True-влево,False-вправо
        self.link=link#определяет "частоту портала" порталы с одинаковой частотой телепортируют друг к другу частоты 0 1 2 соотвесвенно синий красный жельтый портал
        self.rect = self.images[self.link][0].get_rect()
        self.rect.center=(self.x+40,self.y+50)#просто rect
    def draw(self):#отрисовка портала
        if self.orientation:
            self.images[self.link][self.timer_image_portal].set_colorkey((255, 255, 255))
            screen.blit(self.images[self.link][self.timer_image_portal], (self.x, self.y))
        else:
            image = pygame.transform.flip(self.images[self.link][self.timer_image_portal], True, False)
            image.set_colorkey((255, 255, 255))
            screen.blit(image, (self.x, self.y))
        self.timer_image_portal_temp+=1
        if self.timer_image_portal_temp>3:
            self.timer_image_portal=1

        if self.timer_image_portal_temp >6:
            self.timer_image_portal = 2

        if self.timer_image_portal_temp >9:
            self.timer_image_portal = 3

        if self.timer_image_portal_temp>12:
            self.timer_image_portal=0
            self.timer_image_portal_temp=0



class Coin(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        circle(self.screen, (250, 210, 1), self.x, self.y, 12)
        circle(self.screen, (255, 215, 0), self.x, self.y, 10)


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


def move(hero, platforms,k):
    m = False
    for platform in platforms:
        if platform.x <= hero.x <= platform.x + platform.l and hero.y + hero.dy + 100 >= platform.y - 15 and hero.y + 100 <= platform.y - 15:
            m = True
            hero.y = platform.y - 115
    if hero.y + hero.dy + 100 >= 700 and hero.y + 100 <= 700:
        hero.y = 600
        m = True
    if m:
        k = True
    else:
        k = False
    if k:
        if hero.dy < 0:
            hero.y += hero.dy
            hero.dy += g
        else:
            hero.dy = 0
    if not k and hero.y <= 600:
        hero.y += hero.dy
        hero.dy += g
    if hero.x < 0 or hero.x + 79 > 1000:
        if hero.x < 0:
            hero.x = 0
            hero.dx = 0
        if hero.x + 79 > 1000:
            hero.x = 1000 - 79
            hero.dx = 0
    else:
        if k:
            hero.x += hero.dx
    return k
def transpos(object): # телепортация через портал объекта
    for start_portal in portals:
        if start_portal.rect.colliderect(object.rect): #проверка на пересечение границ спрайтов(пересечение грацниц)
            for end_portal in portals:
                if (start_portal!=end_portal)and(start_portal.link==end_portal.link):#проверяет то что разные порталы но одинаковая связь( цвет)
                    object.y=object.y-object.rect.bottom+end_portal.rect.bottom
                    if end_portal.orientation:
                        object.x=end_portal.x-object.rect[2]-10 #вычитаем 10 чтобы  было время на реагирование после телерортации
                    else:
                        object.x=end_portal.x+object.rect[2]+10 #-||-
                    #if (start_portal.orientation!=end_portal.orientation)and(есть скорость):
                    #    object.vx=(-1)*object.vx


FPS = 20
screen = pygame.display.set_mode((width, heigth))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
platforms = []
timer = 0
k = False
portals=[]  #список порталов все порталы добавлять сюда

hero = Hero(screen, 0, 35)
hero.images.append(pygame.transform.scale(pygame.image.load('hero1.png'), (79, 100)))
hero.images.append(pygame.transform.scale(pygame.image.load('hero2.png'), (79, 100)))
portals.append(Portals(screen,300,450,False,2))#тестовые порталы
portals.append(Portals(screen,500,450,False,2))#тестовые порталы

while not finished:
    clock.tick(FPS)

    screen.fill((255, 255, 255))
    image = pygame.image.load('forest1.jpg')
    image = pygame.transform.scale(image, (1000, 600))
    image.set_alpha(200)
    screen.blit(image, (0, 100))

    pl = Platform(screen, 0, 250, 500)
    platforms.append(pl)
    k = move(hero, platforms,k)
    pl.draw()
    hero.draw()

    for i in portals:  #отрисовка порталов
        i.draw()       #отрисовка порталов

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
            if event.key == pygame.K_UP and k:
                hero.dy = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.dx = 0
            if event.key == pygame.K_RIGHT:
                hero.dx = 0


    f = pygame.font.Font(None, 36)
    text = f.render('Your game time (sec):' + str(timer/20), 1, (180, 0, 0))
    screen.blit(text, (400, 30))
    transpos(hero)#проверка на возможность телепортации героя и телепортация в случае если он зашел в портал
    timer += 1

    pygame.display.update()

pygame.quit()

'''if __name__ == '__main__':
    main()'''