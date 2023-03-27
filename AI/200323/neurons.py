import random


class MathNeuron:
    def __init__(self, x_count, w, theta):
        self.x_count = x_count
        self.w = w + 0  # random.randrange(-0.25, 0.25)
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


def createNet(beginWith, amountOfLayers):
    net = []
    net.append(Layer('S', beginWith, 1))
    prevAmount = beginWith
    net.append(Layer('A', beginWith * 2, prevAmount))
    prevAmount = beginWith * 2
    net.append(Layer('A', beginWith, prevAmount))
    tempAmount = beginWith
    net.append(beginWith)
    while tempAmount > 2:
        if tempAmount % 2 == 0:
            prevAmount = tempAmount
            tempAmount = tempAmount / 2
            if tempAmount % 2 != 0:
                tempAmount = tempAmount + 1
            net.append(Layer('A', int(tempAmount), int(prevAmount)))
        else:
            prevAmount = tempAmount
            tempAmount = tempAmount // 2 + 1
            if tempAmount % 2 != 0:
                tempAmount = tempAmount + 1
            net.append(Layer('A', int(tempAmount), int(prevAmount)))

    net.append(Layer('R', 1, 2))

    print(f'СОЗДАНА СЕТЬ НЕЙРОНОВ! ПЕРВЫЙ СЛОЙ РАЗМЕРОМ {beginWith}:')
    print(net)

    return net


createNet(12, 2)
