import sys
import numpy
sys.modules["scipy.random"]=numpy.random
import scipy
import pybrain3

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
#Создание нейронной сети
#Конфигурация:
#   входов: 2
#   выходов: 1
#   скрытых слоёв: 3

the_net=buildNetwork(2,3,1)

activation=the_net.activate([2,1])
print(activation)
print(the_net)
# Создание датасетов (кол во входов 2(должно совпадать с кол вом входов в НС),
#   кол во выходов 1 (=||=))
dataset=SupervisedDataSet(2,1)
# Заполнение датасета
dataset.addSample([0,0], [0])
dataset.addSample([0,1], [0])
dataset.addSample([1,0], [0])
dataset.addSample([1,1], [1])

print(dataset)

