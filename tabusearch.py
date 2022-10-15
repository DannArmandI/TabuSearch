"Genera una solucion random"

from instance import Instance
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
    print(best_solution.rows)
    # finness=[800,True]
    for i in range(400):
        neighbour_analize(instance, best_solution, neighbour,'')
        # print(best_solution.rows)
        # print(rows)
    # print(best_solution.rows)
    print(best_solution.columns)
    print(is_covered(best_solution.rows))
    print(best_solution.finess)
    #     pass


if __name__ == "__main__":
    tabu_search()
