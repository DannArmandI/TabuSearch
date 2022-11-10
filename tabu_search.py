"Aqui inicia el proyecto"

import time
from instance import Instance
from utils import is_covered, neighbour_analize, objetive_funtion, random_sol, Solution , TabuList , generate_chart
import matplotlib.pyplot as plt
import numpy as np


def tabu_search():
    "Aqui inicia el proyecto"
    begin = time.time()
    instance = Instance()
    y=[]
    x=[]
    y2=[]
    x2=[]
    instance.set_instance()
    best_solution = Solution()
    neighbour = Solution()
    tabu_list = TabuList()
    best_solution.columns = random_sol()
    objetive_funtion(instance, best_solution)
    print('Initial Rows: ', best_solution.rows)
    print('Initial Columns: ', best_solution.columns)
    print('Initial Is covered: ', is_covered(best_solution.rows)[0])
    print('Initial Fitness :', best_solution.fitness)
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    flag_repair = False
    flag_chart = 0
    for i in range(550):
        if flag_repair:
            flag_repair = neighbour_analize(
                instance, best_solution, neighbour, 1,tabu_list)
            flag_chart = 1
        else:
            flag_repair = neighbour_analize(
                instance, best_solution, neighbour, 0,tabu_list)
        if(flag_chart):
            y2.append(best_solution.fitness)
            x2.append(i)
        else:                
            y.append(best_solution.fitness)
            x.append(i)
    print('Rows: ', best_solution.rows)
    print('Columns: ', best_solution.columns)
    print('Is covered: ', is_covered(best_solution.rows)[0])
    print('Fitness :', best_solution.fitness)
    end = time.time()
    print('Execution Time: ', "{:.0f}".format(end-begin), 'seg')
    generate_chart(x,y,x2,y2)

if __name__ == "__main__":
    tabu_search()
