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
# TODO 1: Написать три подкласса -- под одному для S, A, R элементов (учитываем особенности! --> ref)
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