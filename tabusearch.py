"Genera una solucion random"

from instance import Instance


def tabu_search():
    "Aqui inicia el proyecto"
    instance=Instance()
    instance.set_instance()
    initial_solution = random_sol(instance)

    for i in range(10):
        pass


def random_sol(instance):
    "Genera una solucion random"
    return [1,2]
