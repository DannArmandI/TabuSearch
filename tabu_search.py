"Aqui inicia el proyecto"

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
    objetive_funtion(instance, best_solution)
    print('Initial Rows: ', best_solution.rows)
    print('Initial Columns: ', best_solution.columns)
    print('Initial Is covered: ', is_covered(best_solution.rows)[0])
    print('Initial Fitness :', best_solution.fitness)
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for _ in range(480):
        neighbour_analize(
        instance, best_solution, neighbour, 1)

    print('Rows: ', best_solution.rows)
    print('Columns: ', best_solution.columns)
    print('Is covered: ', is_covered(best_solution.rows)[0])
    print('Fitness :', best_solution.fitness)


if __name__ == "__main__":
    begin = time.time()
    tabu_search()
    end = time.time()
    print('Execution Time: ', "{:.0f}".format(end-begin), 'seg')
