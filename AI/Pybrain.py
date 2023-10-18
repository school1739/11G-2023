import sys
import numpy
sys.modules["scipy.random"] = numpy.random
import scipy
import pybrain3

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet

# Создание нейронной сети
# Конфигурация:
#     Входов : 2
#     Выходов : 1
#     Скрытых слоев : 3

the_net = buildNetwork(2, 3, 1)

activation = the_net.activate([2, 1])
print(activation)
print(the_net)

# Создание датасета (количество входов 2(должно совпадать с кол-ом входов в НС),
#   количество выходов 1 (==//==))
dataset = SupervisedDataSet(2, 1)

# Заполнение датасета (Функция И)
dataset.addSample([0, 0], [0])
dataset.addSample([0, 1], [0])
dataset.addSample([1, 0], [0])
dataset.addSample([1, 1], [1])

print(dataset)