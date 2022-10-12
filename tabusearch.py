"Genera una solucion random"

from random import randint
from instance import Instance


def tabu_search():
    "Aqui inicia el proyecto"
    instance=Instance()
    instance.set_instance()
    initial_solution = random_sol()
    rows=[0]*200
    # print(initial_solution)
    # finness=[800,True]
    objetive_funtion(initial_solution,instance,rows)
    # for i in range(10):
    #     pass
    
def clear_rows(rows):
    
    for i in range(200):
        rows[i]=0

# def objetive_funtion(initial_solution,columns):
#     is_factible(initial_solution,columns)
#     return []
def is_covered(rows):
      
    for i in range(200):
        if rows[i]==0:
            print('falta el elemento ',i+1)
            return False
        
    return True
  
def objetive_funtion(initial_solution,instance,rows):
    finess=0
    clear_rows(rows)
    
    for (index,element) in enumerate(initial_solution): 
        if element:
            update_rows(rows,instance.columns[index])
            finess=finess+instance.columns[index].cost
    is_covered(rows)        
    print(rows,finess)
    
def update_rows(rows,column):
    # print(len(column.active_rows))
    for element in column.active_rows:
        rows[element-1]=rows[element-1]+1
    # print(rows)
    
def random_sol():
    "Genera una solucion random"
    list_solution=[]
    for i in range(1000):
        list_solution.append(randint(0, 1))
    return list_solution

if __name__ == "__main__":
    tabu_search()