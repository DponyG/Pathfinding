

import heapq
import pygame as pg

vec = pg.math.Vector2

class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, distance):
        heapq.heappush(self.nodes, (cost, node))
    
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
        return from_node.distance_to(to_node)


    def vec2int(v):
        return (int(v.x), int(v.y))
        

    def dijkstras(self):
        frontier = PriorityQueue()
        frontier.put[(vec2int(start))] = None
        cost[vec2int(start)] = 0
        path = {}
        cost = {}

        while not frontier.empty():
            self.current = frontier.get() ## pop the first item off the queue
            if self.current == self.end:
                break
            for next in graph.find_neighbors(vec(self.current)):
                next = self.vec2int(next)
                next_cost = cost[self.current] + self.distance(self.current, next)
                if next not in cost or next_cost < cost[next]:
                    cost[next] = next_cost
                    priority = next_cost
                    frontier.put(next, priority)
                    path[next] = vec(self.current) - vec(next)
        return path







    



        
