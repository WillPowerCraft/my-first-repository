# while - цикл, выполняющий итерации до тех пор пока условие не будет достигнуто
# i = 0
# while i < 10:
#     print('Привет')
#     i += 1

# Пример while часто используется в коде
# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)

# # Обработка цифр числа
# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа
#     print(n, last_digit)

# Если ли в числе цифра 7
num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
        num = 0
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')