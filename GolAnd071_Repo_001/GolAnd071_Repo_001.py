import pygame
from pygame.draw import *

pygame.init()

FPS = 30


def ex1():
    screen = pygame.display.set_mode((400, 400))
    rect(screen, (255, 0, 255), (100, 100, 200, 200))
    rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
    polygon(screen, (255, 255, 0), [(100, 100), (200, 50), (300, 100), (100, 100)])
    polygon(screen, (0, 0, 255), [(100, 100), (200, 50), (300, 100), (100, 100)], 5)
    circle(screen, (0, 255, 0), (200, 175), 50)
    circle(screen, (255, 255, 255), (200, 175), 50, 5)


def ex2():
    screen = pygame.display.set_mode((400, 400))
    x1 = 100
    y1 = 100
    x2 = 300
    y2 = 200
    N = 10
    color = (255, 255, 255)
    rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N):
        line(screen, color, (x, y1), (x, y2))
        x += h


def ex3():
    screen = pygame.display.set_mode((400, 400))
    rect(screen, (150, 150, 150), (0, 0, 400, 400))
    circle(screen, (255, 255, 0), (200, 200), 100)
    circle(screen, (0, 0, 0), (200, 200), 100, 1)
    rect(screen, (0, 0, 0), (150, 250, 100, 20))
    circle(screen, (255, 0, 0), (150, 175), 20)
    circle(screen, (0, 0, 0), (150, 175), 20, 1)
    circle(screen, (0, 0, 0), (150, 175), 9)
    circle(screen, (255, 0, 0), (250, 175), 16)
    circle(screen, (0, 0, 0), (250, 175), 16, 1)
    circle(screen, (0, 0, 0), (250, 175), 8)
    polygon(screen, (0, 0, 0), ((100, 125), (185, 170), (190, 160), (105, 115)))
    polygon(screen, (0, 0, 0), ((300, 140), (215, 170), (211, 160), (296, 130)))


def ex4():
    screen = pygame.display.set_mode((400, 600))
    rect(screen, (125, 125, 125), (0, 0, 400, 250))
    ellipse(screen, (50, 50, 50), (200, 100, 220, 30))
    ellipse(screen, (80, 80, 80), (20, 50, 250, 40))
    rect(screen, (54, 44, 18), (20, 100, 200, 300))
    rect(screen, (53, 23, 12), (50, 320, 40, 50))
    rect(screen, (53, 23, 12), (100, 320, 40, 50))
    rect(screen, (255, 255, 0), (150, 320, 40, 50))
    rect(screen, (50, 50, 50), (0, 250, 240, 30))
    for i in range(4):
        rect(screen, (172, 138, 100), (40 + i * 130 / 3, 100, 30, 150))
    for i in range(7):
        rect(screen, (50, 50, 50), (10 + i * 35, 220, 10, 30))
    rect(screen, (50, 50, 50), (20, 210, 200, 10))
    polygon(screen, (0, 0, 0), ((0, 100), (40, 70), (200, 70), (240, 100)))
    circle(screen, (255, 255, 255), (360, 40), 30)
    rect(screen, (50, 50, 50), (50, 60, 5, 30))
    rect(screen, (50, 50, 50), (140, 45, 10, 45))
    rect(screen, (50, 50, 50), (190, 40, 7, 50))
    ellipse(screen, (100, 100, 100), (180, 20, 200, 30))
    ellipse(screen, (70, 70, 70), (50, 30, 200, 30))
    rect(screen, (50, 50, 50), (70, 30, 20, 60))
    polygon(
        screen,
        (200, 200, 200),
        (
            (250, 550),
            (270, 450),
            (290, 440),
            (350, 525),
            (340, 545),
            (310, 525),
            (300, 535),
            (270, 525),
        ),
    )
    circle(screen, (200, 200, 200), (280, 445), 20)
    circle(screen, (0, 0, 0), (270, 440), 5)
    circle(screen, (0, 0, 0), (285, 440), 5)


