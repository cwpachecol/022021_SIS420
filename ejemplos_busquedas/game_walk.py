#!/usr/bin/env python
# coding: utf-8

import math
from busquedas_02 import astar
from modelos import ProblemaBusqueda

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


class GameWalkPuzzle(ProblemaBusqueda):

    def __init__(self, board):
        self.board = board
        self.estado_objetivo = (0, 0)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.estado_inicial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.estado_objetivo = (x, y)

        super(GameWalkPuzzle, self).__init__(estado_inicial = self.estado_inicial)

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

    def es_objetivo(self, estado):
        return estado == self.estado_objetivo

    def costo(self, estado, accion, state2):
        return COSTS[accion]

    def heuristica(self, estado):
        x, y = estado
        gx, gy = self.estado_objetivo
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


def main():
    problem = GameWalkPuzzle(MAP)
    resultado = astar(problem, busqueda_grafo = True)
    path = [x[1] for x in resultado.camino()]

    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if (x, y) == problem.estado_inicial:
                print("o", end='')
            elif (x, y) == problem.estado_objetivo:
                print("x", end='')
            elif (x, y) in path:
                print("·", end='')
            else:
                print(MAP[y][x], end='')
        print()


if __name__ == "__main__":
    main()
