

import heapq
import queue

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
        self.shortestPath = [] # might not be the shortest path depending on your algorithm

    def getShortestPath(self):
        return self.shortestPath

    def distance(self, from_node, to_node):
        return vec(from_node).distance_to(vec(to_node))
    
    def setShortestPath(self, parent, j):

        if not j in parent:
            return
        if parent[j] == -1:
            return
        self.shortestPath.append(vec(parent[j]))
        self.setShortestPath(parent, parent[j])

        
      
    # credit goes to https://www.youtube.com/watch?v=e3gbNOl4DiM&t=6s

    def dijkstras(self):
        path = {}
        cost = {}
        self.shortestPath = []
        frontier = PriorityQueue()
        frontier.put(self.graph.vec2int(self.start), 0)
        path[self.graph.vec2int(self.start)] = None
        cost[self.graph.vec2int(self.start)] = 0
        parent = {} ## a dictionary that will hold shortest path
        parent[self.graph.vec2int(self.start)] = -1
        
        while not frontier.empty():
            current = frontier.get() ## pop the first item off the queue
            if current == self.end:
                break
            for next in self.graph.find_neighbors(vec(current)):
                next = self.graph.vec2int(next)
                next_cost = cost[current] + self.distance(next, self.end)
    
                if next not in cost or next_cost < cost[next]:
                    parent[next] = current
                    cost[next] = next_cost
                    priority = next_cost
                    frontier.put(next, priority)
                    path[next] = vec(current) - vec(next)
        self.setShortestPath(parent, self.graph.vec2int(self.end))
        return path

    def DFS(self):
        visited = []
        currentOptions = [self.start]
        currentPath = []
        self.shortestPath = []
        path = {}
        current = 0
        while current != self.end:
            if not currentOptions:
                currentPath.pop(len(currentPath) - 1)
                if len(currentPath) == 0:
                    return path
                current = currentPath[len(currentPath) -1]
                currentOptions = self.getUnvisted(current,visited)
            else:
                newPos = currentOptions.pop(len(currentOptions) -1)
                intNewPos = self.graph.vec2int(newPos)
                path[intNewPos] = vec(current) - vec(intNewPos)
                current = newPos
                currentPath.append(newPos)
                visited.append(newPos)
                currentOptions = self.getUnvisted(current,visited)
        self.shortestPath = currentPath
        return path

    def getUnvisted(self,current,visited):
        unvisited = []
        for next in self.graph.find_neighbors(vec(current)):
            beenVisited = 0
            for vis in visited:
                if vis == next:
                    beenVisited = 1
                    break
            if beenVisited == 0:
                unvisited.append(next)
        return unvisited

    def heuristic(self,node1, node2):
        return abs(node1.x - node2.x) + (node1.y - node2.y)

    def a_star_search(self):
        frontier = PriorityQueue()
        frontier.put(self.graph.vec2int(self.start), 0)
        path = {}
        cost = {}
        path[self.graph.vec2int(self.start)] = None
        cost[self.graph.vec2int(self.start)] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == self.end:
                break
            for next in self.graph.find_neighbors(vec(current)):
                next = self.graph.vec2int(next)
                next_cost = cost[current] + 1
                if next not in cost or next_cost < cost[next]:
                    cost[next] = next_cost
                    priority = next_cost + self.distance(next, self.end)
                    frontier.put(next, priority)
                    path[next] = vec(current)
        self.shortestPath = self.get_return_path(path, self.end)
        return path

    def BFS(self):
        graph = self.graph
        current = self.start
        return_path = []
        path = {}
        search_queue = queue.Queue(0)
        search_queue.put(current)
        iterations = 0
        while not search_queue.empty():
            iterations += 1
            current = search_queue.get()
            if current == self.end:
                return_path = self.get_return_path(path, current)
                print("BFS path with length {len(return_path)}: {return_path}")
                break
            else:
                neighbors = graph.find_neighbors(current)
                for n in neighbors:
                    neighbor = self.graph.vec2int(n)
                    if neighbor not in path.keys():
                        path[neighbor] = current
                        search_queue.put(n)
        self.shortestPath = return_path
        return path

    def get_return_path(self, path, end_node):
        new_path = []
        previous = end_node
        while previous != self.start:
            current = previous
            if not self.graph.vec2int(current) in path:
                return []
            previous = path[self.graph.vec2int(current)]
            new_path.append(current)
        new_path.append(self.start)
        return new_path







    



        
