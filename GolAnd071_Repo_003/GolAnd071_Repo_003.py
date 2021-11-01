import math
from random import *
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        self.vy -= 1
        self.vx *= 0.99
        self.x += self.vx
        self.y -= self.vy
        if self.x <= 10:
            self.x = 10
            self.vx = -self.vx * 0.5
        if self.x >= 790:
            self.x = 790
            self.vx = -self.vx * 0.5
        if self.y <= 10:
            self.y = 10
            self.vy = -self.vy * 0.5
        if self.y >= 590:
            self.y = 590
            self.vy = -self.vy * 0.5


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        if event:
            if event.pos[0] != 20:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            elif event.pos[1] != 450:
                self.an = math.atan((event.pos[0]-20) / (event.pos[1]-450))
            else:
                self.an = 0
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        gunSurf = pygame.Surface((50 * math.log10(self.f2_power), 10))
        gunSurf.fill(WHITE)
        pygame.draw.line(gunSurf, self.color, (0, 5), (50 * math.log10(self.f2_power), 5), 5)
        gunSurf = pygame.transform.rotate(gunSurf, -math.degrees(self.an))
        self.screen.blit(gunSurf, (20, 450 + min(0, 50 * math.log10(self.f2_power) * math.sin(self.an))))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(2, 50)
        vx = self.vx = randint(-10, 10)
        vy = self.vy = randint(-10, 10)
        color = self.color = RED
        self.live = 1

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        if self.x <= 110 + self.r:
            self.x = 110 + self.r
            self.vx = -self.vx
        if self.x >= 790 - self.r:
            self.x = 790 - self.r
            self.vx = -self.vx
        if self.y <= 10 + self.r:
            self.y = 10 + self.r
            self.vy = -self.vy
        if self.y >= 550 - self.r:
            self.y = 550 - self.r
            self.vy = -self.vy

    def hit(self, points=1):
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target(screen)
target2 = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    target1.move()
    target2.move()

    for b in balls:
        b.move()
        if b.hittest(target1):
            target1.live -= 1
            target1.hit()
        if target1.live == 0:
            target1.new_target()
        if b.hittest(target2):
            target2.live -= 1
            target2.hit()
        if target2.live == 0:
            target2.new_target()
    gun.power_up()

pygame.quit()
