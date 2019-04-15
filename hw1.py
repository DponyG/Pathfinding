import re
import pygame as pg
import random
import time
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
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
g = SquareGrid(GRIDWIDTH, GRIDHEIGHT, screen, WIDTH, HEIGHT)
FPS = 30


## Will be parsed by a file parser
walls = [(10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (5, 8), (12, 8), (12, 9), (12, 10), (12, 11), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 0), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (24, 10), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4)]
for wall in walls:
    g.walls.append(vec(wall))

goal = vec(1, 1)
start = vec(1, 3)


def newMap(xSize,ySize,amountOfWalls):
    global GRIDWIDTH,GRIDHEIGHT
    global g,screen,WIDTH,HEIGHT
    unknown = []
    GRIDWIDTH = int(xSize)
    GRIDHEIGHT = int(ySize)
    WIDTH = TILESIZE*GRIDWIDTH
    HEIGHT = TILESIZE*GRIDHEIGHT
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    g = SquareGrid(GRIDWIDTH, GRIDHEIGHT, screen, WIDTH, HEIGHT)
    g.walls = []
    for x in range(xSize):
        for y in range(ySize):
            unknown.append(vec(x,y))
    for w in range(amountOfWalls):
        g.walls.append(unknown.pop(random.randint(0,xSize*ySize-w-1)))
    global start, goal
    start = unknown.pop(random.randint(0,xSize*ySize-amountOfWalls-1))
    goal = unknown.pop(random.randint(0,xSize*ySize-amountOfWalls-2))
    return Algorithms(g, start, goal)

def printData(t,lenPath,total,timeTook):
    if t == "DFS":
        fh = open("DFS", "a+")
    elif t == "BFS":
        fh = open("BFS", "a+")
    elif t == "A":
        fh = open("A", "a+")
    elif t == "D":
        fh = open("D", "a+")
    performance = lenPath/total
    fh.write(str(performance) + ", " + str(timeTook) + "\n")
    fh.close()
    
## needed to display shortest path

def main():
    path = {}
    findPath = False
    running = True
    filename = "test2"
    parseFile(filename)
    algorithms = Algorithms(g, start, goal)
    timeTook = 0
    filetype = ""
    starttime = 0
    endtime = 0
    screen.fill(DARKGRAY)
    g.draw_grid()
    g.draw_wall()
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                if event.key == pg.K_d:
                    print("Dijkstras")
                    screen.fill(DARKGRAY)
                    g.draw_grid()
                    g.draw_wall()
                    starttime = time.time()
                    path = algorithms.dijkstras()
                    endtime = time.time()
                    filetype = "D"
                    findPath = True
                if event.key == pg.K_s:
                    print("DFS")
                    screen.fill(DARKGRAY)
                    g.draw_grid()
                    g.draw_wall()
                    starttime = time.time()
                    path = algorithms.DFS()
                    endtime = time.time()
                    filetype = "DFS"
                    findPath = True
                if event.key == pg.K_f:
                    print("BFS")
                    screen.fill(DARKGRAY)
                    g.draw_grid()
                    g.draw_wall()
                    starttime = time.time()
                    path = algorithms.BFS()
                    endtime = time.time()
                    filetype = "BFS"
                    findPath = True
                if event.key == pg.K_a:
                    print("ASTAR")
                    screen.fill(DARKGRAY)
                    g.draw_grid()
                    g.draw_wall()
                    starttime = time.time()
                    path = algorithms.a_star_search()
                    endtime = time.time()
                    filetype = "A"
                    findPath = True
                if event.key == pg.K_n:
                    algorithms = newMap(20,20,100)
                    screen.fill(DARKGRAY)
                    g.draw_grid()
                    g.draw_wall()

        pg.display.set_caption("{:.2f}".format(clock.get_fps()))

        if(findPath == True):
            timeTook = endtime - starttime
            
            counter = 0
            for node in path:
                x, y = node
                rect = pg.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
                pg.draw.rect(screen, MEDGRAY, rect)
                counter += 1
            print("Nodes Searched: "+ str(counter))
            printData(filetype,counter,GRIDHEIGHT*GRIDWIDTH,timeTook)
            counter = 0
            for node in algorithms.getShortestPath():
                counter += 1
                x = node.x * TILESIZE
                y = node.y * TILESIZE
                rect = pg.Rect(x, y, TILESIZE, TILESIZE)
                pg.draw.rect(screen, CYAN, rect)
            print("Path Length:" + str(counter))
            
            # current = start + path[g.vec2int(start)]

            # while current != goal:
            #     x = current.x * TILESIZE
            #     y = current.y * TILESIZE
            #     rect = pg.Rect(x, y, TILESIZE, TILESIZE)
            #     pg.draw.rect(screen, CYAN, rect)
            #     current = current + path[g.vec2int(current)]
            findPath = False
        home = pg.Rect(start.x*TILESIZE, start.y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, BLUE, home)

        end = pg.Rect(goal.x*TILESIZE, goal.y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, RED, end)
        
        pg.display.flip()

def parseFile(filename):
    global GRIDWIDTH,GRIDHEIGHT
    global g,screen,WIDTH,HEIGHT
    
    fh = open(filename, "r")
    counter = 0
    walls = []
    x = 0
    y = -1
    for line in fh:
        if counter == 0:
            garbage,parms = int, re.findall(r'\d+', line)
            GRIDWIDTH = int(parms[0])
            GRIDHEIGHT = int(parms[1])
            WIDTH = TILESIZE*GRIDWIDTH
            HEIGHT = TILESIZE*GRIDHEIGHT
            g = SquareGrid(GRIDWIDTH, GRIDHEIGHT, screen, WIDTH, HEIGHT)
            screen = pg.display.set_mode((WIDTH, HEIGHT))
            counter += 1
        else:
            for char in line:
                if char =='#':
                    walls.append((x,y))
                    g.walls.append(vec(x,y))
                elif char == 'S':
                    global start 
                    start = vec(x,y)
                elif char == 'E':
                    global goal 
                    goal = vec(x,y)
                x += 1
            x = 0
        y += 1
    fh.close()
    
    return start,goal

if __name__ == '__main__':
    main()
