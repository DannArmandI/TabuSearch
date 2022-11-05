"Funciones para poder ejecutar Tabu Search"
from random import randint


class Solution:
    "Es una clase para almacenar todo lo necesario en una solucion"
    rows = [0]*200
    columns = [0]*1000
    fitness = 0

    def set(self, aux):
        "Funcion para definir un valor para un objeto de tipo Solution"
        self.columns = aux.columns.copy()
        self.rows = aux.rows.copy()
        self.fitness = aux.fitness

class TabuListElement:
    "Clase que representa un elemento en la lista Tabu"
    

def neighbour_analize(instance, best_solution, neighbour, repair_flag):
    "Analiza los vecinos de una solucion determinada"
    local_best = Solution()
    local_best.set(best_solution)
    for i in range(999, -1, -1):
        neighbour.set(best_solution)
        if neighbour.columns[i] == 0:
            continue
        else:
            neighbour.columns[i] = 0
        covered_flag, missing_rows = objetive_funtion(instance, neighbour)
        if not covered_flag:
            if repair_flag:
                repair_solution_complex(instance, neighbour, missing_rows)
            else:
                continue
        if local_best.fitness >= neighbour.fitness :
            local_best.set(neighbour)
            if repair_flag:
                continue
            break
    if local_best.columns == best_solution.columns:
        print('bucle encontrado')
    best_solution.set(local_best)


def repair_solution(instance, neighbour, missing_rows):
    "Repara las solucion de manera simple"
    for (i, column) in enumerate(neighbour.columns):
        if not missing_rows:
            break
        if column:
            continue
        else:
            finded_rows = [
                x for x in instance.columns[i].active_rows if x in missing_rows]
            if finded_rows:
                neighbour.columns[i] = 1
                neighbour.fitness += instance.columns[i].cost
                for finded_row in finded_rows:
                    missing_rows.remove(finded_row)
                    neighbour.rows[finded_row]+=1


def repair_solution_complex(instance, neighbour, missing_rows):
    "asdasd"
    while missing_rows:
        best_trade_off=10000
        best_column_index=0
        best_finded_rows=[]
        for (i, column) in enumerate(neighbour.columns):
            if not missing_rows:
                break
            if column:
                continue
            else:
                finded_rows = [
                    x for x in instance.columns[i].active_rows if x in missing_rows]
                if finded_rows:
                    trade_off=instance.columns[i].cost/len(finded_rows)
                    if best_trade_off >= trade_off:
                        best_trade_off=trade_off
                        best_column_index = i
                        best_finded_rows=finded_rows
        neighbour.columns[best_column_index] = 1
        neighbour.fitness += instance.columns[best_column_index].cost
        for finded_row in best_finded_rows:
            missing_rows.remove(finded_row)
            neighbour.rows[finded_row]+=1

def clear_rows(rows):
    "Limpia las filas asociadas a una solucion"
    for i in range(200):
        rows[i] = 0

def is_covered(rows):
    "Verifica si todas las restricciones estan cubiertas"
    missing_rows = []
    flag = True
    for i in range(200):
        if rows[i] == 0:
            missing_rows.append(i)

    if missing_rows:
        flag = False
    return flag, missing_rows


def objetive_funtion(instance, solution):
    "Calcula la funcion objetivo y llama a is_covered"
    solution.fitness = 0
    clear_rows(solution.rows)

    for (index, element) in enumerate(solution.columns):
        if element:
            update_rows(solution.rows, instance.columns[index])
            solution.fitness = solution.fitness+instance.columns[index].cost
    return is_covered(solution.rows)


def update_rows(rows, column):
    "Actualiza las filas con en relacion a la columna que se activara"
    for element in column.active_rows:
        rows[element] += 1


def random_sol():
    "Genera una solucion random"
    list_solution = []
    for _ in range(1000):
        list_solution.append(randint(0, 1))
    return list_solution
