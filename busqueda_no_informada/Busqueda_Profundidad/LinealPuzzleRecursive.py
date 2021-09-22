# Puzle lineal con Busqueda en Profundidad Recursiva
from Tree import Node


def search_solution_DFS_R(init_node, solution, visited):
    visited.append(init_node.get_data())
    if init_node.get_data() == solution:
        return init_node
    else:
        # Expandir nodos sucesores (hijos)
        node_data = init_node.get_data()
        son = [node_data[1], node_data[0], node_data[2], node_data[3]]
        left_son = Node(son)
        son = [node_data[0], node_data[2], node_data[1], node_data[3]]
        central_son = Node(son)
        son = [node_data[0], node_data[1], node_data[3], node_data[2]]
        right_son = Node(son)
        init_node.set_child([left_son, central_son, right_son])

        for node_son in init_node.get_child():
            if not node_son.get_data() in visited:
                # Llamada Recursiva
                Solution = search_solution_DFS_R(node_son, solution, visited)
                if Solution is not None:
                    return Solution
        return None


if __name__ == "__main__":
    init_state = [4, 2, 3, 1]
    solution = [1, 2, 3, 4]
    solution_node = None
    visited = []
    init_node = Node(init_state)
    node = search_solution_DFS_R(init_node, solution, visited)

    # Mostrar Resultado
    result = []
    while node.get_fathr() is not None:
        result.append(node.get_data())
        node = node.get_fathr()
    result.append(init_state)
    result.reverse()
    print(result)
