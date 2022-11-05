from utils import TabuList, TabuListElement
import matplotlib.pyplot as plt

y = [26000, 26000, 26000, 26000, 26000,
     26000, 26000, 26000, 26000, 26000, 26000]
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# tabu_list=TabuList()
# tabu_list.add(20)
# tabu_list.decrease_count_list()
# tabu_list.add(10)
# tabu_list.print_list()
# tabu_list.decrease_count_list()
# tabu_list.decrease_count_list()
# tabu_list.decrease_count_list()
# tabu_list.decrease_count_list()
# print('------------------------')
# tabu_list.print_list()
