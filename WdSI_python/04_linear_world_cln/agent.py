# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, walls, loc, dir, eps_move, eps_perc):
        self.size = size
        self.walls = walls
        self.eps_move = eps_move
        self.eps_perc = eps_perc
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.action_dir = 1

        self.t = 0
        self.P = np.zeros(self.size, dtype=np.float)
        # we start from 0
        self.P[loc[0]] = 1.0

    def __call__(self):
        # most probable location
        loc = np.argmax(self.P)
        # if reached one of the ends then start moving in the opposite direction
        if (self.action_dir == 1 and loc == self.size - 1) or \
           (self.action_dir == -1 and loc == 0):
            self.action_dir *= -1

        # move by one or two cells
        action = self.action_dir * np.random.choice([1, 2])

        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE


        # ------------------

        return action

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        possible_actions_with_probability = {
            action+0: 1-6*self.eps_move,
            action-1: 2*self.eps_move,
            action+1: 2*self.eps_move,
            action-2: self.eps_move,
            action+2: self.eps_move,
        }
        
        for xt in range(len(self.P)):
            for new_act, prob in enumerate(possible_actions_with_probability):
                if new_act >= 0 and new_act < len(self.P):
                    self.P[xt+new_act] *= prob 
            
        print(self.P)
        # ------------------
        return

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        # print(self.P)
        pass
        #for xt in range(1, len(self.P)):

        # ------------------

    def get_posterior(self):
        return self.P
