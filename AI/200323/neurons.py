import random


class MathNeuron:
    def __init__(self, x_count, w, theta):
        self.x_count = x_count
        self.w = w + round(random.triangular(-0.25, 0.25), 2)
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