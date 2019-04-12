from algorithm import Algorithms
import queue


class BreadthFirstSearch(Algorithms):
    def __init__(self, graph, start, end):
        super().__init__(graph, start, end)

    def get_path(self):
        graph = self.graph
        current = self.start
        paths = []
        path = {}
        search_queue = queue.Queue(0)
        search_queue.put(current)
        iterations = 0
        while not search_queue.empty():
            iterations += 1
            current = search_queue.get()
            if current == self.end:
                path_length = self.get_path_length(path, current)
                paths.append((current, path_length))
            else:
                neighbors = graph.find_neighbors(current)
                for n in neighbors:
                    neighbor = self.vec2int(n)
                    if neighbor not in path.keys():
                        path[neighbor] = current
                        search_queue.put(n)

        min_path, min_length = paths[0]
        for possible_path, length in paths:
            if length < min_length:
                min_path = possible_path
                min_length = length
        return_path = self.get_path_from_end(path, min_path)
        print(f"BFS path with length {min_length}: {return_path}")
        return return_path

    def get_path_length(self, path, end_node):
        length = 0
        previous = end_node
        while previous != self.start:
            previous = path[self.vec2int(previous)]
            length += 1
        return length

    def get_path_from_end(self, path, end_node):
        new_path = {}
        previous = end_node
        while previous != self.start:
            current = previous
            previous = path[self.vec2int(current)]
            new_path[self.vec2int(previous)] = current
        return new_path
