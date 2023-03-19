class MathNeuron:
    def __init__(self, num_inputs):
        self.weights = []
        for i in range(num_inputs):
            self.weights.append(1)  # инициализация веса до 1
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
            output = 0
        return output
