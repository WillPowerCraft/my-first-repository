# Пользовательские функции
# def - define – определять)


# Собственные функции
# В предыдущих уроках мы использовали встроенные в Python
# функции print(), input(), int(), str(), len() и многие другие.
# Пришло время начать писать свои собственные функции.
# Имена функциям назначаются так же, как переменным
# def название_функции():
#     блок кода
# Пример:
# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
# draw_box()
# print()
# draw_box()
# print()
# draw_box()



# Иногда, при объявлении функции требуется сделать своего рода заглушку,
# чтобы функция ничего не выполняла. Тогда мы используем ключевое слово pass
# def do_nothing():
#     pass



# Функции по параметрам
# Пример
# def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)
# draw_box(5, 9)
# print()
# draw_box(2, 3)

# Пример с подставлением в параметры функции переменных
# m = 5
# n = 10
# draw_box(m, n)

# Параметры функции указываются при создании фунции
# Аргументы функции указываются при обращении к функции



# Локальные и глобальные переменные

# Локальные - те что объявляются внутри фунции, остальной код не имеет к ним доступа
# Разные функции могут иметь локальные переменные с одинаковыми именами,
# потому что они не видят локальных переменных друг друга.
# Параметрическая переменная - Область действия параметрической переменной — функция,
# в которой этот параметр используется.
# К параметрической переменной имеет доступ весь программный код этой функции.
# Параметрическая переменная тоже локальная.
# Память для локальных переменных выделяется на время исполнения данной функции в специальной области,
# называемой стеком. При завершении работы функции память освобождается,
# внутренние результаты работы функции не сохраняются от одного обращения к другому.

# Глобальные переменные - зло
# Глобальными называются переменные, объявленные в основной программе и доступные
# как программе, так и всем ее функциям.
# Обмен информацией между основной программой и функциями осуществляется
# только с помощью параметров функций и глобальных переменных.
# Функция может использовать любые глобальные переменные кроме имеющих те же имена,
# что и ее локальные переменные. Если в функции объявлена локальная переменная с тем же именем,
# что у одной из глобальных, то данная глобальная переменная становится недоступной в этой функции,
# и при указании идентификатора переменной произойдет обращение к локальной переменной функции,
# а не одноименной глобальной.
# В большинстве случаев следует создавать переменные локально
# и передавать их в качестве аргументов в функции, которым нужно к ним обратиться.

# Глобальные переменные - Константы
# Математический модуль math  определяет две глобальные переменные,
# math.pi и math.e, которым присвоены математические значения констант
# π = 3.14159265 и e = 2.71828.

# Если нужно, чтобы инструкция внутри функции присваивала значение глобальной переменной,
# то требуется дополнительный шаг. В этом случае,
# глобальная переменная должна быть объявлена внутри функции.
# Пример:
# def print_texas():
#     global birds
#     birds = 5000
#     print('В Техасе обитает', birds, 'птиц.')
#
# def print_california():
#     print('В Калифорнии обитает', birds, 'птиц.')
#
# print_texas()
# print_california()



# Функции с возвратом значения

# Примеры фунций с возвратом значения:
# функция int() – преобразует строку к целому числу и возвращает его;
# функция float() – преобразует строку к вещественному числу и возвращает его;
# функция range() – возвращает последовательность целых чисел 0, 1, 2, ...;
# функция abs() – возвращает абсолютное значение числа (модуль числа);
# функция len() – возвращает длину строки или списка.

# Функцию с возвратом значения пишут точно так же, как и без,
# но она должна иметь инструкцию return.

# def название_функции():
#     блок кода
#     return выражение

# Пример функции переводящей градусы по Фаренгейту в градусы Цельсия:
# функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
# # основная программа
# temp = float(input('Bвeдите количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия

# В модуле math имеется встроенная функция hypot(x, у)
# которая возвращает длину гипотенузы прямоугольного треугольника с катетами x и y.