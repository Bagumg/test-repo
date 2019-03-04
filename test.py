# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import re
from math import sqrt

class Figure:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def length(self):
        length = round(sqrt(((int(self.second[0]) - int(self.first[0])) ** 2) + ((int(self.second[1]) - int(self.first[1]))) ** 2), 2)
        return length



class Triangle(Figure):
    def __init__(self, A, B, C):
        self.A = re.split(r',', A)
        self.B = re.split(r',', B)
        self.C = re.split(r',', C)
        super(Triangle, self).__init__(first=self.A, second=self.B)
    def length(self):
        return super().length()

tri = Triangle('198,57', '19,1', '13,792')
fig = Figure('198,57', '19,1')
print(fig.length())
print(tri.length())


"""
# Вычисляет длины сторон треугольника по координатам вершин
    def side_length(self):
        AB = round(sqrt(((int(self.B[0]) - int(self.A[0])) ** 2) + ((int(self.B[1]) - int(self.A[1]))) ** 2), 2)
        AC = round(sqrt(((int(self.C[0]) - int(self.A[0])) ** 2) + ((int(self.C[1]) - int(self.A[1]))) ** 2), 2)
        BC = round(sqrt(((int(self.C[0]) - int(self.B[0])) ** 2) + ((int(self.C[1]) - int(self.B[1]))) ** 2), 2)
        return AB, AC, BC

# Вычисляет высоту треуголька к одной из сторон
# Стороны указываются в аргументах, от 0 до 2
    def triange_height(self, side):
        square = self.square()
        side_length = self.side_length()
        height = round((2 * int(square)) / int(side_length[side]), 2)
        return height

# Вычисляет периметр треугольника
    def triangle_perim(self):
        perim = 0
        sides = self.side_length()
        for i in range(len(sides)):
            perim += sides[i]
        return perim

sq = Triangle('198,57', '19,1', '13,792')
print(sq.square())
print(sq.side_length())
print(sq.triange_height(0))
print(sq.triangle_perim())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze():
    def __init__(self, A, B, C, D):
        self.A = re.split(r',', A)
        self.B = re.split(r',', B)
        self.C = re.split(r',', C)
        self.D = re.split(r',', D)

# Проверяем, является ли трапеция равнобедренной.
# Если диагонали раны, то трапеция равнобедренная
    def is_isosceles(self):
        BD = round(sqrt(((int(self.B[0]) - int(self.D[0])) ** 2) + ((int(self.B[1]) - int(self.D[1]))) ** 2), 2)
        AC = round(sqrt(((int(self.A[0]) - int(self.C[0])) ** 2) + ((int(self.A[1]) - int(self.C[1]))) ** 2), 2)
        if BD == AC:
            return True
        else:
            return False

# Вычисляет длины сторон
    def side_length(self):
        AB = round(sqrt(((int(self.A[0]) - int(self.B[0])) ** 2) + ((int(self.A[1]) - int(self.B[1]))) ** 2), 2)
        BC = round(sqrt(((int(self.B[0]) - int(self.C[0])) ** 2) + ((int(self.B[1]) - int(self.C[1]))) ** 2), 2)
        CD = round(sqrt(((int(self.C[0]) - int(self.D[0])) ** 2) + ((int(self.C[1]) - int(self.D[1]))) ** 2), 2)
        AD = round(sqrt(((int(self.A[0]) - int(self.D[0])) ** 2) + ((int(self.A[1]) - int(self.D[1]))) ** 2), 2)
        return AB, BC, CD, AD

# Вычисляет периметр трапеции
    def trapeze_perim(self):
        perim = 0
        sides = self.side_length()
        for i in range(len(sides)):
            perim += sides[i]
        return round(perim, 2)

# Вычисляет высоту трапеции
    def trapeze_height(self):
        height = round((sqrt((4 * self.side_length()[0]) - ((self.side_length()[3] - self.side_length()[1]) ** 2))) / 2, 2)
        return height

# Вычисляет площадь трапеции
    def trapeze_suqare(self):
        square = ((self.side_length()[3] + self.side_length()[1]) / 2) * self.trapeze_height()
        return round(square, 2)


tr = Trapeze('1,1', '5,100', '100,96', '100, 1')
print(tr.is_isosceles())
print(tr.side_length())
print(tr.trapeze_perim())
print(tr.trapeze_height())
print(tr.trapeze_suqare())
"""