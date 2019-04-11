## GRAPHICS WAS TAKEN FROM TUTORIAL
## https://www.youtube.com/watch?v=JZsJq47hqVg

from variables import *
import pygame as pg
vec = pg.math.Vector2


class SquareGrid:
    def __init__(self, GRIDWIDTH, GRIDHEIGHT, screen, WIDTH, HEIGHT):
        self.screen = screen
        self.GRIDWIDTH = GRIDWIDTH
        self.GRIDHEIGHT = GRIDHEIGHT
        self.walls = []
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]

        self.TILESIZE = 48
        self.WIDTH = WIDTH
        self.HEIGHT= HEIGHT


        ##  COLOR CONSTANTS
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.MAGENTA = (255, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.DARKGRAY = (40, 40, 40)
        self.LIGHTGRAY = (140, 140, 140)
  
    def in_bounds(self, node):
        return 0 <= node.x < self.GRIDWIDTH and 0 <= node.y < self.GRIDHEIGHT

    def passable(self, node):
        return node not in self.walls

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def draw_wall(self):
        for wall in self.walls:
            rect = pg.Rect(wall * self.TILESIZE, (self.TILESIZE, self.TILESIZE))
            pg.draw.rect(self.screen, self.LIGHTGRAY, rect)
    
    def vec2int(v):
        return (int(v.x), int(v.y))

    def draw_grid(self):
        for x in range(0, self.WIDTH, self.TILESIZE):
            pg.draw.line(self.screen, self.LIGHTGRAY, (x, 0), (x, self.HEIGHT))
        for y in range(0, self.HEIGHT, self.TILESIZE):
            pg.draw.line(self.screen, self.LIGHTGRAY, (0, y), (self.WIDTH, y))




