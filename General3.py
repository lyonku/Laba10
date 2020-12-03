#!/usr/bin/evn python3
# -*- config: utf-8 -*-

# Решите следующую задачу: напишите функцию, которая считывает с клавиатуры числа и
# перемножает их до тех пор, пока не будет введен 0. Функция должна возвращать
# полученное произведение. Вызовите функцию и выведите на экран результат ее работы.


if __name__ == '__main__':

    def composition():

        while True:
            a = int(input('first number: '))
            b = int(input('second number: '))

            if a == 0 or b == 0:
                break

            p = a * b
            print('Composition:', p)

    composition()
