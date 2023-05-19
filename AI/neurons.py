import random


class MathNeuron:
    # init a neuron with x_count inputs, that every input has its own weight (w +- 0.25) and threshold (theta)
    def __init__(self, x_count, w, theta):
        self.x_count = x_count
        self.w = []
        self.theta = theta
        self.sum = 0
        for i in range(x_count):
            self.w.append(w+random.uniform(-0.25, 0.25))
        # print all inputs and their weights like "Input 1 = 0.25"
        for i in range(x_count):
            print(f"Вход {i}: {self.w[i]}")

    def get_info(self):
        print(f"Нейрон с количеством входов {self.x_count}, весом {self.w} и порогом {self.theta}")

import random

def activate(self, x):
    if len(x) != self.x_count:
        print("Количество входов не соответствует количеству входов нейрона")
    else:
        self.sum = 0
        for i in range(self.x_count):
            self.w[i] = random.uniform(-0.25, 0.25)
            self.sum += x[i] * self.w[i]
            # print all inputs and their weights
            print(f"Вход {i}: {x[i]} * {self.w[i]} = {x[i] * self.w[i]}")
        if self.sum > self.theta:
            print("Нейрон активирован")
            return True
        else:
            print("Нейрон не активирован")
            return False


class SNeuron(MathNeuron):
    def __init__(self):
        super().__init__(1, 1, 1)
        print("Создан нейрон S")

    def activate(self, x):
        if x > self.theta:
            print("Нейрон S активирован")
            return True
        else:
            print("Нейрон S не активирован")
            return False


class ANeuron(MathNeuron):
    def __init__(self, x_count, w, theta):
        super().__init__(x_count, w, theta)
        print("Создан нейрон A")

    def activate(self, x):
        if self.x_count == 0:
            print("Нет входов")
            return None
        else:
            if super().activate(x):
                return True
            else:
                return False


class RNeuron(MathNeuron):
    def __init__(self, x_count, w, theta):
        super().__init__(x_count, w, theta)
        print("Создан нейрон R")

    def activate(self):
        if self.sum > self.theta:
            print("Нейрон R активирован")
            return 1
        elif self.sum == self.theta:
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
                self.neurons.append(SNeuron())
        elif self.type == "A":
            for i in range(self.number):
                self.neurons.append(ANeuron(self.x, 1, 1))
        elif self.type == "R":
            for i in range(self.number):
                self.neurons.append(RNeuron(self.x, 1, 1))
        else:
            print("Неверный тип нейрона")
            return None

# global function to create network (1st layer - S, 2nd - A, 3rd - R)
# where 1st layer has N neuron, 2nd - 2*N,
# and there so much layers so every subsequent layer has N/2 neurons less than previous
# the last layer has only 1 R neuron
def create_network(N):
    layers = []
    layers.append(Layer("S", N, 0))
    layers.append(Layer("A", 2*N, N))
    while N > 1:
        N = int(N/2)
        layers.append(Layer("R", N, 2*N))
    return layers

layers = create_network(64)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import networkx as nx
import matplotlib.pyplot as plt

# make a pandas dataframe with all neurons and their weights separated by groups based on type of neuron
import pandas as pd
df = pd.DataFrame(columns=["Neuron", "Weight", "Type"])
for i in range(len(layers)):
    for j in range(len(layers[i].neurons)):
        for k in range(len(layers[i].neurons[j].w)):
            df = df.append({"Neuron": f"{i}_{j}", "Weight": layers[i].neurons[j].w[k], "Type": layers[i].type}, ignore_index=True)
print(df)


# plot a graph of network with networkx where color of node based on type of neuron (S - green, A - blue, R - red)
G = nx.Graph()
for i in range(len(layers)):
    for j in range(len(layers[i].neurons)):
        G.add_node(f"{i}_{j}")
for i in range(len(layers)):
    for j in range(len(layers[i].neurons)):
        if i != len(layers) - 1:
            for k in range(len(layers[i+1].neurons)):
                G.add_edge(f"{i}_{j}", f"{i+1}_{k}")
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
nx.draw(G, with_labels=True, node_size=100, alpha=0.5, node_color=colors, font_size=8, font_color="white")
plt.show()