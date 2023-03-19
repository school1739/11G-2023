    #  0: Написать класс для математического нейрона (считаем, что число выходов может быть >1, дендриты не учитываем)
class MathNeuron:
    def __init__(self, nomerinputs):
        self.weights = []
        for i in range(nomerinputs):
            self.weights.append(1)
        self.bias = 0

    def calcoutputs(self, inputs):
        OBSHsumma = 0
        for i in range(len(inputs)):
            OBSHsumma += inputs[i] * self.weights[i]
        OBSHsumma += self.bias
        output = 1 / (1 + pow(2.71828, -OBSHsumma))
        return output

    def setw(self, weights):
        self.weights = weights

    def setb(self, bias):
        self.bias = bias

    def getw(self):
        return self.weights


    def getb(self):
        return self.bias

#  1: Написать три подкласса -- под одному для S, A, R элементов (учитываем особенности! --> ref)
#  2: Написать универсальный класс для нейронного слоя:
        # Args:
        # Neuron type
        # Neuron number
        # x
#  3: Написать функцию создания несвязной нейронной сети:
        # Функция создаёт нужное количество слоёв нейронов по правилу: количество нейронов в первом слоё задаётся явно,
            # второй слой -- вдвое больше первого, каждый последующий -- вдвое меньше предыдущего (количество нейронов
            # округляем до чётных вверх); слои создаются в нужном количестве, пока в слое не останется один нейрон;
            # типы (S, A, R) в слоях определяются автоматически.
        # Args:
        # Layers number
        # 1st layer neurons number

#  Note 0: wₙ = x ± 0.25, θₙ = 1
#  Note 1: x - class arg

# Reference: http://bit.ly/3FmnVEo




