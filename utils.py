" asdasdasd"
from random import randint
import numpy as np


class Solution:
    "se almacena la mejor solucion"
    rows = [0]*200
    columns = [0]*1000
    fitness = 0

    def set(self, aux):
        "asdasd"
        self.columns = aux.columns.copy()
        self.rows = aux.rows.copy()
        self.fitness = aux.fitness


def neighbour_analize(instance, best_solution, neighbour, repair_flag):
    "asd"
    local_best = Solution()
    local_best.set(best_solution)
    for i in range(999, -1, -1):
        neighbour.set(best_solution)
        if neighbour.columns[i] == 0:
            continue
        else:
            neighbour.columns[i] = 0
        # print(neighbour.columns)
        covered_flag, missing_rows = objetive_funtion(instance, neighbour)
        if not covered_flag:
            if repair_flag:
                # print('solucion reparada')
                repair_solution(instance, neighbour, missing_rows)
            else:
                continue
        if local_best.fitness >= neighbour.fitness :
            local_best.set(neighbour)
            if repair_flag:
                continue
            break

    if local_best.columns == best_solution.columns:
        return True
    best_solution.set(local_best)


def repair_solution(instance, neighbour, missing_rows):
    "asdasd"
    for (i, column) in enumerate(neighbour.columns):
        if not missing_rows:
            break
        if column:
            continue
        else:
            finded_rows = [
                x for x in instance.columns[i].active_rows if x in missing_rows]
            # print('finded_rows: ', finded_rows)
            # print('missing_rows: ', missing_rows)
            if finded_rows:
                neighbour.columns[i] = 1
                neighbour.fitness += instance.columns[i].cost
                for finded_row in finded_rows:
                    missing_rows.remove(finded_row)
                    neighbour.rows[finded_row]+=1


def clear_rows(rows):
    "asd"
    for i in range(200):
        rows[i] = 0


def is_covered(rows):
    "asd "
    missing_rows = []
    flag = True
    for i in range(200):
        if rows[i] == 0:
            missing_rows.append(i)

    if missing_rows:
        flag = False
    return flag, missing_rows


def objetive_funtion(instance, solution):
    " asd"
    solution.fitness = 0
    clear_rows(solution.rows)

    for (index, element) in enumerate(solution.columns):
        if element:
            update_rows(solution.rows, instance.columns[index])
            solution.fitness = solution.fitness+instance.columns[index].cost
    return is_covered(solution.rows)


def update_rows(rows, column):
    " asd"
    # print(len(column.active_rows))
    for element in column.active_rows:
        rows[element] += 1
    # print(rows)


def random_sol():
    "Genera una solucion random"
    list_solution = []
    for _ in range(1000):
        list_solution.append(randint(0, 1))
    return list_solution
