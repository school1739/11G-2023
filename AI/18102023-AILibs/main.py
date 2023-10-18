import sys
import numpy as np
sys.modules["scipy.random"] = numpy.random
import pybrain3 as pb
import scipy as sp


from pybrain3.tools.shortcuts import buildNetwork

# Создание нейронной сети
# Конфигурация:
#       Входов: 2
#       Выходов: 1
#       Скрытых слоёв: 3

theNet = buildNetwork(2,3,1)

activation = theNet.activate([2,1])

print(activation)
print(theNet)

dataset.addSample([0, 0], [0])
dataset.addSample([0, 1], [0])
dataset.addSample([1, 0], [0])
dataset.addSample([1, 1], [1])
