# prob.py
# This is

import random
import numpy as np
import queue

from gridutil import *


class Agent:
    def __init__(self, size, walls, loc, dir, goal):
        self.size = size
        self.walls = walls
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal

        self.t = 0
        # graf se rb
        self.nodes = {loc:self.make_new_locs(loc) for loc in self.locations}
        self.path = self.find_path()
        #print(self.locations)

    def __call__(self):
        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE
        actions = {
            (-1, 0): 'W',
            (1, 0): 'E',
            (0, 1): 'N',
            (0, -1): 'S'
        }


        if self.loc == self.path[0]:
            self.path.pop(0)

        dir = tuple(map(lambda i,j: j-i, self.loc, self.path[0]))      
        self.loc = self.path[0]
        # ------------------

        return actions[dir]

    def make_new_locs(self, pos):
        x, y = pos

        new_locs = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        return [new_loc for new_loc in new_locs if new_loc in self.locations]

    def find_path(self):
        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE
        
        #print(self.graph)
        start_edge = self.loc
        end_edge = self.goal

        current_edge = start_edge
        edges_queue = queue.Queue()
        edges_queue.put(start_edge)
        visited = [False for _ in enumerate(self.nodes)]
        visited[self.loc_to_idx[start_edge] - 1] = True
        previous_edge = [-1 for _ in enumerate(self.nodes)]

        while current_edge != end_edge:
            current_edge = edges_queue.get()

            for edge in self.nodes.get(current_edge):
                if not visited[self.loc_to_idx[edge] - 1]:
                    edges_queue.put(edge)
                    visited[self.loc_to_idx[edge] - 1] = True
                    previous_edge[self.loc_to_idx[edge] - 1] = current_edge

        path = []
        while current_edge != -1:
            path.append(current_edge)
            current_edge = previous_edge[self.loc_to_idx[current_edge] - 1]
        
        path.reverse()
        return path

    def get_path(self):
        return self.path
