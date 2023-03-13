import math


class Neuron(dendrite_count, theta, weights):
    def __init__(self, dendrite_count, theta, weights):
        self.dendrite_count = dendrite_count
        self.theta = theta
        self.weights = weights

    def activation(self, inputs):
        weighted_sum = 0
        for i in range(0, self.dendrite_count):
            weighted_sum += inputs[i] * self.weights[i]
        return 1 / (1 + math.exp(-weighted_sum - self.theta))


class Layer(neuron_count, neurons):
    def __init__(self, neuron_count, neurons):
        self.neuron_count = neuron_count
        self.neurons = neurons

    def activation(self, inputs):
        outputs = []
        for i in range(0, self.neuron_count):
            outputs.append(self.neurons[i].activation(inputs))
        return outputs


class Brain(layer_count, layers):
    def __init__(self, layer_count, layers):
        self.layer_count = layer_count
        self.layers = layers

    def activation(self, inputs):
        outputs = []
        for i in range(0, self.layer_count):
            outputs.append(self.layers[i].activation(inputs))
        return outputs
