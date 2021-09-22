# Author: GuillermoToledano
# Date: 07/01/2019


def backtracking(variables, variables_ranges, optimal, depth):
    min = variables_ranges[depth][0]
    max = variables_ranges[depth][1]
    for v in range(min, max):
        variables[depth] = v
        if depth < len(variables) - 1:
            # Es candidato si no incumple ninguna restriccion
            if is_candidate(variables):
                optimal = backtracking(variables[:], variables_ranges, optimal, depth + 1)
            else:
                # Estamos en una hoja. Comprobamos solucion
                solution = eval_solution(variables)
                if solution > eval_solution(optimal) and is_candidate(variables):
                    optimal = (variables[0], variables[1])
    return optimal


def eval_solution(vars):
    x1 = vars[0]
    x2 = vars[1]
    val = (12 - 6) * x1 + (8 - 4) * x2
    return val


def is_candidate(vars):
    x1 = vars[0]
    x2 = vars[1]
    value1 = 7 * x1 + 4 * x2
    value2 = 6 * x1 + 5 * x2
    if value1 <= 150 and value2 <= 160:
        return True
    else:
        return False


if __name__ == "__main__":
    # Valor de variables X1 y X2
    variables_val = [0, 0]
    # Rango de las variables X1 y X2
    variables_ran = [(0, 51), (0, 76)]
    # Mejor solucion encontrada
    optimal_val = (0, 0)
    solution = backtracking(variables_val[:], variables_ran, optimal_val, 0)
    print("Best solution: %d Jeans, %d Shirts, Benefit: %d" % (solution[0], solution[1], eval_solution(solution)))
