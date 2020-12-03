#!/usr/bin/evn python3
# -*- config: utf-8 -*-

# Решите следующую задачу: в основной ветке программы вызывается функция cylinder(),
# которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
# вычисляющая площадь круга по формуле pi*(r^2). В теле cylinder() у пользователя
# спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
# которая вычисляется по формуле 2*pi*r*h, или полную площадь цилиндра. В последнем
# случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().

import math


if __name__ == '__main__':
    h = int(input('Enter height: '))
    r = int(input('Enter radius: '))

    def cylinder():

        def circle():
            square = side + 2 * (math.pi * (r ** 2))
            return square

        q = input("Get the full area of a cylinder - 1, or just the side area - 2 (1/2)")

        side = 2 * math.pi * r * h

        if q == "1":
            print(circle())

        elif q == "2":
            print(side)


    cylinder()
