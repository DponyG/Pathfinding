

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


    def printPath(self, parent, j):

        if parent[j] == -1:
            return


        self.printPath(parent, parent[j])

      
    # credit goes to https://www.youtube.com/watch?v=e3gbNOl4DiM&t=6s
    def dijkstras(self):
        path = {}
        cost = {}
        frontier = PriorityQueue()
        frontier.put(self.graph.vec2int(self.start), 0)
        path[self.graph.vec2int(self.start)] = None
        cost[self.graph.vec2int(self.start)] = 0
        parent = {} ## a dictionary that will hold shortest path
        parent[self.graph.vec2int(self.start)] = -1
        
        while not frontier.empty():
            minDistance = 1000
            current = frontier.get() ## pop the first item off the queue
            if current == self.end:
                break
            for next in self.graph.find_neighbors(vec(current)):
                next = self.graph.vec2int(next)
                next_cost = cost[current] + self.distance(next, self.end)
    
                if next not in cost or next_cost < cost[next]:
                    if next_cost < minDistance:
                        minDistance = next_cost
                        parent[next] = current
                        cost[next] = next_cost
                        priority = next_cost
                        frontier.put(next, priority)
                        path[next] = vec(current) - vec(next)
        return path









    



        
