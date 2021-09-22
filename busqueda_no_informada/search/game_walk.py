#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import math
from simpleai.search import SearchProblem, astar

MAP = """
##############################
#         #              #   #
# ####    ########       #   #
#  o #    #              #   #
#    ###     ####   ######   #
#         ####      #        #
#            #  #   #   #### #
#     ######    #       # x  #
#        #      #            #
##############################
"""
MAP = [list(x) for x in MAP.split("\n") if x]

COSTS = {
    "up": 1.0,
    "down": 1.0,
    "left": 1.0,
    "right": 1.0,
    "up left": 1.4,
    "up right": 1.4,
    "down left": 1.4,
    "down right": 1.4,
}


class GameWalkPuzzle(SearchProblem):

    def __init__(self, board):
        self.board = board
        self.objetivo = (0, 0)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.objetivo = (x, y)

        super(GameWalkPuzzle, self).__init__(initial_state=self.initial)

    def acciones(self, estado):
        acciones = []
        for accion in list(COSTS.keys()):
            newx, newy = self.resultado(estado, accion)
            if self.board[newy][newx] != "#":
                acciones.append(accion)
        return acciones

    def resultado(self, estado, accion):
        x, y = estado

        if accion.count("up"):
            y -= 1
        if accion.count("down"):
            y += 1
        if accion.count("left"):
            x -= 1
        if accion.count("right"):
            x += 1

        new_state = (x, y)
        return new_state

    def is_objetivo(self, estado):
        return estado == self.objetivo

    def cost(self, estado, accion, state2):
        return COSTS[accion]

    def heuristica(self, estado):
        x, y = estado
        gx, gy = self.objetivo
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


def main():
    problem = GameWalkPuzzle(MAP)
    resultado = astar(problem, graph_search=True)
    camino = [x[1] for x in resultado.camino()]

    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if (x, y) == problem.initial:
                print("o", end='')
            elif (x, y) == problem.objetivo:
                print("x", end='')
            elif (x, y) in camino:
                print("·", end='')
            else:
                print(MAP[y][x], end='')
        print()


if __name__ == "__main__":
    main()
