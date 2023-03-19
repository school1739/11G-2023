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
class ElemS(MathNeuron):
    def __init__(self, nomer__inputs, threshold):
        super().__init__(nomer__inputs)
        self.threshold = threshold

    def calcoutput(self, inputs):
        OBSHsumma = 0
        for i in range(len(inputs)):
            OBSHsumma += inputs[i] * self.weights[i]
        OBSHsumma += self.bias
        if OBSHsumma >= self.threshold:
            output = 1
        else:
            output = 0
        return output


class ElemA(MathNeuron):
    def __init__(self, num_inputs, threshold):
        super().__init__(num_inputs)
        self.threshold = threshold

    def calculate_output(self, inputs):
        OBSHsumma = 0
        for i in range(len(inputs)):
            OBSHsumma += inputs[i] * self.weights[i]
        OBSHsumma += self.bias
        if OBSHsumma >= self.threshold:
            output = 1
        else:
            output = 0
        return output


class ElemR(MathNeuron):
    def __init__(self, nomer__inputs):
        super().__init__(nomer__inputs)

    def calcoutput(self, __inputs):
        OBSHsumma = 0
        for i in range(len(__inputs)):
            OBSHsumma += __inputs[i] * self.weights[i]
        OBSHsumma += self.bias
        if OBSHsumma > 0:
            output = 1
        elif OBSHsumma < 0:
            output = -1
        else:
            output = 0  # undefined can be represented as 0 or None
        return output
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
        class Neironal:
            def __init__(self, tips_neiron, nomer_neuronov, x = None):
                self.neirons = []
                for i in range(nomer_neuronov):
                    if x is not None:
                        neiron1 = tips_neiron(x)
                    else:
                        neiron1 = tips_neiron()
                    self.neurons.append(neiron1)

            def compoutputs(self, inputs):
                outputs = []
                for neiron1 in self.neurons:
                    outputs.append(neiron1.calcoutput(inputs))
                return outputs

            def setw(self, weights):
                for neuron, weight in zip(self.neirons, weights):
                    neuron.setw(weight)

            def setb(self, biases):
                for neiron1, bias in zip(self.neurons, biases):
                    neiron1.setb(bias)

            def getter_neirons(self):
                return self.neirons

    #  Note 0: wₙ = x ± 0.25, θₙ = 1
#  Note 1: x - class arg

# Reference: http://bit.ly/3FmnVEo




