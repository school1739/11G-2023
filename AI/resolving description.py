import sys
import numpy
sys.modules["scipy.random"] = numpy.random
import scipy as sp
import pybrain3 as pb

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet

#Создание нейронной сети
#Конфигурация:
#   Входов: 2
#   Выходов: 1
#   Cкрытых слоев: 3

the_net = buildNetwork(2,3,1)

activation = the_net.activate([2,1])
print(activation)
print(the_net)

# Создание датасета (количество входов 2(должно совпадать с кол-вом входов НС))
#   количество выходов 1 (==\\==)
dataset=SupervisedDataSet(2,1)

