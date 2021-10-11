import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
frame = 0
screen = pygame.display.set_mode((1200, 800))
score = 0
scorepos = (10, 10)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def update_frame(frame):
    frame += 1
    frame %= 50
    return frame


def update_ball():
    global num, x, y, r, vx, vy, color, t
    if frame == 0:
        num = randint(1, 10)
        x, y, r, vx, vy, color, t = [], [], [], [], [], [], []
        for i in range(num):
            t.append(True)
            x.append(randint(100, 1100))
            y.append(randint(100, 700))
            r.append(randint(50, 100))
            vx.append(randint(-50, 50))
            vy.append(randint(-50, 50))
            color.append(COLORS[randint(0, 5)])
            circle(screen, color[i], (x[i], y[i]), r[i])
    else:
        for i in range(num):
            if t[i]:
                x[i] += vx[i]
                y[i] += vy[i]
                if x[i] <= r[i] or y[i] <= r[i] or x[i] >= 1200 or y[i] >= 800:
                    vx[i] = randint(-50, 50)
                    vy[i] = randint(-50, 50)
                x[i] = max(r[i], min(1200 - r[i], x[i]))
                y[i] = max(r[i], min(800 - r[i], y[i]))
                circle(screen, color[i], (x[i], y[i]), r[i])


def click(event, score):
    for i in range(num):
        if (event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2 <= r[i] ** 2:
            score += 10
            t[i] = False
    return score


def update_score():
    font = pygame.font.Font(None, 50)
    text = font.render(str(score), True, [255, 255, 255])
    screen.blit(text, scorepos)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = click(event, score)
    update_score()
    update_ball()
    frame = update_frame(frame)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()