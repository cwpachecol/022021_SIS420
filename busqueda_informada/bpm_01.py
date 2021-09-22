# Funcion Heuristica - Heuristic Function
from NodosBI import NodoBI


def busqueda_heuristica(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        nodo_datos = nodo_inicial.get_datos()
        hijo = [nodo_datos[1], nodo_datos[0], nodo_datos[2], nodo_datos[3]]
        hijo_izquierda = NodoBI(hijo)
        hijo = [nodo_datos[0], nodo_datos[2], nodo_datos[1], nodo_datos[3]]
        hijo_centro = NodoBI(hijo)
        hijo = [nodo_datos[0], nodo_datos[1], nodo_datos[3], nodo_datos[2]]
        hijo_derecha = NodoBI(hijo)
        nodo_inicial.set_hijo([hijo_izquierda, hijo_centro, hijo_derecha])

        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_datos() in visitados and heuristica(nodo_inicial, nodo_hijo):
                # Llamada recursiva
                solutn = busqueda_heuristica(nodo_hijo, solucion, visitados)
                if solutn is not None:
                    return solutn
        return None


def heuristica(nodo_padre, nodo_hijo):
    padre_calidad = 0
    hijo_calidad = 0
    padre_datos = nodo_padre.get_datos()
    hijo_datos = nodo_hijo.get_datos()

    for n in range(1, len(padre_datos)):
        if padre_datos[n] > padre_datos[n - 1]:
            padre_calidad = padre_calidad + 1
        if hijo_datos[n] > hijo_datos[n - 1]:
            hijo_calidad = hijo_calidad + 1

    if hijo_calidad >= padre_calidad:
        return True
    else:
        return False


if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    estado_solucion = [1, 2, 3, 4]
    nodos_visitados = []
    nodo_inicial = NodoBI(estado_inicial)
    nodo_solucion = busqueda_heuristica(nodo_inicial, estado_solucion, nodos_visitados)
    print(nodo_solucion.obtenerSolucion())
    #for nodo_actual in nodo_solucion.obtenerCamino():
    #    print(nodo_actual.datos)
    