#!/usr/bin/env python

"""code template"""

import random
import numpy as np

from graphics import *
from gridutil import *
from agent import *
from env import *


def main():
    # comment to get different scenarios
    random.seed(13)
    # rate of executing actions
    rate = 1
    # size of the environment
    env_size = 32
    eps_move = 0.02
    eps_perc = 0.015
    # map of the environment: 1 - wall, 0 - free
    map = np.zeros((env_size, env_size))
    # build the list of walls locations
    walls = []
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i, j] == 1:
                walls.append((j, env_size - i - 1))

    # list of valid locations
    locs = list({*locations(env_size)}.difference(walls))
    # start and goal location
    start = (0, env_size // 2)

    # create the environment and viewer
    env = LocWorldEnv(env_size, walls, start, eps_move, eps_perc)
    view = LocView(env)

    # create the agent
    agent = Agent(env.size, env.walls, env.agentLoc,
                  env.agentDir, eps_move, eps_perc)
    t = 0
    while t != 40:
        print('\nstep %d' % t)

        print('performing action')
        # get agent's action and execute it
        action = agent()
        print('action: ', action)
        env.doAction(action)

        P = agent.get_posterior()
        view.update(env, P)
        update(rate)
        # uncomment to pause before action
        view.pause()

        print('performing perception')
        percept = env.getPercept()
        print('percept: ', percept)
        print('true loc: %d' % env.agentLoc[0])
        agent.correct_posterior(percept)

        P = agent.get_posterior()
        view.update(env, P)
        update(rate)
        # uncomment to pause before action
        view.pause()

        t += 1

    # pause until mouse clicked
    view.pause()


if __name__ == '__main__':
    main()
