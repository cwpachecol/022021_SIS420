'''
8 puzzle problema, a smaller version of the fifteen puzzle:
http://en.wikipedia.org/wiki/Fifteen_puzzle
States are defined as string representations of the pieces on the puzzle.
Actions denote what piece will be moved to the empty space.

States must allways be inmutable. We will use strings, but internally most of
the time we will convert those strings to lists, which are easier to handle.
For example, the estado (string):

'1-2-3
 4-5-6
 7-8-e'

will become (in lists):

[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]

'''

from __future__ import print_function

from busquedas_02 import astar
from modelos import ProblemaBusqueda
from visores import WebViewer


GOAL = '''1-2-3
4-5-6
7-8-e'''

INITIAL = '''4-1-2
7-e-3
8-5-6'''


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(rows, element_to_find):
    '''Find the location of a piece in the puzzle.
       Returns a tuple: row, column'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


# we create a cache for the estado_objetivo position of each piece, so we don't have to
# recalculate them every time
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = find_location(rows_goal, number)


class EigthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        '''Returns a list of the pieces we can move to the empty space.'''
        rows = string_to_list(estado)
        row_e, col_e = find_location(rows, 'e')

        acciones = []
        if row_e > 0:
            acciones.append(rows[row_e - 1][col_e])
        if row_e < 2:
            acciones.append(rows[row_e + 1][col_e])
        if col_e > 0:
            acciones.append(rows[row_e][col_e - 1])
        if col_e < 2:
            acciones.append(rows[row_e][col_e + 1])

        return acciones

    def resultado(self, estado, accion):
        '''Return the resulting estado after moving a piece to the empty space.
           (the "accion" parameter contains the piece to move)
        '''
        rows = string_to_list(estado)
        row_e, col_e = find_location(rows, 'e')
        row_n, col_n = find_location(rows, accion)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        return list_to_string(rows)

    def es_objetivo(self, estado):
        '''Returns true if a estado is the estado_objetivo estado.'''
        return estado == GOAL

    def costo(self, state1, accion, estado2):
        '''Returns the costo of performing an accion. No useful on this problema, i
           but needed.
        '''
        return 1

    def heuristica(self, estado):
        '''Returns an *estimation* of the distancia from a estado to the estado_objetivo.
           We are using the manhattan distancia.
        '''
        rows = string_to_list(estado)

        distancia = 0

        for number in '12345678e':
            row_n, col_n = find_location(rows, number)
            row_n_goal, col_n_goal = goal_positions[number]

            distancia += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)

        return distancia


resultado = astar(EigthPuzzleProblem(INITIAL))
# if you want to use the visual debugger, use this instead:
# resultado = astar(EigthPuzzleProblem(INITIAL), visor=WebViewer())

for accion, estado in resultado.camino():
    print('Move number', accion)
    print(estado)

