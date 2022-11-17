from graphics import *
from gridutil import *

import random


class LocWorldEnv:
    actions = "turnleft turnright forward".split()

    def __init__(self, size, walls, doors, start_loc, eps_move, eps_perc_true, eps_perc_false):
        self.size = size
        self.walls = walls
        self.doors = doors
        self.action_sensors = []
        self.locations = {*locations(self.size)}.difference(self.walls)
        self.start_loc = start_loc
        self.eps_move = eps_move
        self.eps_perc_true = eps_perc_true
        self.eps_perc_false = eps_perc_false
        self.lifes = 3
        self.reset()
        self.finished = False

    def reset(self):
        self.agentLoc = self.start_loc
        self.agentDir = 'N'

    def getPercept(self):
        rand_val = random.random()
        # we are next to a door
        if self.agentLoc[0] in self.doors:
            # chance that measurement is incorrect
            if rand_val < self.eps_perc_true:
                percept = False
            else:
                percept = True
        else:
            # chance that measurement is incorrect
            if rand_val < self.eps_perc_false:
                percept = True
            else:
                percept = False

        return percept

    def doAction(self, action):
        points = -1

        rand_val = random.random()
        if rand_val < 2 * self.eps_move:
            action -= 1
        elif rand_val < 3 * self.eps_move:
            action -= 2
        elif rand_val < 5 * self.eps_move:
            action += 1
        elif rand_val < 6 * self.eps_move:
            action += 2

        print('executed action ', action)
        # self.agentLoc = (min(max(self.agentLoc[0] + action, 0), self.size - 1), self.agentLoc[1])
        self.agentLoc = ((self.agentLoc[0] + action) % self.size, self.agentLoc[1])

        return points  # cost/benefit of action


class LocView:
    # LocView shows a view of a LocWorldEnv. Just hand it an env, and
    #   a window will pop up.

    Size = .5
    Points = {'N': (0, -Size, 0, Size), 'E': (-Size, 0, Size, 0),
              'S': (0, Size, 0, -Size), 'W': (Size, 0, -Size, 0)}

    color = "black"

    def __init__(self, state, height=800, title="Loc World"):
        xySize = state.size
        win = self.win = GraphWin(title, 1.33 * height, height, autoflush=False)
        win.setBackground("gray99")
        win.setCoords(-.5, -.5, 1.33 * xySize - .5, xySize - .5)
        cells = self.cells = {}
        for x in range(xySize):
            for y in range(xySize):
                cells[(x, y)] = Rectangle(Point(x - .5, y - .5), Point(x + .5, y + .5))
                cells[(x, y)].setWidth(0)
                cells[(x, y)].draw(win)
        self.agt = None
        self.arrow = None
        self.prob_prim = []
        ccenter = 1.167 * (xySize - .5)
        # self.time = Text(Point(ccenter, (xySize - 1) * .75), "Time").draw(win)
        # self.time.setSize(36)
        # self.setTimeColor("black")

        self.agentName = Text(Point(ccenter, (xySize - 1) * .5), "").draw(win)
        self.agentName.setSize(20)
        self.agentName.setFill("Orange")

        self.info = Text(Point(ccenter, (xySize - 1) * .25), "").draw(win)
        self.info.setSize(20)
        self.info.setFace("courier")

        self.update(state, [])

    def setAgent(self, name):
        self.agentName.setText(name)

    # def setTime(self, seconds):
    #     self.time.setText(str(seconds))

    def setInfo(self, info):
        self.info.setText(info)

    def update(self, state, P):
        # View state in exiting window
        for loc, cell in self.cells.items():
            if loc in state.walls:
                cell.setFill("black")
            # next to a door
            if loc[0] in state.doors and loc[1] == state.size // 2:
                cell.setFill("brown")
            else:
                cell.setFill("white")

        for prim in self.prob_prim:
            prim.undraw()
        self.prob_prim = []
        for i in range(len(P)):
            self.prob_prim.append(self.drawRect((i, state.agentLoc[1] + 2), P[i]))

        if self.agt:
            self.agt.undraw()
        if state.agentLoc:
            self.agt = self.drawArrow(state.agentLoc, state.agentDir, 5, self.color)

    def drawRect(self, loc, height, color="blue"):
        x, y = loc
        a = Rectangle(Point(x - .5, y - .5), Point(x + .5, y - .5 + 4 * height))
        a.setWidth(0)
        a.setFill(color)
        a.draw(self.win)
        return a

    def drawDot(self, loc, color="blue"):
        x, y = loc
        a = Circle(Point(x, y), .1)
        a.setWidth(1)
        a.setFill(color)
        a.draw(self.win)
        return a

    def drawLine(self, loc1, loc2, color="blue"):
        x1, y1 = loc1
        x2, y2 = loc2
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        a = Line(p1, p2)
        a.setWidth(2)
        a.setFill(color)
        a.draw(self.win)
        return a

    def drawArrow(self, loc, heading, width, color):
        x, y = loc
        dx0, dy0, dx1, dy1 = self.Points[heading]
        p1 = Point(x + dx0, y + dy0)
        p2 = Point(x + dx1, y + dy1)
        a = Line(p1, p2)
        a.setWidth(width)
        a.setArrow('last')
        a.setFill(color)
        a.draw(self.win)
        return a

    def pause(self):
        self.win.getMouse()

    # def setTimeColor(self, c):
    #     self.time.setTextColor(c)

    def close(self):
        self.win.close()
