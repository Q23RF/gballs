import pygame, sys
from pygame.locals import *
import random
import math

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
ballnum=10

class Ball():
    #建構子
    def __init__(self, x, y, size, color=WHITE, speedx=0, speedy=0):  #預設值
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.speedx=speedx
        self.speedy=speedy
        
    def update(self, screen):
        screen_height=screen.get_height() #取得視窗高度
        screen_width=screen.get_width()   #取得視窗寬度
                        
        if self.x+self.size>screen_width or self.x-self.size<0:
            self.speedx*=-1
        if self.y+self.size>screen_height or self.y-self.size<0:
            self.speedy*=-1
            
        self.x+=self.speedx
        self.y+=self.speedy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, 0)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((750,500))

pygame.display.set_caption('賭球')


    
FPS=30
fpsClock = pygame.time.Clock()

balls=[]
for i in range(ballnum):
    x=random.randint(100,400)
    y=random.randint(100,300)
    size=random.randint(20,40)
    r=random.randint(0,40)
    g=random.randint(100,255)
    b=random.randint(20,140)
    speedx=random.randint(-5,5)
    speedy=random.randint(-5,5)
    ballx=Ball(x=x,y=y,color=(r,g,b),speedx=speedx,speedy=speedy,size=size)
    balls.append(ballx)


while True:
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==MOUSEBUTTONUP:
            for k in range(len(balls)):
                radius = balls[k].size / 2
                mpos = pygame.mouse.get_pos()
                x1, y1 = mpos
                x2, y2 = balls[k].x, balls[k].y
                distance = math.hypot(x1 - x2, y1 - y2)
                if distance <= radius:
                    balls[k].color = (255,255,255)
        
        if event.type==KEYUP:
            if len(balls) > 0:
                j=0
                del(balls[j])
                j+=1
            else:
                pygame.quit()
                sys.exit()


    #狀態更新        
    #計算圓形位置
    for ball in balls:
        ball.update(DISPLAYSURF)
         
    #畫面更新
    DISPLAYSURF.fill(BLACK)
    for ball in balls:
        ball.draw(DISPLAYSURF)  
 
    pygame.display.update()
    
    fpsClock.tick(FPS)
    