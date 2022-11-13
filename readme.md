# Resolución SCP con Tabú Search

En este trabajo resolveremos una instancia del problema de optimización combinatorial Set Covering Problem (SCP), mediante el uso de la metaheurística Tabú Search. Incorporaremos mecanismos de reparación para poder explotar el rendimiento de esta MH. Al terminar cada resolución, se mostrará un gráfico mostrando el valor de la función objetivo vs el número de iteraciones que transcurrieron.

## Instalación

Primero se requiere sé que se tenga instalado Python en el computador que se desea correr el proyecto.

[Python](https://www.python.org/downloads/)

Una vez teniendo Python instalado debemos ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```
Lo anterior Instalara todos los paquetes necesarios para ejecutar el proyecto

## Uso del proyecto

Para poder ejecutar el proyecto solo es necesario ejecutar el siguiente comando:

```bash
py tabu_search.py
```
Con lo anterior ya se resolverá la instancia [scp41.txt](https://github.com/DannArmandI/TabuSearch/blob/develop/instance/scp41.txt) e imprimirá los resultados por consola, como también mostrara grafico con la información de la ejecución.

### Para modificar la cantidad de iteraciones
En el archivo tabu_search.py en la línea 32 se encontrara con el siguiente Bucle, por lo que solo deberá modificar el numero dentro del **range**
```python
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
```
## Estándares de Calidad

Se utilizaron los Estándares de Calidad del [PEP8](https://peps.python.org/pep-0008/) para los estilos del código , como también se utilizó programación orientada a objetos

## Agradecimientos

Agradecemos tanto a Profesor, como Ayudante del curso Algoritmos Bio Inspirados, por haber aportado con ideas para la resolución del SCP con Tabú Search

## Créditos de Autor 

[Dann Armand](https://github.com/DannArmandI/) & [Cristóbal Cáceres](https://github.com/cristobal2209/)