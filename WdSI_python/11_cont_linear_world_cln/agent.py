# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, sigma_move, sigma_perc):
        self.size = size
        self.sigma_sq_move = sigma_move ** 2
        self.sigma_sq_perc = sigma_perc ** 2
        # list of valid locations
        self.locations = [loc for loc in range(size)]
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.action_dir = -1

        self.t = 0
        self.n = 20

        # create an initial particle set as 1-D numpy array (self.p)
        # and initial weights as 1-D numpy array (self.w)
        # TODO PUT YOUR CODE HERE
        self.sigma_perc = sigma_perc
        self.sigma_move = sigma_move
        self.p = np.random.randint(self.n, size=self.n)
        self.w = np.ones_like(self.p) * 1/self.n
        # ------------------

    def __call__(self):
        # if reached one of the ends then start moving in the opposite direction
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

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        self.p = self.p + action + self.sigma_move * np.random.randn(self.n)
        # ------------------

        # this function does not return anything
        return

    def calculate_weights(self, percept):
        # calculate weights using percept
        # TODO PUT YOUR CODE HERE
        N_mu = lambda mu: 0.5/self.sigma_perc/math.sqrt(2*np.pi) * np.exp(-(percept-mu)**2/2/self.sigma_sq_perc)
        self.w = np.array([N_mu(p_i) for p_i in self.p])
        self.w /= sum(self.w) # normalize
        # ------------------

        # this function does not return anything
        return

    def correct_posterior(self):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE
        
        # ------------------

        # this function does not return anything
        return

    def get_particles(self):
        return self.p

    def get_weights(self):
        return self.w
