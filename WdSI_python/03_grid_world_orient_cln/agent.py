# prob.py
# This is

import random
import numpy as np
import queue
import math

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
        self.nodes = self.make_graph()
        self.path, self.actions = self.find_path()

    def make_graph(self):
        dirs = ['N', 'W', 'S', 'E']
        nodes = dict()

        for pos in self.locations:
            for facing in dirs:
                nodes[(pos[0], pos[1], facing)] = self.get_available_neighbours(pos, facing)
                
        return nodes

    def get_available_neighbours(self, pos, facing):
        x, y = pos

        new_locs = {
            'E': (x+1, y),
            'W': (x-1, y),
            'N': (x, y+1),
            'S': (x, y-1)
        }

        costs = {}
        if facing == 'N':
            costs = {
                'N': 'forward',
                'W': 'turnleft',
                'E': 'turnright',
            }
            del new_locs['S']
        elif facing == 'S':
            costs = {
                'W': 'turnright',
                'E': 'turnleft',
                'S': 'forward'
            }
            del new_locs['N']
        elif facing == 'E':
            costs = {
                'N': 'turnleft',
                'S': 'turnright',
                'E': 'forward'
            }
            del new_locs['W']
        elif facing == 'W':
            costs = {
                'N': 'turnright',
                'S': 'turnleft',
                'W': 'forward',
            }
            del new_locs['E']

        ret = []
        
        for dir, new_loc in new_locs.items():
            if new_loc in self.locations:
                ret.append( 
                    ((new_loc[0], new_loc[1], dir), costs[dir])
                )

        return ret

    def __call__(self):
        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE
        action = self.actions[0]
        if self.loc == self.path[0]:

            self.path.pop(0)
        if action == 'forward':
            self.actions.pop(0)
            self.loc = self.path[0]
        else:
            self.actions[0] = 'forward'

        return action

        # ------------------

    def find_path(self):
        costs = {
            'turnleft': 5,
            'turnright': 2,
            'forward': 1
        }

        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE
        
        start_node = (self.loc[0], self.loc[1], self.dir)
        end_node = self.goal

        q = queue.PriorityQueue()
        q.put((0, start_node))  # wartosc node_id

        total_cost = {n: math.inf for n in self.nodes}
        total_cost[start_node] = 0

        parent = {n: None for n in self.nodes}
        parent_actions = {n: None for n in self.nodes}
        visited = set()
        curr_node = None

        while not q.empty():
            _, curr_node = q.get()

            if curr_node in visited:
                continue

            visited.add(curr_node)

            if curr_node[0] == end_node[0] and curr_node[1] == end_node[1]:
                break

            for node, cost in self.nodes[curr_node]:
                if node in visited:
                    continue

                old_cost = total_cost[node]
                new_cost = total_cost[curr_node] + costs[cost]
                if new_cost < old_cost:
                    total_cost[node] = new_cost
                    parent[node] = curr_node
                    parent_actions[node] = cost
                    q.put((new_cost, node))

        path = []
        actions = []
        while curr_node:
            path.append(curr_node)
            if parent_actions[curr_node]:
                actions.append(parent_actions[curr_node])
            curr_node = parent[curr_node]
        path.reverse()
        actions.reverse()
        # ------------------

        return path, actions

    def get_path(self):
        return self.path
