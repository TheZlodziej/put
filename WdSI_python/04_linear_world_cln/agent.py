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
        self.predict_posterior(action)

        # ------------------

        return action

    def norm_P(self):
        self.P = [i/sum(self.P) for i in self.P]  # zeby sie dodaly do 1

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        actions_with_probability = {
            0: 1-6*self.eps_move,
            -1: 2*self.eps_move,
            1: 2*self.eps_move,
            -2: self.eps_move,
            2: self.eps_move,
        }

        old_P = self.P
        self.P = np.zeros(self.size)

        for xt in range(self.size):
            for curr_action, prob in actions_with_probability.items():
                curr_xt_offset = action + curr_action + xt
                if curr_xt_offset >= 0 and curr_xt_offset < self.size:
                    self.P[curr_xt_offset] += old_P[xt]*prob

        self.norm_P()
        # ------------------
        return

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        percepts_with_probability = {  # P(z_t | x_t)
            percept+0: 1-6*self.eps_perc,
            percept-1: 2*self.eps_perc,
            percept+1: 2*self.eps_perc,
            percept-2: self.eps_perc,
            percept+2: self.eps_perc,
        }

        old_P = self.P
        self.P = np.zeros(self.size)

        for sensor_pos, prob in percepts_with_probability.items():
            if sensor_pos >= 0 and sensor_pos < self.size:
                self.P[sensor_pos] = old_P[sensor_pos]*prob

        self.norm_P()
        # ------------------

    def get_posterior(self):
        return self.P
