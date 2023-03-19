class MathNeuron:
    def __init__(self, num_inputs):
        self.weights = []
        for i in range(num_inputs):
            self.weights.append(1)
        self.bias = 0

    def calculate_output(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        sum += self.bias
        output = 1 / (1 + pow(2.71828, -sum))
        return output

    def set_weights(self, weights):
        self.weights = weights

    def set_bias(self, bias):
        self.bias = bias

    def get_weights(self):
        return self.weights


    def get_bias(self):
        return self.bias


class SElement(MathNeuron):
    def __init__(self, num_inputs, threshold):
        super().__init__(num_inputs)
        self.threshold = threshold

    def calculate_output(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        sum += self.bias
        if sum >= self.threshold:
            output = 1
        else:
            output = 0
        return output


class AElement(MathNeuron):
    def __init__(self, num_inputs, threshold):
        super().__init__(num_inputs)
        self.threshold = threshold

    def calculate_output(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        sum += self.bias
        if sum >= self.threshold:
            output = 1
        else:
            output = 0
        return output


class RElement(MathNeuron):
    def __init__(self, num_inputs):
        super().__init__(num_inputs)

    def calculate_output(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        sum += self.bias
        if sum > 0:
            output = 1
        elif sum < 0:
            output = -1
        else:
            output = 0  # undefined can be represented as 0 or None
        return output
# TODO 2: Написать универсальный класс для нейронного слоя:
        # Args:
        # Neuron type
        # Neuron number
        # x
# TODO 3: Написать функцию создания несвязной нейронной сети:
        # Функция создаёт нужное количество слоёв нейронов по правилу: количество нейронов в первом слоё задаётся явно,
            # второй слой -- вдвое больше первого, каждый последующий -- вдвое меньше предыдущего (количество нейронов
            # округляем до чётных вверх); слои создаются в нужном количестве, пока в слое не останется один нейрон;
            # типы (S, A, R) в слоях определяются автоматически.
        # Args:
        # Layers number
        # 1st layer neurons number

# TODO Note 0: wₙ = x ± 0.25, θₙ = 1
# TODO Note 1: x - class arg

# Reference: http://bit.ly/3FmnVEo