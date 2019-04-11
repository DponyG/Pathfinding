
import pygame as pg
from os import path
from variables import *
from grid import SquareGrid
from algorithm import Algorithms

vec = pg.math.Vector2

TILESIZE = 48
GRIDWIDTH = 28
GRIDHEIGHT = 15
WIDTH = TILESIZE*GRIDWIDTH
HEIGHT= TILESIZE*GRIDHEIGHT
DARKGRAY = (40, 40, 40)
MEDGRAY = (75, 75, 75)
CYAN = (0, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

FPS = 30
g = SquareGrid(GRIDWIDTH, GRIDHEIGHT, screen, WIDTH, HEIGHT)

## Will be parsed by a file parser
walls = [(10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (5, 8), (12, 8), (12, 9), (12, 10), (12, 11), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (22, 5), (23, 5), (24, 5), (25, 5), (18, 10), (20, 10), (19, 10), (21, 10), (22, 10), (23, 10), (14, 4), (14, 5), (14, 6), (14, 0), (14, 1), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 0), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (24, 10), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4)]
for wall in walls:
    g.walls.append(vec(wall))

goal = vec(8, 8)
start = vec(15, 9)



## needed to display shortest path
def vec2int(v):
    return (int(v.x), int(v.y))

def main():
    path = {}
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    d = Algorithms(g, start, goal)
                    path = d.dijkstras()
                   
        screen.fill(DARKGRAY)
                   
        for node in path:
            x, y = node
            rect = pg.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(screen, MEDGRAY, rect)
                     
        pg.display.set_caption("{:.2f}".format(clock.get_fps()))
        g.draw_grid()
        g.draw_wall()

        # current = start + path[vec2int(start)]
        # while current != goal:
        #     x = current.x * TILESIZE
        #     y = current.y * TILESIZE
        #     rect = pg.Rect(x, y, TILESIZE, TILESIZE)
        #     pg.draw.rect(screen, CYAN, rect)
        #     current = current + path[vec2int(current)]
        
        home = pg.Rect(start.x*TILESIZE, start.y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, BLUE, home)

        end = pg.Rect(goal.x*TILESIZE, goal.y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, RED, end)
        
        pg.display.flip()



if __name__ == '__main__':
    main()