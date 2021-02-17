# Цикл for
# for i in range(4):
#     print('Привет')
#
# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# Блок команд, который выполняется в цикле for называется телом цикла.
# Однократное выполнение тела цикла называется итерацией цикла.
# Переменная i используется как порядковый номер итерации по умолчанию начиная с 0
# for i in range(10):
#     print(i, '-- Привет')

# Чтобы начало отсчета было с единицы
# for i in range(10):
#     print(i + 1, '-- Привет')

# Бывают ситуации когда переменная цикла не используется в теле цикла.
# В таком случае, вместо того, чтобы давать ей имя, мы можем указать символ нижнего подчеркивания _
# for _ in range(5):
#     print('Python - awesome!')

# for i in range(10):
#     print(i, input())

# range(n) - создает последовательность от 0 до n - 1
# range(n, m) - создает последовательность от n до m - 1
# если n > m, то это приводит к генерации пустой последовательности
# range(n, m, k) - создает последовательно от n до m - 1 с шагом генерации k
# range(n, m, k) - если n > m и k < 0 то сгенерируется отрицательная последовательность

# for _ in range(1, 11, 2):
#     print(_)

# Переменная счетчика - каждый раз при удовлетворении условиям в цикле прибавляем к ней 1
# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )

# Example
# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

# Example
# total = 0
# for i in range(10):
#     num = int(input())
#     total = total + num
# average = total / 10
# print('Среднее значение равно', average)

# Обмен значений переменных
# Во большинстве языков программирования делают так:
# temp = x
# x = y
# y = temp
# а в Питоне делают круче:
# x, y = y, x

# Сигнальная метка - flag = true false
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num != 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# Min Max
# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# largest = int(input())  # принимаем первое число за максимальное
# for i in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# Расширенные операторы присваивания
# x = 1
# x += 5
# x -= 2
# x *= 10
# x /= 4
# x //= 4
# x %= 4

# # Задача - считать 10 чисел и вывести произведение отличных от нуля чисел
# # Вариант с if
# co = 1
# for i in range(10):
#     co2 = int(input())
#     if co2 > 0:
#         co *= co2
# print(co)
# # Вариант без if
# co = 1
# for _ in range(10):
#     co2 = int(input())
#     co *= co2 + (co2 == 0) # Если выражение истинно (True), то вместо него подставляется 1, а если ложно - 0
# print(co)


#print('NO' if sum(int(input()) % 2 for i in '1234567890') else 'YES')
x = int(input())
if x:
    print('yes')

for i in range(10):
int(input()) % 2