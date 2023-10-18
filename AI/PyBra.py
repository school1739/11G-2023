import sys
import numpy
sys.modules["scipy.random"] = numpy.random
import scipy
import pybrain3

from pybrain3.tools.shortcuts import buildNetwork

# Создание нейронной сети
# Конфигурация:
#     Входов: 2
#     Выходов: 1
#     Скрытых слоёв: 3

the_net = buildNetwork(2, 3, 1)

activation = the_net.activate([2,1])
print(activation)
print(the_net)

# Создание датасета(количество входов 2(должно совпадать с количеством входов в НС)
#        количество выходов 1 (=//=))
dataset=SupervisedDataSet(2, 1)


# Заполение датасета
dataset.addSample([0, 0], [0])
dataset.addSample([0, 1], [0])
dataset.addSample([0, 1], [0])
dataset.addSample([0, 1], [0])