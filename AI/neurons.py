import random


class MathNeuron:
    def __init__(self, x_count, w, theta):
        self.x_count = x_count
        self.w = w + random.random(-0.25, 0.25)
        self.theta = theta
        self.sum = 0
        print(f"Создан нейрон с количеством входов {self.x_count}, весом {self.w} и порогом {self.theta}")

    def get_info(self):
        print(f"Нейрон с количеством входов {self.x_count}, весом {self.w} и порогом {self.theta}")

    def activate(self, x):
        if len(x) != self.x_count:
            print("Количество входов не соответствует количеству входов нейрона")
        else:
            self.sum = 0
            for i in range(self.x_count):
                self.sum += x[i] * self.w[i]
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

class Net:
    def create_net(self, layers_number, first_layer_neurons_number):
        current_number = 0
        for layer in range(1, layers_number+1):
            if layer == 1:
                for j in range(1, first_layer_neurons_number):
                    Layer("S", 1, 1).create_neurons()
            elif layer == 2:
                for j in range(1, first_layer_neurons_number*2):
                    current_number = first_layer_neurons_number*2
                    Layer("A", 1, 1).create_neurons()
            elif layer == layers_number:
                    Layer("R", 1, 1).create_neurons()
            else:
                for j in range(1, ((current_number//2)+current_number%2)+1):
                    Layer("A", 1, 1).create_neurons()

