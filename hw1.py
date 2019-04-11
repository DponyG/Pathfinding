
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
walls = [(10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (5, 8), (12, 8), (12, 9), (12, 10), (12, 11), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 0), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (24, 10), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4)]
for wall in walls:
    g.walls.append(vec(wall))

goal = vec(, 4)
start = vec(20, 0)



## needed to display shortest path

def main():
    path = {}
    findPath = False
    running = True
    filename = "test"
    start,goal = parseFile(filename)
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
                    d = Algorithms(g, goal, start )
                    path = d.dijkstras()
                    findPath = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    d = Algorithms(g, goal, start)
                    path = d.DFS()
                    findPath = True
                   
        screen.fill(DARKGRAY)
                   
        for node in path:
            x, y = node
            rect = pg.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(screen, MEDGRAY, rect)
                     
        pg.display.set_caption("{:.2f}".format(clock.get_fps()))
        g.draw_grid()
        g.draw_wall()


        if(findPath == True):
            for node in d.getShortestPath():
                x = node.x * TILESIZE
                y = node.y * TILESIZE
                rect = pg.Rect(x, y, TILESIZE, TILESIZE)
                pg.draw.rect(screen, CYAN, rect)

            # current = start + path[g.vec2int(start)]

            # while current != goal:
            #     x = current.x * TILESIZE
            #     y = current.y * TILESIZE
            #     rect = pg.Rect(x, y, TILESIZE, TILESIZE)
            #     pg.draw.rect(screen, CYAN, rect)
            #     current = current + path[g.vec2int(current)]
        
        home = pg.Rect(start.x*TILESIZE, start.y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, BLUE, home)

        end = pg.Rect(goal.x*TILESIZE, goal.y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, RED, end)
        
        pg.display.flip()

def parseFile(filename):
    fh = open(filename, "r")
    counter = 0
    walls = []
    g.walls = []
    x = 0
    y = 0
    for line in fh:
        if counter == 0:
            sizeData = line
            counter += 1
        else:
            for char in line:
                if char =='#':
                    walls.append((x,y))
                    g.walls.append(vec(x,y))
                elif char == 'S':
                    start = vec(x,y)
                elif char == 'E':
                    goal = vec(x,y)
                x += 1
            x = 0
        y += 1
    fh.close()
    return start,goal

if __name__ == '__main__':
    main()
