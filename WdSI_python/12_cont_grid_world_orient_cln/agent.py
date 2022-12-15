# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, landmarks, sigma_move_fwd, sigma_move_turn, sigma_perc):
        self.size = size
        self.landmarks = landmarks
        self.sigma_move_fwd = sigma_move_fwd
        self.sigma_move_turn = sigma_move_turn
        self.sigma_perc = sigma_perc

        self.t = 0
        self.n = 500
        # create an initial particle set as 2-D numpy array with size (self.n, 3) (self.p)
        # and initial weights as 1-D numpy array (self.w)
        # TODO PUT YOUR CODE HERE
        self.p = np.array([[np.random.randint(self.size), np.random.randint(self.size), np.random.random()*2*np.pi] for _ in range(self.n)])
        print(self.p)
        self.w = np.ones(self.n) * 1/self.n
        # ------------------

    def __call__(self):
        # turn by -pi/20.0 and move forward by 1
        action = (-math.pi/20, 1.0)
        # no turn, only move forward by 1.0
        # action = (0.0, 1.0)

        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE
        self.predict_posterior(action)
        # ------------------

        self.t += 1

        return action

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        turn, dist = action

        for i, state in enumerate(self.p):
            x, y, rot = tuple(state)
            
            rot += turn + self.sigma_move_turn * np.random.randn()
            
            dx = dist*np.cos(rot)
            x += dx + self.sigma_move_fwd * np.random.randn()
            
            dy = dist*np.sin(rot)
            y += dy + self.sigma_move_fwd * np.random.randn()

            self.p[i] = [x, y, rot]
        # ------------------

        # this function does not return anything
        return

    def calculate_weights(self, percept):
        # calculate weights using
        # TODO PUT YOUR CODE HERE


        # TU JEST ZLE!!! percept zwraca odleglosc do jednego i drugiego markera
        move_perc, orient_perc = percept

        N_mu = lambda x, mu: 0.5/math.sqrt(self.sigma_perc*2*np.pi) * np.exp(-(x-mu)**2/2/self.sigma_perc)
        self.w = np.array([N_mu(move_perc, state[0]) * N_mu(move_perc, state[1]) * N_mu(orient_perc, state[2]) for state in self.p])
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
