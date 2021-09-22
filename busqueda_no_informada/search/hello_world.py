# coding=utf-8

from __future__ import print_function

from simpleai.search import SearchProblem, astar

OBJETIVO = 'HELLO WORLD'


class HelloProblem(SearchProblem):
    def acciones(self, estado):
        if len(estado) < len(OBJETIVO):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def resultado(self, estado, accion):
        return estado + accion

    def is_objetivo(self, estado):
        return estado == OBJETIVO

    def heuristica(self, estado):
        # how far are we from the objetivo?
        wrong = sum([1 if estado[i] != OBJETIVO[i] else 0
                    for i in range(len(estado))])
        missing = len(OBJETIVO) - len(estado)
        return wrong + missing

problem = HelloProblem(initial_state='')
resultado = astar(problem)

print(resultado.estado)
print(resultado.camino())
