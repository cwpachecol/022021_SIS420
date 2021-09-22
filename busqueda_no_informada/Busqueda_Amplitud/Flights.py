# Busqueda en Amplitud - Breadth First Search
from Tree import Node


def search_BSF_solution(connections, init_state, solution):
    solved = False
    visited_nodes = []
    frontrs_nodes = []

    init_node = Node(init_state)
    frontrs_nodes.append(init_node)
    while (not solved) and len(frontrs_nodes) != 0:
        node = frontrs_nodes[0]
        # extraer nodo y añadirlo a visitados
        visited_nodes.append(frontrs_nodes.pop(0))
        if node.get_data() == solution:
            solved = True
            return node
        else:
            # expandir nodos hijo - ciudades con conexion
            node_data = node.get_data()
            child_list = []
            for chld in connections[node_data]:
                child = Node(chld)
                child_list.append(child)
                if not child.on_list(visited_nodes) and not child.on_list(frontrs_nodes):
                    frontrs_nodes.append(child)

            node.set_child(child_list)


if __name__ == "__main__":
    connections = {
        'Malaga': {'Salamanca', 'Madrid', 'Barcelona'},
        'Sevilla': {'Santiago', 'Madrid'},
        'Granada': {'Valencia'},
        'Valencia': {'Barcelona'},
        'Madrid': {'Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander'},
        'Salamanca': {'Malaga', 'Madrid'},
        'Santiago': {'Sevilla', 'Santander', 'Barcelona'},
        'Santander': {'Santiago', 'Madrid'},
        'Zaragoza': {'Barcelona'},
        'Barcelona': {'Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia'}
    }

    init_state = 'Malaga'
    solution = 'Santiago'
    solution_node = search_BSF_solution(connections, init_state, solution)
    # mostrar resultado
    result = []
    node = solution_node
    while node.get_fathr() is not None:
        result.append(node.get_data())
        node = node.get_fathr()
    result.append(init_state)
    result.reverse()
    print(result)
