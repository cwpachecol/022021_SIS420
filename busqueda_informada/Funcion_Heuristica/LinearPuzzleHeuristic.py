# Funcion Heuristica - Heuristic Function
from NodosBI import NodoBI


def search_heuristic_solution(init_node, solution, visited):
    visited.append(init_node.get_data())
    if init_node.get_data() == solution:
        return init_node
    else:
        # Expandir nodos sucesores (hijos)
        node_data = init_node.get_data()
        son = [node_data[1], node_data[0], node_data[2], node_data[3]]
        son_left = Node(son)
        son = [node_data[0], node_data[2], node_data[1], node_data[3]]
        son_central = Node(son)
        son = [node_data[0], node_data[1], node_data[3], node_data[2]]
        son_right = Node(son)
        init_node.set_son([son_left, son_central, son_right])

        for son_node in init_node.get_son():
            if not son_node.get_data() in visited and improvement(init_node, son_node):
                # Llamada recursiva
                solutn = search_heuristic_solution(son_node, solution, visited)
                if solutn is not None:
                    return solutn
        return None


def improvement(father_node, son_node):
    father_quality = 0
    son_quality = 0
    father_data = father_node.get_data()
    son_data = son_node.get_data()

    for n in range(1, len(father_data)):
        if father_data[n] > father_data[n - 1]:
            father_quality = father_quality + 1
        if son_data[n] > son_data[n - 1]:
            son_quality = son_quality + 1

    if son_quality >= father_quality:
        return True
    else:
        return False


if __name__ == "__main__":
    initial_state = [4, 3, 2, 1]
    solution_state = [1, 2, 3, 4]
    visited_nodes = []
    initial_node = Node(initial_state)
    solution_node = search_heuristic_solution(initial_node, solution_state, visited_nodes)

    result = []
    node = solution_node
    while node.get_father() is not None:
        result.append(node.get_data())
        node = node.get_father()
    result.append(initial_state)
    result.reverse()
    print(result)
