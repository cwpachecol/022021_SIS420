# Puzle lineal con Busqueda en Profundidad - Deep First Search
from Tree import Node

def search_solution_DFS(init_state, solution):
    solved = False
    visited_nodes = []
    frontrs_nodes = []
    init_node = Node(init_state)
    frontrs_nodes.append(init_node)
    while (not solved) and len(frontrs_nodes) != 0:
        node = frontrs_nodes.pop()
        # Extraer nodo y añadirlo a visitados
        visited_nodes.append(node)
        if node.get_data() == solution:
            # Solucion encontrada
            solved = True
            return node
        else:
            # Expandir nodos hijos
            data_node = node.get_data()
            # Operador Izquierdo
            child = [data_node[1], data_node[0], data_node[2], data_node[3]]
            left_child = Node(child)
            if not left_child.on_list(visited_nodes) and not left_child.on_list(frontrs_nodes):
                frontrs_nodes.append(left_child)
            # Operador Central
            child = [data_node[0], data_node[2], data_node[1], data_node[3]]
            central_child = Node(child)
            if not central_child.on_list(visited_nodes) and not central_child.on_list(frontrs_nodes):
                frontrs_nodes.append(central_child)
            # Operador Derecho
            child = [data_node[0], data_node[1], data_node[3], data_node[2]]
            right_child = Node(child)
            if not right_child.on_list(visited_nodes) and not right_child.on_list(frontrs_nodes):
                frontrs_nodes.append(right_child)
            node.set_child([left_child, central_child, right_child])


if __name__ == "__main__":
    init_state = [4, 2, 3, 1]
    solution = [1, 2, 3, 4]
    solution_node = search_solution_DFS(init_state, solution)
    # Mostrar resultado
    result = []
    node = solution_node
    while node.get_fathr() is not None:
        result.append(node.get_data())
        node = node.get_fathr()
    result.append(init_state)
    result.reverse()
    print(result)
