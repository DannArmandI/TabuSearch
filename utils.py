" asdasdasd"
from random import randint


class Solution:
    "se almacena la mejor solucion"
    rows = [0]*200
    columns = [0]*1000
    finess = 0

    def copy(self, copia):
        "asdasd"
        copia.columns = self.columns.copy()
        copia.rows = self.rows.copy()
        copia.finess = self.finess


def neighbour_analize(instance, best_solution, neighbour, repair_method):
    "asd"
    local_best = Solution()
    best_solution.copy(local_best)
    for i in range(1000):
        best_solution.copy(neighbour)
        if neighbour.columns[i] == 0:
            continue
        else:
            neighbour.columns[i] = 0
        # print(neighbour.columns)
        covered = objetive_funtion(instance, neighbour)
        if not covered:
            if repair_method:
                print('solucion reparada')
                repair_solution(neighbour, repair_method)
            continue
        elif neighbour.finess <= local_best.finess:
            neighbour.copy(local_best)
            # print(local_best.columns)
    # print(local_best.columns)
    if local_best.columns == best_solution.columns:
        print('bucle encontrado')
        return True
    local_best.copy(best_solution)
    # print(best_solution.columns)

# def alterColumns(column):
#     "asd"
#     if column==0:
#         column=1
#     else: column=0


def repair_solution(neighbour, repair_method):
    "jasdjkasd"
    pass


def clear_rows(rows):
    "asd"
    for i in range(200):
        rows[i] = 0

# def objetive_funtion(initial_solution,columns):
#     is_factible(initial_solution,columns)
#     return []


def is_covered(rows):
    "asd "
    for i in range(200):
        if rows[i] == 0:
            # print('falta el elemento ', i+1)
            return False

    return True


def objetive_funtion(instance, solution):
    " asd"
    solution.finess = 0
    clear_rows(solution.rows)

    for (index, element) in enumerate(solution.columns):
        if element:
            update_rows(solution.rows, instance.columns[index])
            solution.finess = solution.finess+instance.columns[index].cost
    return is_covered(solution.rows)
    # print(rows, finess)
    # return finess


def update_rows(rows, column):
    " asd"
    # print(len(column.active_rows))
    for element in column.active_rows:
        rows[element-1] = rows[element-1]+1
    # print(rows)


def random_sol():
    "Genera una solucion random"
    list_solution = []
    for i in range(1000):
        list_solution.append(randint(0, 1))
    return list_solution
