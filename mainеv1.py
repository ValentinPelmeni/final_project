import pygame
import random
from pygame.draw import *
import math
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
class Guns:
    def __init__(self,screen,owner,gun_type):#тут под owner имееться в виду тот кто держит пушку нужен для координат если
                                              #если будет несколько игроков надо указать игрока если конечно player.x даст координату игрока
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.owner=owner
        self.gun_type=gun_type
        self.images=[pygame.transform.scale(pygame.image.load('gun1.png'), (80, 45))]
    def draw(self):
        angle = math.atan2(-self.owner.y+pygame.mouse.get_pos()[1], self.owner.x-pygame.mouse.get_pos()[0])#тут наверное надо будет чтото поменять позиции мышки
                                                                                                             #всм не знаю как по мультиплееру передоваться будет
        image = pygame.transform.rotate(self.images[self.gun_type], angle)
        image = self.images[self.gun_type]
        image.set_colorkey((255, 255, 255))
        image = pygame.transform.rotate(image, ((angle / 3.14) * 180)+180)
        screen.blit(image, (self.owner.x+30, self.owner.y+20))
    def vistrel(self):
        angle = math.atan2(-self.owner.y + pygame.mouse.get_pos()[1], self.owner.x - pygame.mouse.get_pos()[0])
        bullets.append(Bullets(self.screen,self.owner.x+60,self.owner.y+30,-20*math.cos(angle),20*math.sin(angle),self.owner,self.gun_type,0))



class Bullets:
    def __init__(self, screen, x, y, vx,vy,owner,bullet_type,bullet_time_life):
        #x,y,vx,vy-стандарнто,owner-тот кто выстрелил чтобы в коцне пуля не убила стрелявшего
        # bullet_type-тип пули(вдруг будут еще) bullet_time_life-просто таймер(мб время жизни пули должно пригодиться)
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.images=[pygame.transform.scale(pygame.image.load('bullet1.png'), (20, 20))]
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.owner=owner
        self.bullet_type=bullet_type
        self.bullet_time_life=bullet_time_life
        self.rect = self.images[self.bullet_type].get_rect()
        print(vx,vy)
        print("создал")
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
        self.bullet_time_life-=1
        print('движемся')
    def draw(self): #тут ничего интересного просто отрисовка пули (поворот изображения и тп)
        print("рисую пулю")
        angle=math.atan2(-self.vy, self.vx)
        image=pygame.transform.rotate(self.images[self.bullet_type],angle)
        image=self.images[self.bullet_type]
        image.set_colorkey((0,0,0))
        image=pygame.transform.rotate(image,(angle/3.14)*180)
        screen.blit(image, (self.x, self.y))
        self.rect.center = (self.x, self.y)

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
                    if (start_portal.orientation!=end_portal.orientation)and(type(object)==Bullets):
                        object.vx=int((-1)*object.vx)
def Generator_pl():
    level=(300,500,700, 1000,100)#уровни на которых нужно сделать платформы
    jump_distance=150#длинна прыжка
    min_length=200#минимальная длинна платформы
    max_length=400#максимальная длинна платформы
    for i in level:
        x_nachala=0
        while x_nachala<width+5:#проверка на не выход за экран
            length=random.randint(min_length,max_length)
            platforms.append(Platform(screen, x_nachala, i, length))
            x_nachala+=(length+jump_distance)
            #print("mozno")#для отладки


FPS = 30
screen = pygame.display.set_mode((width, heigth))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
platforms = []
bullets=[]
timer = 0
k = False
portals=[]  #список порталов все порталы добавлять сюда

hero = Hero(screen, 0, 35)
hero.images.append(pygame.transform.scale(pygame.image.load('hero1.png'), (79, 100)))
hero.images.append(pygame.transform.scale(pygame.image.load('hero2.png'), (79, 100)))
portals.append(Portals(screen,300,450,True,2))#тестовые порталы
portals.append(Portals(screen,50,450,False,2))#тестовые порталы
Generator_pl()
bullets.append(Bullets(screen,100,100,8,0.5,0,0,0))
test_gun=Guns(screen,hero,0)
while not finished:
    clock.tick(FPS)

    screen.fill((255, 255, 255))
    image = pygame.image.load('forest1.jpg')
    image = pygame.transform.scale(image, (1000, 600))
    image.set_alpha(200)
    screen.blit(image, (0, 100))

    k = move(hero, platforms,k)
    hero.draw()


    for i in portals:  #отрисовка порталов
        i.draw()       #отрисовка порталов
    for i in platforms:  #плтаформ
        i.draw()
    for i in bullets:#движение и отрисовка пуль
        i.draw()
        i.move()
        #if i.timer<0:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.dx = -8
                hero.m = (-1)
            if event.key == pygame.K_RIGHT:

                hero.dx = 8
                hero.m = 1
            if event.key == pygame.K_UP and k:
                hero.dy = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.dx = 0
            if event.key == pygame.K_RIGHT:
                hero.dx = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            test_gun.vistrel()

    test_gun.draw()

    f = pygame.font.Font(None, 36)
    text = f.render('Your game time (sec):' + str(timer/20), 1, (180, 0, 0))
    screen.blit(text, (400, 30))
    transpos(hero)#проверка на возможность телепортации героя и телепортация в случае если он зашел в портал
    for i in bullets:
        transpos(i)#проверка на возможность телепортации всех пуль
    timer += 1

    pygame.display.update()

pygame.quit()

'''if __name__ == '__main__':
    main()'''
