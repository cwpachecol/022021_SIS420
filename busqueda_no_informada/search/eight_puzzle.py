'''
problem rompecabezas de 8 piezas:

Los estados son definidos como strings que representan las piesas sobre el rompecabezas
Las acciones denotan que pieza se puede mover a un espacio vacio.
Los estados siempre deben ser inmutables. 
Usaremos cadenas, pero internamente la mayoría de las veces convertiremos 
esas cadenas en listas, que son más fáciles de manejar.
Por ejemplo, el estado (cadena):
'1-2-3
 4-5-6
 7-8-e'

se convertirá (en listas):

[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]

'''

from busquedas_01 import *

OBJETIVO = "1-2-3\n4-5-6\n7-8-e"

INICIAL = "1-2-3\n4-5-6\n7-e-8"

def list_a_string(lista_):
    return '\n'.join(['-'.join(fila) for fila in lista_])

def string_a_lista(cadena_caracteres_):
    return [fila.split('-') for fila in cadena_caracteres_.split('\n')]

def encontrar_ubicacion(filas, elemento_a_encontrar):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       Devuelve una tupla: fila, columna'''
    for ir, fila in enumerate(filas):
        for ic, element in enumerate(fila):
            if element == elemento_a_encontrar:
                return ir, ic

# Se crea un caché para la posición objetivo de cada pieza, 
# por lo que no tenemos que volver a calcularlas cada vez.

objetivo_posiciones = {}
filas_objetivo = string_a_lista(OBJETIVO)
for numero in '12345678e':
    objetivo_posiciones[numero] = encontrar_ubicacion(filas_objetivo, numero)


class EigthPuzzleProblem(Problema):
    def acciones(self, estado):
        '''Returns a list of the pieces we can move to the empty space.'''
        filas = string_a_lista(estado)
        fila_e, columna_e = encontrar_ubicacion(filas, 'e')

        acciones = []
        if fila_e > 0:
            acciones.append(filas[fila_e - 1][columna_e])
        if fila_e < 2:
            acciones.append(filas[fila_e + 1][columna_e])
        if columna_e > 0:
            acciones.append(filas[fila_e][columna_e - 1])
        if columna_e < 2:
            acciones.append(filas[fila_e][columna_e + 1])

        return acciones

    def resultado(self, estado, accion):
        '''Return the resulting estado after moving a piece to the empty space.
           (the "accion" parameter contains the piece to move)
        '''
        filas = string_a_lista(estado)
        fila_e, columna_e = encontrar_ubicacion(filas, 'e')
        fila_n, columna_n = encontrar_ubicacion(filas, accion)

        filas[fila_e][columna_e], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_e][columna_e]

        return list_a_string(filas)

    def esObjetivo(self, estado):
        '''Returns true if a estado is the objetivo estado.'''
        return estado == OBJETIVO

    #def costoCamino(self, state1, accion, state2):
    #    '''Returns the cost of performing an accion. No useful on this problem, i
    #       but needed.
    #    '''
    #    return 1

    def heuristica(self, estado):
        '''Returns an *estimation* of the distancia from a estado to the objetivo.
           We are using the manhattan distancia.
        '''
        filas = string_a_lista(estado)

        distancia = 0

        for numero in '12345678e':
            fila_n, columna_n = encontrar_ubicacion(filas, numero)
            fila_n_objetivo, columna_n_objetivo = objetivo_posiciones[numero]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - columna_n_objetivo)

        return distancia


#resultado = astar_search(EigthPuzzleProblem(INICIAL, OBJETIVO)).solution()
resultado = busqueda_profundidad_iterativa(EigthPuzzleProblem(INICIAL, OBJETIVO))

# if you want to use the visual debugger, use this instead:
# resultado = astar(EigthPuzzleProblem(INICIAL), viewer=WebViewer())

for accion, estado in resultado.camino():
    print('Move numero', accion)
    print(estado)

