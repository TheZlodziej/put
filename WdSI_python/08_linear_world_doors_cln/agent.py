# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, doors, eps_move, eps_perc_true, eps_perc_false):
        self.size = size
        self.doors = doors
        self.eps_move = eps_move
        self.eps_perc_true = eps_perc_true
        self.eps_perc_false = eps_perc_false
        # list of valid locations
        self.locations = [loc for loc in range(self.size)]
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.action_dir = -1

        self.t = 0
        self.P = 1.0 / self.size * np.ones(self.size, dtype=np.float)

    def __call__(self):
        # change direction after 20 steps
        if self.t % 20 == 0:
            self.action_dir *= -1

        # move by one or two cells
        action = self.action_dir * np.random.choice([1, 2])

        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE
        self.predict_posterior(action)
        # ------------------

        self.t += 1

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
                curr_xt_offset = (action + curr_action + xt) % self.size
                # if curr_xt_offset >= 0 and curr_xt_offset < self.size:
                self.P[curr_xt_offset] += old_P[xt]*prob
                
        self.norm_P()

        # ------------------

        return

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        
        # percept = false
        print("curwa",self.doors)
        for i in range(0, self.size):
            doors_in_P_i = i in self.doors

            prob = -1

            if doors_in_P_i and percept:
                prob = 1 - self.eps_perc_true

            if doors_in_P_i and not percept:
                prob = self.eps_perc_true

            if not doors_in_P_i and percept:
                prob = self.eps_perc_false

            if not doors_in_P_i and not percept:
                prob = 1 - self.eps_perc_false
            
            self.P[i] *= prob
            
        self.norm_P()

        # ------------------

    def get_posterior(self):
        return self.P
