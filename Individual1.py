#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.

import sys

if __name__ == '__main__':

    trains = []


    def add():
        name = input("Название пункта назначения: ")
        num = int(input("Номер поезда: "))
        time = input("Время отправления: ")

        train = {
            'name': name,
            'num': num,
            'time': time,
        }

        trains.append(train)
        if len(trains) > 1:
            trains.sort(key=lambda item: item.get('num', ''))


    def list():
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)

        for idx, train in enumerate(trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                    idx,
                    train.get('name', ''),
                    train.get('num', ''),
                    train.get('time', 0)
                )
            )

        print(line)


    def select():
        parts = command.split(' ', maxsplit=2)

        number = int(parts[1])

        count = 0
        for train in trains:
            if train.get('num') == number:
                count += 1
                print('Номер поезда:', train.get('num', ''))
                print('Пункт назначения:', train.get('name', ''))
                print('Время отправления:', train.get('time', ''))

        if count == 0:
            print("Таких поездов нет!")


    def help():
        print("Список команд:\n")
        print("add - добавить поезд;")
        print("list - вывести список поездов;")
        print("select <номер поезда> - запросить информацию о выбранном поезде;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            add()

        elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

        elif command == 'help':
            help()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
