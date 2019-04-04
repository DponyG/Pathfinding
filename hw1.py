
import pygame as pg
from os import path
from variables import *
from grid import SquareGrid

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
g = SquareGrid(GRIDWIDTH, GRIDHEIGHT)


def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.set_caption("{:.2f}".format(clock.get_fps()))
        screen.fill(DARKGRAY)
        draw_grid()
        g.draw_wall()
        pg.display.flip()

if __name__ == '__main__':
    main()