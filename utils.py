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
    column_index=int()
    count=5
    
    def decrease_count(self):
        "as"
        self.count -= 1
        
class TabuList:
    
    tabu_list=[TabuListElement()]
    
    def __init__(self) -> None:
        self.tabu_list.clear()
    
    def add(self, element):
        tabu_element = TabuListElement()
        tabu_element.column_index=element
        self.tabu_list.append(tabu_element)
        
    def search_element(self, element):
        for tabu_element in self.tabu_list:
            if tabu_element.column_index==element:
                return True
        return False    
    
    def decrease_count_list(self):
        copy = self.tabu_list.copy()
        for tabu_element in copy:
            tabu_element.decrease_count()
            if not tabu_element.count:
                self.tabu_list.remove(tabu_element)
                            
    def print_list(self):
        for tabu_element in self.tabu_list:
            print(tabu_element.column_index,' ',tabu_element.count)

def neighbour_analize(instance, best_solution, neighbour, repair_flag ,tabu_list):
    "Analiza los vecinos de una solucion determinada"
    local_best = Solution()
    local_best.set(best_solution)
    for i in range(999, -1, -1):
        neighbour.set(best_solution)
        if neighbour.columns[i] == 0:
            continue
        else:
            neighbour.columns[i] = 0
            tabu_list.add(i)
        covered_flag, missing_rows = objetive_funtion(instance, neighbour)
        if not covered_flag:
            if repair_flag:
                repair_solution(instance, neighbour, missing_rows,tabu_list)
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
    tabu_list.decrease_count_list()


def repair_solution(instance, neighbour, missing_rows,tabu_list):
    "Repara las solucion de manera simple"
    for (i, column) in enumerate(neighbour.columns):
        if not missing_rows:
            break
        if column or tabu_list.search_element(i) :
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
