# Búsqueda con Coste Uniforme - Uniform Cost Search
from Tree import Node


def Compare(node):
    return node.get_cost()


def search_solution_UCS(connections, init_state, solution):
    solved = False
    visited_nodes = []
    frontier_nodes = []
    init_node = Node(init_state)
    init_node.set_cost(0)
    frontier_nodes.append(init_node)
    while (not solved) and len(frontier_nodes) != 0:
        # Ordenar lista de nodos frontera
        frontier_nodes = sorted(frontier_nodes, key=Compare)
        node = frontier_nodes[0]
        # Extraer nodo y añadirlo a visitados
        visited_nodes.append(frontier_nodes.pop(0))
        if node.get_data() == solution:
            # Solucion encontrada
            solved = True
            return node
        else:
            # Expandir nodos hijo (ciudades con conexion)
            node_data = node.get_data()
            child_list = []
            for achild in connections[node_data]:
                child = Node(achild)
                cost = connections[node_data][achild]
                child.set_cost(node.get_cost() + cost)
                child_list.append(child)
                if not child.on_list(visited_nodes):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if child.on_list(frontier_nodes):
                        for n in frontier_nodes:
                            if n.equal(child) and n.get_cost() > child.get_cost():
                                frontier_nodes.remove(n)
                                frontier_nodes.append(child)
                    else:
                        frontier_nodes.append(child)
            node.set_child(child_list)


if __name__ == "__main__":
    connections = {
        'Malaga': {'Granada': 125, 'Madrid': 513},
        'Sevilla': {'Madrid': 514},
        'Granada': {'Malaga': 125, 'Madrid': 423, 'Valencia': 491},
        'Valencia': {'Granada': 491, 'Madrid': 356, 'Zaragoza': 309, 'Barcelona': 346},
        'Madrid': {'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 'Granada': 423, 'Barcelona': 603, 'Santander': 437,
                   'Valencia': 356, 'Zaragoza': 313, 'Santiago': 599},
        'Salamanca': {'Santiago': 390, 'Madrid': 203},
        'Santiago': {'Salamanca': 390, 'Madrid': 599},
        'Santander': {'Madrid': 437, 'Zaragoza': 394},
        'Zaragoza': {'Barcelona': 296, 'Valencia': 309, 'Madrid': 313},
        'Barcelona': {'Zaragoza': 296, 'Madrid': 603, 'Valencia': 396}
    }
    init_state = 'Malaga'
    solution = 'Santiago'
    solution_node = search_solution_UCS(connections, init_state, solution)
    # Mostrar resultado
    result = []
    node = solution_node
    while node.get_fathr() is not None:
        result.append(node.get_data())
        node = node.get_fathr()
    result.append(init_state)
    result.reverse()
    print(result)
    print("Coste: %s" % str(solution_node.get_cost()))
