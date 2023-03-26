import random


class MathNeuron:
    def __init__(self, x_count, w, theta):
        self.x_count = x_count
        self.w = w + random.random(-0.25, 0.25)
        self.theta = theta
        self.sum = 0
        print(f"Создан нейрон с количеством входов {self.x_count}, весом {self.w} и порогом {self.theta}")

    def get_info(self):
        print(f"Нейрон с количеством входов {self.x_count}, весом {self.w} и порогом {self.theta}")

    def activate(self, x):
        if len(x) != self.x_count:
            print("Количество входов не соответствует количеству входов нейрона")
        else:
            self.sum = 0
            for i in range(self.x_count):
                self.sum += x[i] * self.w[i]
            if self.sum > self.theta:
                print("Нейрон активирован")
                return True
            else:
                print("Нейрон не активирован")
                return False


class SNeuron(MathNeuron):
    def __init__(self):
        super().__init__(1, 1, 1)
        print("Создан нейрон S")

    def activate(self, x):
        if x > self.theta:
            print("Нейрон S активирован")
            return True
        else:
            print("Нейрон S не активирован")
            return False


class ANeuron(MathNeuron):
    def __init__(self, x_count, w, theta):
        super().__init__(x_count, w, theta)
        print("Создан нейрон A")

    def activate(self, x):
        if self.x_count == 0:
            print("Нет входов")
            return None
        else:
            if super().activate(x):
                return True
            else:
                return False


class RNeuron(MathNeuron):
    def __init__(self, x_count, w, theta):
        super().__init__(x_count, w, theta)
        print("Создан нейрон R")

    def activate(self):
        if self.sum > self.theta:
            print("Нейрон R активирован")
            return 1
        elif self.sum == self.theta:
            print("Нейрон R не определён")
            return None
        else:
            print("Нейрон R не активирован")
            return -1


class Layer:
    def __init__(self, type, number, x):
        self.type = type
        self.number = number
        self.x = x
        self.neurons = []
        self.create_neurons()

    def create_neurons(self):
        if self.type == "S":
            for i in range(self.number):
                self.neurons.append(SNeuron())
        elif self.type == "A":
            for i in range(self.number):
                self.neurons.append(ANeuron(self.x, 1, 1))
        elif self.type == "R":
            for i in range(self.number):
                self.neurons.append(RNeuron(self.x, 1, 1))
        else:
            print("Неверный тип нейрона")
            return None



#  3: Написать функцию создания несвязной нейронной сети:
        # Функция создаёт нужное количество слоёв нейронов по правилу: количество нейронов в первом слоё задаётся явно,
            # второй слой -- вдвое больше первого, каждый последующий -- вдвое меньше предыдущего (количество нейронов
            # округляем до чётных вверх); слои создаются в нужном количестве, пока в слое не останется один нейрон;
            # типы (S, A, R) в слоях определяются автоматически.
        # Args:
        # Layers number
        # 1st layer neurons number





def create_network(kol_vo_neir1s, kol_vo_trebsl):#kol_vo_neir1s - количество нейронов в первом слое, задаваемое явно  #kol_vo_trebsl - количество требуемых слоев в сети
    network = []# будет хранить все слои
    second_sloi_neiron = kol_vo_neir1s * 2
    network.append([None] * kol_vo_neir1s)  # добавляем в конец списка нужное кол-во элементов
    network.append(second_sloi_neiron * [None])
    if second_sloi_neiron  % 2 == 0:# вроде как округление до четных вверъх
        second_sloi_neiron = second_sloi_neiron
    else:
        second_sloi_neiron = second_sloi_neiron + 1
    for i in range(1, kol_vo_trebsl):
        cur_neurons = max(1, second_sloi_neiron //2 )# max для того чтобы если кто-то додумается ввести отрицательное количество слоев, то выводилось бы 1
        network.append([None] * cur_neurons)
        second_sloi_neiron = cur_neurons # обновляем кол-во нейронов для следущего слоя
    return network # и возвращаем весь список слоев сети

#network = create_network(7, -4) # пример выполнения c отрицательным количеством слоев(проверка на дурака)
network = create_network(5, 3)# обычный пример для слоев
print(network)


# По идее сейчас работает как надо,  это уже измененная версия












