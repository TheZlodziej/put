# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, walls, graph, loc, dir, goal, edges_len):
        self.size = size
        self.walls = walls
        self.graph = graph
        # list of valid locations
        self.locations = list(self.graph.keys())
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal
        self.costs = edges_len

        self.t = 0
        self.path = self.find_path()

    def __call__(self):
        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE

        if self.loc == self.path[0]:
            self.path.pop(0)

        self.loc = self.path[0]
        # ------------------

        return self.path[0]

    def find_path(self):
        start_node = self.loc
        end_node = self.goal

        q = queue.PriorityQueue()
        q.put((0, start_node))  # wartosc node_id

        total_cost = {n: math.inf for n in self.graph}
        total_cost[start_node] = 0

        parent = {n: None for n in self.graph}
        visited = set()

        while not q.empty():
            _, curr_node = q.get()

            if curr_node in visited:
                continue
            visited.add(curr_node)

            if curr_node == end_node:
                break

            for node in self.graph[curr_node]:
                if node in visited:
                    continue
                
                cost = self.costs[node]

                old_cost = total_cost[node]
                new_cost = total_cost[curr_node] + cost
                if new_cost < old_cost:
                    total_cost[node] = new_cost
                    parent[node] = curr_node
                    q.put((new_cost, node))

        path = []
        curr_node = end_node
        while curr_node:
            path.append(curr_node)
            curr_node = parent[curr_node]
        path.reverse()

        return path

    def get_path(self):
        return self.path
