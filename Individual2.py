#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.

import sys
import json


def add(trains, name, num, time):
    train = {
        'name': name,
        'num': num,
        'time': time,
    }

    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('num', ''))


def list(trains):
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


def select(trains):
    count = 0
    for train in trains:
        if train.get('num') == number:
            count += 1
            print('Номер поезда:', train.get('num', ''))
            print('Пункт назначения:', train.get('name', ''))
            print('Время отправления:', train.get('time', ''))

    if count == 0:
        print("Таких поездов нет!")


def load(parts):
    with open(parts, 'r') as f:
        return trains


def save(trains, parts):
    with open(parts, 'w') as f:
        json.dump(trains, f)


if __name__ == '__main__':

    trains = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            add(trains, name, num, time)

        elif command == 'list':
            print(list(trains))

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])
            select(trains)

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            trains = load(parts[1])

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            save(trains, parts[1])

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
