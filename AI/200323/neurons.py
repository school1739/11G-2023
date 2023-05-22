import random


class MathNeuron:
    # init a neuron with x_count inputs, that every input has its own weight (w +- 0.25) and threshold (theta)
    def __init__(self, count_X, w, Theta):
        self.count_X = count_X
        self.w = []
        self.Theta = Theta
        self.sum = 0
        for i in range(count_X):
            self.w.append(w+random.uniform(-0.25, 0.25))

        for i in range(count_X):
            print(f"Вход {i}: {self.w[i]}")
            the_file.write("Вход {i}: {self.w[i]}")

    def get_info(self):
        print(f"Нейрон с количеством входов {self.count_X}, порогом {self.Theta}  и весом {self.w} ")

import random

def activate(self, x):
    if len(x) != self.count_X:
        print("Кол-во входов не соответствует количеству входов нейрона")
    else:
        self.sum = 0
        for i in range(self.count_X):
            self.w[i] = random.uniform(-0.25, 0.25)
            self.sum += x[i] * self.w[i]
            # print all inputs and their weights
            print(f"Вход {i}: {x[i]} * {self.w[i]} = {x[i] * self.w[i]}")
        if self.sum > self.Theta:
            print("Нейрон активирован")
            return True
        else:
            print("Нейрон не активирован")
            return False


class Neuron_S(MathNeuron):
    def __init__(self):
        super().__init__(1, 1, 1)
        print("Создан нейрон S")

    def activate(self, x):
        if x > self.Theta:
            print("Нейрон S активирован")
            return True
        else:
            print("Нейрон S не активирован")
            return False


class ANeuron(MathNeuron):
    def __init__(self, count_X, w, Theta):
        super().__init__(count_X, w, Theta)
        print("Создан нейрон A")

    def activate(self, x):
        if self.count_X == 0:
            print("Нет входов")
            return None
        else:
            if super().activate(x):
                return True
            else:
                return False


class Neuron_R(MathNeuron):
    def __init__(self, count_X, w, Theta):
        super().__init__(count_X, w, Theta)
        print("Создан нейрон R")

    def activate(self):
        if self.sum > self.Theta:
            print("Нейрон R активирован")
            return 1
        elif self.sum == self.Theta:
            print("Нейрон R не определён")
            return None
        else:
            print("Нейрон R не активирован")
            return -1


class Layer:
    def __init__(self, type, number, x):
        self.type = type
        self.number = number
        self.x = x
        self.neurons = []
        self.create_neurons()

    def create_neurons(self):
        if self.type == "S":
            for i in range(self.number):
                self.neurons.append(Neuron_S())
        elif self.type == "A":
            for i in range(self.number):
                self.neurons.append(ANeuron(self.x, 1, 1))
        elif self.type == "R":
            for i in range(self.number):
                self.neurons.append(Neuron_R(self.x, 1, 1))

        else:
            print("Неверный тип нейрона")
            return None

the_file = open("./AI_log.log", 'a', encoding='UTF-8')


def network_create(N):
    layers = []
    layers.append(Layer("S", N, 0))
    layers.append(Layer("A", 2*N, N))
    while N > 1:
        N = int(N/2)
        layers.append(Layer("R", N, 2*N))
    return layers

layers = network_create(64)
# попытка  создания network, но что-то не то вышло
'''
def create_network(kol_vo_neir1s, kol_vo_trebsl):#kol_vo_neir1s - количество нейронов в первом слое, задаваемое явно  #kol_vo_trebsl - количество требуемых слоев в сети
    network = []# будет хранить все слои
    second_sloi_neiron = kol_vo_neir1s * 2
    network.append([None] * kol_vo_neir1s)  # добавляем в конец списка нужное кол-во элементов
    network.append(second_sloi_neiron * [None])
    if second_sloi_neiron  % 2 == 0:# вроде как округление до четных вверъх
        second_sloi_neiron = second_sloi_neiron
    else:
        second_sloi_neiron = second_sloi_neiron + 1
    for i in range(1, kol_vo_trebsl):
        cur_neurons = max(1, second_sloi_neiron //2 )# max для того чтобы если кто-то додумается ввести отрицательное количество слоев, то выводилось бы 1
        network.append([None] * cur_neurons)
        second_sloi_neiron = cur_neurons # обновляем кол-во нейронов для следущего слоя
    return network # и возвращаем весь список слоев сети

#network = create_network(7, -4) # пример выполнения c отрицательным количеством слоев(проверка на дурака)
network = create_network(5, 3)# обычный пример для слоев
print(network)'''


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import networkx as nx
import matplotlib.pyplot as plt


import pandas as pd
df = pd.DataFrame(columns=["Neuron", "Weight", "Type"])#датафрейм
for i in range(len(layers)): # итерация  по слоям
    for j in range(len(layers[i].neurons)):  # итерация  по нейронам
        for k in range(len(layers[i].neurons[j].w)):  # итерация по весам
# добавление новой строки в датафрейм
            df = df._append({"Neuron": f"{i}_{j}", "Weight": layers[i].neurons[j].w[k], "Type": layers[i].type}, ignore_index=True)

print(df)


G = nx.Graph() # новый граф
for i in range(len(layers)): # итерация по слоям
    for j in range(len(layers[i].neurons)): # итерация по нейронам в слоях
        G.add_node(f"{i}_{j}")
for i in range(len(layers)): # итерация по слоям
    for j in range(len(layers[i].neurons)): # итерация по нейронам в 1-ом слое
        if i != len(layers) - 1:
            for k in range(len(layers[i+1].neurons)): # итерация по нейронам в последующем слое
                G.add_edge(f"{i}_{j}", f"{i+1}_{k}")

#характеристика графика
plt.figure(figsize=(10, 10), dpi=300, facecolor='w', edgecolor='k')
colors = []
for i in range(len(layers)):
    for j in range(len(layers[i].neurons)):
        if layers[i].type == "S":
            colors.append("green")
        elif layers[i].type == "A":
            colors.append("blue")
        elif layers[i].type == "R":
            colors.append("red")


nx.draw(G, with_labels=True, node_size=100, alpha=0.5, node_color=colors, font_size=8, font_color="orange")
plt.show()




#














