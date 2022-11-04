"Genera una solucion random"

import time
from instance import Instance
from utils import is_covered, neighbour_analize, objetive_funtion, random_sol, Solution


def tabu_search():
    "Aqui inicia el proyecto"
    instance = Instance()
    instance.set_instance()
    best_solution = Solution()
    neighbour = Solution()
    best_solution.columns = random_sol()
    # neighbour.columns=random_sol()
    # rows=[0]*200
    objetive_funtion(instance, best_solution)
    print('Initial Rows: ', best_solution.rows)
    print('Initial Columns: ', best_solution.columns)
    print('Initial Is covered: ', is_covered(best_solution.rows)[0])
    print('Initial Fitness :', best_solution.fitness)
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    flag_repair = False
    for _ in range(500):
        if flag_repair:
            flag_repair = neighbour_analize(
                instance, best_solution, neighbour, 1)
        else:
            flag_repair = neighbour_analize(
                instance, best_solution, neighbour, 0)
        # print(best_solution.rows)
        # print(rows)
    # print(best_solution.rows)
    print('Rows: ', best_solution.rows)
    print('Columns: ', best_solution.columns)
    print('Is covered: ', is_covered(best_solution.rows)[0])
    print('Fitness :', best_solution.fitness)
    #     pass


if __name__ == "__main__":
    begin = time.time()
    tabu_search()
    end = time.time()
    print('Execution Time: ', "{:.0f}".format(end-begin), 'seg')
