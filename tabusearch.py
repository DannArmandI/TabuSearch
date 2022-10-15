"Genera una solucion random"

from instance import Instance
import time
from utils import *


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
    print('Initial Is covered: ', is_covered(best_solution.rows))
    print('Initial Finess :', best_solution.finess)
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    flag = False
    for i in range(400):
        if flag:
            flag = neighbour_analize(instance, best_solution, neighbour, '')
            # neighbour_analize(instance, best_solution,
            #                   neighbour, 'simple_repair')
        else:
            flag = neighbour_analize(instance, best_solution, neighbour, '')
        # print(best_solution.rows)
        # print(rows)
    # print(best_solution.rows)
    print('Rows: ', best_solution.rows)
    print('Columns: ', best_solution.columns)
    print('Is covered: ', is_covered(best_solution.rows))
    print('Finess :', best_solution.finess)
    #     pass


if __name__ == "__main__":
    begin = time.time()
    tabu_search()
    end = time.time()
    print('Execution Time: ', "{:.0f}".format(end-begin), 'seg')
