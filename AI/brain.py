class neuron:
    def __init__(self, inputs, weights, bias):
        self.inputs = inputs
        self.weights = weights
        self.bias = bias

    def get_output(self):
        output = 0
        for i in range(len(self.inputs)):
            output += self.inputs[i] * self.weights[i]
        output += self.bias
        return output


class layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def get_outputs(self):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.get_output())
        return outputs

neuron1 = neuron([1, 2, 3], [0.2, 0.8, -0.5], 2)
neuron2 = neuron([2, 3, 4], [0.5, -0.91, 0.26], -1)
neuron3 = neuron([3, 4, 5], [-0.26, -0.27, 0.17], 0.5)
layer1 = layer([neuron1, neuron2, neuron3])
print(layer1.get_outputs())