def drawBckgrnd(scr):
    rect(scr, (125, 125, 125), (0, 0, 400, 250))


def drawHs(scr, stPnt, scl=1):
    rect(scr, (54, 44, 18), (stPnt[0], stPnt[1], 200 * scl, 300 * scl))
    rect(
        scr,
        (53, 23, 12),
        (stPnt[0] + 30 * scl, stPnt[1] + 220 * scl, 40 * scl, 50 * scl),
    )
    rect(
        scr,
        (53, 23, 12),
        (stPnt[0] + 80 * scl, stPnt[1] + 220 * scl, 40 * scl, 50 * scl),
    )
    rect(
        scr,
        (255, 255, 0),
        (stPnt[0] + 130 * scl, stPnt[1] + 220 * scl, 40 * scl, 50 * scl),
    )
    rect(
        scr,
        (50, 50, 50),
        (stPnt[0] - 20 * scl, stPnt[1] + 150 * scl, 240 * scl, 30 * scl),
    )
    for i in range(4):
        rect(
            scr,
            (172, 138, 100),
            (stPnt[0] + (20 + i * 130 / 3) * scl, stPnt[1], 30 * scl, 150 * scl),
        )
    for i in range(7):
        rect(
            scr,
            (50, 50, 50),
            (stPnt[0] - (10 - i * 35) * scl, stPnt[1] + 120 * scl, 10 * scl, 30 * scl),
        )
    rect(scr, (50, 50, 50), (stPnt[0], stPnt[1] + 110 * scl, 200 * scl, 10 * scl))
    polygon(
        scr,
        (0, 0, 0),
        (
            (stPnt[0] - 20 * scl, stPnt[1]),
            (stPnt[0] + 20 * scl, stPnt[1] - 30 * scl),
            (stPnt[0] + 180 * scl, stPnt[1] - 30 * scl),
            (stPnt[0] + 220 * scl, stPnt[1]),
        ),
    )


def drawGhst(scr, stPnt, scl=1, hScl=1):
    polygon(
        scr,
        (200, 200, 200),
        (
            (stPnt[0], stPnt[1]),
            (stPnt[0] + 20 * scl * hScl, stPnt[1] - 100 * scl),
            (stPnt[0] + 40 * scl * hScl, stPnt[1] - 110 * scl),
            (stPnt[0] + 100 * scl * hScl, stPnt[1] - 25 * scl),
            (stPnt[0] + 90 * scl * hScl, stPnt[1] - 5 * scl),
            (stPnt[0] + 60 * scl * hScl, stPnt[1] - 25 * scl),
            (stPnt[0] + 50 * scl * hScl, stPnt[1] - 15 * scl),
            (stPnt[0] + 20 * scl * hScl, stPnt[1] - 25 * scl),
        ),
    )
    circle(
        scr,
        (200, 200, 200),
        (stPnt[0] + 30 * scl * hScl, stPnt[1] - 105 * scl),
        20 * scl,
    )
    circle(scr, (0, 0, 0), (stPnt[0] + 20 * scl * hScl, stPnt[1] - 110 * scl), 5 * scl)
    circle(scr, (0, 0, 0), (stPnt[0] + 35 * scl * hScl, stPnt[1] - 110 * scl), 5 * scl)


def ex5():
    screen = pygame.display.set_mode((400, 600))
    drawBckgrnd(screen)
    drawHs(screen, (20, 220), 0.5)
    drawHs(screen, (150, 170), 0.5)
    drawHs(screen, (290, 120), 0.5)
    circle(screen, (255, 255, 255), (360, 40), 30)
    ellipse(screen, (100, 100, 100), (180, 20, 200, 30))
    ellipse(screen, (70, 70, 70), (50, 30, 200, 30))
    drawGhst(screen, (250, 550), 1, -1)
    drawGhst(screen, (250, 550))
    drawGhst(screen, (100, 550), 0.5)


if __name__ == "__main__":
    eval("ex" + input() + "()")

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
