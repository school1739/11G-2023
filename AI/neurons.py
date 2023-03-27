import random

class MathNeuron:
    def __init__(self, wCount, x, theta):
        self.weightsCount = wCount
        self.weights = [x + random.triangular(-0.25, 0.25) for _ in range(wCount)]
        self.theta = theta
        self.sum = 0
        
    def Activate(self, x):
        if len(x) != len(self.weights):
            print("Количество входов не соответствует количеству входов нейрона")
        else:
            self.sum = 0
            for i in range(self.weightsCount):
                self.sum += x[i] * self.weights[i]
            if self.sum > self.theta:
                return True
            else:
                return False

class SNeuron(MathNeuron):
    def __init__(self):
        super().__init__(1, 1, 1)

    def Activate(self, x):
        if x >= self.theta:
            return True
        else:
            return False

class ANeuron(MathNeuron):
    def __init__(self, wCount, x, theta):
        super().__init__(wCount, x, theta)

    def Activate(self, x):
        if self.weightsCount == 0:
            return None
        else:
            return super().activate(x)

class RNeuron(MathNeuron):
    def __init__(self, wCount, x, theta):
        super().__init__(wCount, x, theta)
        
    def Activate(self, x):
        if len(x) != len(self.weights):
            print("Количество входов не соответствует количеству входов нейрона")
        else:
            self.sum = 0
            for i in range(self.weightsCount):
                self.sum += x[i] * self.weights[i]
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
    def __init__(self, typ, amount, x):
        self.type = typ
        self.amount = amount
        self.x = x
        self.neurons = []
        self.CreateNeurons()

    def CreateNeurons(self):
        if self.type == "S":
            for i in range(self.amount):
                self.neurons.append(SNeuron())
        elif self.type == "A":
            for i in range(self.amount):
                self.neurons.append(ANeuron(self.x, 1, 1))
        elif self.type == "R":
            for i in range(self.amount):
                self.neurons.append(RNeuron(self.x, 1, 1))
        else:
            print("Неверный тип нейрона")
            return None

def CreateNet(amount):
    layers = []
    layers.append(Layer("S", amount, 0.5))
    current = amount * 2
    while current > 1:
        if current % 2 != 0:
            current += 1
        layers.append(Layer("A", current, 1))
        current /= 2
    layers.append(Layer("R", 1, 1))
    return layers
        
