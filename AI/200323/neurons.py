class MathNeuron:
    def __init__(self, numInputs):
        self.weight = []
      
        for counter in range(numInputs):
            self.weight.append(1)
        self.bias = 0

    def calculateOutput(self, inputs):
        sum = 0
        for counter in range(len(inputs)):
            sum += inputs[counter] * self.weight[counter]
        sum += self.bias
        output = 1 / (1 + pow(2.71828, -sum))
        return output

    def setWeight(self, weight):
        self.weight = weight

    def setBias(self, bias):
        self.bias = bias

    def getWeight(self):
        return self.weight

    def getBias(self):
        return self.bias

class SElement(MathNeuron):
    def __init__(self, numInputs, threshold):
        super().__init__(numInputs)
        self.threshold = threshold

    def calculateOutput(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weight[i]
        sum += self.bias
        if sum >= self.threshold:
            output = 1
        else:
            output = 0
        return output

class AElement(MathNeuron):
    def __init__(self, numInputs, threshold):
        super().__init__(numInputs)
        self.threshold = threshold

    def calculateOutput(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weight[i]
        sum += self.bias
        if sum >= self.threshold:
            output = 1
        else:
            output = 0
        return output

class RElement(MathNeuron):
    def __init__(self, numInputs):
        super().__init__(numInputs)

    def calculateOutput(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weight[i]
        sum += self.bias
        if sum > 0:
            output = 1
        elif sum < 0:
            output = -1
        else:
            output = 0
        return output
      
class NeuralLayer:
    def __init__(self, neuronType, numNeurons, x=None):
        self.neurons = []
        for i in range(numNeurons):
            if x is not None:
                neuron = neuronType(x)
            else:
                neuron = neuronType()
            self.neurons.append(neuron)

    def calcOutputs(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.calculateOutput(inputs))
        return outputs

    def setWeight(self, weight):
        for neuron, weight in zip(self.neurons, weight):
            neuron.setWeight(weight)

    def setBias(self, biases):
        for neuron, bias in zip(self.neurons, biases):
            neuron.setBias(bias)

    def getNeurons(self):
        return self.neurons

def createDisconnected(layerNum, firstLayer):
    network = []
    currentLayer = firstLayer
    for i in range(layerNum):
        layer = []
        for j in range(currentLayer):
            if j == 0:
                layer.append('S')
            elif j % 2 == 0:
                layer.append('A')
            else:
                layer.append('R')

        network.append(layer)
        currentLayer = (currentLayer // 2) + (currentLayer % 2)
    network.append(['S'])
    return network
