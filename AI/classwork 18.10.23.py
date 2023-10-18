import sys
import numpy
sys.modules["scipy.random"] = numpy.random
import scipy
import pybrain3

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import supervised

# Создание нейронной сети
# Конфигурация
# Входов: 2
# Выходов: 1
# Скрытых слоёв: 3

the_net = buildNetwork(2, 3, 1)

activation = the_net.activate([2, 1])
print(activation)
print(the_net)

# Создание датасета (входы 2, совпадает с колвом входов в НС
# Колво входов 1 (==//==)
dataset = SupervisedDataSet(2, 1)
