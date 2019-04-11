

import heapq
import pygame as pg

vec = pg.math.Vector2

class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, distance):
        heapq.heappush(self.nodes, (distance, node))
    
    def get(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return len(self.nodes) == 0

class Algorithms:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.weights = {}

    def distance(self, from_node, to_node):
        return vec(from_node).distance_to(vec(to_node))


    def vec2int(self,v):
        return (int(v.x), int(v.y))
        
    def dijkstras(self):
        path = {}
        cost = {}
        frontier = PriorityQueue()
        frontier.put(self.vec2int(self.start), 0)
        path[self.vec2int(self.start)] = None
        cost[self.vec2int(self.start)] = 0
        
        while not frontier.empty():
            self.current = frontier.get() ## pop the first item off the queue
            if self.current == self.end:
                break
            for next in self.graph.find_neighbors(vec(self.current)):
                next = self.vec2int(next)
                next_cost = cost[self.current] + self.distance(self.current, self.end)
                if next not in cost or next_cost < cost[next]:
                    cost[next] = next_cost
                    priority = next_cost
                    frontier.put(next, priority)
                    path[next] = vec(self.current) - vec(next)
        return path







    



        
