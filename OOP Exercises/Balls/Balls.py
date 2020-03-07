# Name: Kevin Cui
# Date: 2020-02-05
# Description: Ball Class

import pygame
import os
import random
import math
import time

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

SIDELEN = 650

pygame.display.set_caption("Balls")
window = pygame.display.set_mode((SIDELEN, SIDELEN))

BLACK = (0, 0, 0)

RED = (200, 120, 120)
GREEN = (120, 200, 120)
BLUE = (120, 120, 200)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (200, 200, 120)
WHITE = (255, 255, 255)

COLOURS = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, WHITE]

font = pygame.font.SysFont('Arial Black', 48)
text = font.render("GAME OVER", 5, WHITE)

snitch = pygame.transform.scale(pygame.image.load("1.png"), (20, 20)).convert_alpha()
bludger = pygame.transform.scale(pygame.image.load("0.png"), (70, 70)).convert_alpha()

balls = []

class Ball(object):

    def __init__(self, colour, size, speedX, speedY, visible=True):
        self.colour = colour
        self.size = size
        self.speedX = speedX
        self.speedY = speedY
        self.visible = visible
        self.generatePos()

    def __str__(self):
        return 'Size: '+str(self.size)+'; Speed (x, y): ('+str(self.speedX)+', '+str(self.speedY)+'); Position (x, y): ('+str(self.ball_x)+', '+str(self.ball_y)+')'

    def generatePos(self):
        overflow_check = 0
        pos = False
        while not pos and overflow_check < 100:
            pos = True
            self.ball_x = random.randrange(self.size, SIDELEN - self.size, 5)
            self.ball_y = random.randrange(self.size, SIDELEN - self.size, 5)
            for b in balls:
                if b != self and self.collideBall(b):
                    pos = False
            overflow_check += 1
        if overflow_check == 100:
            balls.pop(balls.index(self))
            return False
        return True
    
    def draw(self):
        if self.visible:
            pygame.draw.circle(window, self.colour, (self.ball_x, self.ball_y), self.size)

    def collideBall(self, other):
        return math.sqrt((self.ball_x - other.ball_x)**2 + (self.ball_y - other.ball_y)**2) <= self.size + other.size

    def bounce(self):
        
        self.ball_x += self.speedX
        self.ball_y += self.speedY

        if self.ball_x - self.size <= 0:
            self.ball_x -= self.speedX
            self.speedX = abs(self.speedX)
        if self.ball_x + self.size >= SIDELEN:
            self.ball_x -= self.speedX
            self.speedX = -abs(self.speedX)
        if self.ball_y - self.size <= 0:
            self.ball_y -= self.speedY
            self.speedY = abs(self.speedY)
        if self.ball_y + self.size >= SIDELEN:
            self.ball_y -= self.speedY
            self.speedY = -abs(self.speedY)

        i = 0
        while i < len(balls):
            b = balls[i]
            i += 1
            if b != self and not (hasattr(b, 'name') and b.name == 'Snitch') and self.collideBall(b):
                self.ball_x -= self.speedX
                self.ball_y -= self.speedY
                self.speedX *= -1
                self.speedY *= -1
                b.speedX *= -1
                b.speedY *= -1
                if hasattr(b, 'name') and b.name == 'Bludger':
                    balls.pop(balls.index(self))
                    return

def gameOver():
    window.fill(BLACK)
    window.blit(text, (85, 120))
    pygame.display.update()    

class Snitch(Ball):

    def __init__(self):
        self.name = 'Snitch'
        Ball.__init__(self, WHITE, 10, random.choice((-5, 5)), random.choice((-4, 4)))

    def draw(self):
        self.visible = int(time.time()) % 4 < 2
        if self.visible:
            pygame.draw.circle(window, self.colour, (self.ball_x, self.ball_y), self.size)
            window.blit(snitch, (self.ball_x - self.size, self.ball_y - self.size))

    def bounce(self):
        
        self.ball_x += self.speedX
        self.ball_y += self.speedY

        if self.ball_x - self.size <= 0:
            self.generatePos()
            self.speedX = random.choice((-5, 5))
            self.speedY = random.choice((-4, 4))
        if self.ball_x + self.size >= SIDELEN:
            self.generatePos()
            self.speedX = random.choice((-5, 5))
            self.speedY = random.choice((-4, 4))
        if self.ball_y - self.size <= 0:
            self.generatePos()
            self.speedX = random.choice((-5, 5))
            self.speedY = random.choice((-4, 4))
        if self.ball_y + self.size >= SIDELEN:
            self.generatePos()
            self.speedX = random.choice((-5, 5))
            self.speedY = random.choice((-4, 4))
            
        b = balls[1]
        if hasattr(b, 'name') and b.name == 'Bludger' and self.collideBall(b):
            balls.pop(balls.index(self))
            return

class Bludger(Ball):

    def __init__(self):
        self.name = 'Bludger'
        Ball.__init__(self, WHITE, 35, random.choice((-1, 1)), random.choice((-1, 1)))

    
    def bounce(self):
        
        self.ball_x += self.speedX
        self.ball_y += self.speedY

        if self.ball_x - self.size <= 0:
            self.ball_x -= self.speedX
            self.speedX = abs(self.speedX)
        if self.ball_x + self.size >= SIDELEN:
            self.ball_x -= self.speedX
            self.speedX = -abs(self.speedX)
        if self.ball_y - self.size <= 0:
            self.ball_y -= self.speedY
            self.speedY = abs(self.speedY)
        if self.ball_y + self.size >= SIDELEN:
            self.ball_y -= self.speedY
            self.speedY = -abs(self.speedY)

        i = 0
        while i < len(balls):
            b = balls[i]
            i += 1
            if b != self and self.collideBall(b):
                self.ball_x -= self.speedX
                self.ball_y -= self.speedY
                self.speedX *= -1
                self.speedY *= -1
                balls.pop(i-1)
                i -= 1
    
    def draw(self):
        if self.visible:
            pygame.draw.circle(window, self.colour, (self.ball_x, self.ball_y), self.size)
            window.blit(bludger, (self.ball_x - self.size, self.ball_y - self.size))
            
play = True
key_down = False
over = False

balls.append(Snitch())
balls.append(Bludger())

while play:

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and not key_down:
        key_down = True
        balls.append(Ball(random.choice(COLOURS), random.randint(15, 30), random.choice((random.randint(-3, -2), random.randint(2, 3))), random.choice((random.randint(-3, -2), random.randint(2, 3)))))
    elif not key[pygame.K_SPACE]:
        key_down = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            play = False

    window.fill(BLACK)

    for b in balls:
        b.bounce()
        b.draw()

    if not (hasattr(balls[0], 'name') and balls[0].name == 'Snitch'):
        play = False
        over = True
    
    pygame.display.update()
    pygame.time.delay(5)

while over:
    gameOver()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            over = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            over = False
    pygame.time.delay(5)
    
pygame.quit()
