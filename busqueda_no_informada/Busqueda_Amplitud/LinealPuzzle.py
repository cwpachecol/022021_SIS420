# Busqueda en Amplitud - Breadth First Search
from TreeBNI import Node


def search_BFS_solution(init_state, solution):
    solved = False
    visited_nodes = []
    frontrs_nodes = []

    initNode = Node(init_state)
    frontrs_nodes.append(initNode)
    while (not solved) and len(frontrs_nodes) != 0:
        node = frontrs_nodes.pop(0)
        # extraer nodo y añadirlo a visitados
        visited_nodes.append(node)
        if node.get_data() == solution:
            # solucion encontrada
            solved = True
            return node
        else:
            # expandir nodos hijo
            node_data = node.get_data()

            # operador izquierdo
            child = [node_data[1], node_data[0], node_data[2], node_data[3]]
            left_child = Node(child)
            if not left_child.on_list(visited_nodes) and not left_child.on_list(frontrs_nodes):
                frontrs_nodes.append(left_child)

            # operador central
            child = [node_data[0], node_data[2], node_data[1], node_data[3]]
            center_child = Node(child)
            if not center_child.on_list(visited_nodes) and not center_child.on_list(frontrs_nodes):
                frontrs_nodes.append(center_child)

            # operador derecho
            child = [node_data[0], node_data[1], node_data[3], node_data[2]]
            right_child = Node(child)
            if not right_child.on_list(visited_nodes) and not right_child.on_list(frontrs_nodes):
                frontrs_nodes.append(right_child)

            node.set_child([left_child, center_child, right_child])


if __name__ == "__main__":
    init_state = [4, 3, 2, 1]
    solution = [1, 2, 3, 4]
    solution_node = search_BFS_solution(init_state, solution)
    # mostrar resultado
    result = []
    node = solution_node
    while node.get_fathr() is not None:
        result.append(node.get_data())
        node = node.get_fathr()

    result.append(init_state)
    result.reverse()
    print(result)
