# fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(31))


# Получить идентификатор id
# x = [1, 2, 3]
# print(id(x))
# print(id([1, 2, 3]))


# Ссылаются ли переменные на один объект можно оператором is
# x = [1, 2, 3]
# y = x
# y is x # True - потому что обе переменных ссылаются на один объект
# y is [1, 2, 3] # False - потому что этот список был создан позже, чем список присвоенный переменной x


# Изменяется объект, а не переменная:
# x = [1, 2, 3]
# y = x
# print(y is x)
# x.append(4)
# print(x)
# print(y)


# Тип объекта не может быть изменен после создания объекта
# Узнать тип объекта можно с помощью функции type()
# x = [1, 2, 3]
# print(type(x))
# print(type(4))
# print(type(type(x)))


# Типы объектов в Python есть изменяемые - Mutable и неизменяемые Immutable
# Immutable - числа, int, float, complex, bool, tuple, str, frozenset - неизменяемое множество
# Mutable - list - список, dict - словарь, set - множество