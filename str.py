# функции len() - длина строки str() - строка, оператор in
# s1 = 'abcdef'
# length1 = len(s1)               # считаем длину строки из переменной s1
# length2 = len('Python rocks!')  # считаем длину строкового литерала
# print(length1)
# print(length2)

# Иногда работать переводить число в строку и работать со строкой проще
# num1 = 1777    # целое число
# num2 = 17.77   # число с плавающей точкой
# s1 = str(num1) # преобразовали целое число в строку '1777'
# s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'

# Конкатенация строк (сцепление строк)
# s1 = 'ab' + 'bc'
# s2 = 'bc' + 'ab'
# s3 = s1 + s2 + '!!'
# print(s1)
# print(s2)
# print(s3)
#
# print('a', 'b', 'c', sep='*', end='!')
# print()  # переход на новую строку
# print('a' + '*' + 'b' + '*' + 'c' + '!')

# Умножение строки на число
# s = 'Hi' * 4
# print(s)

# Тройные кавычки позволяют вводить многострочный текст
# print('''Путин - вор!
# Путин - вор!
# Путин - вор!''')

# Оператор in - для проверки есть ли одна строка внутри другой строки
# s = input()
# if 'a' in s:
#     print('Введенная строка содержит символ а')
# else:
#     print('Введенная строка не содержит символ а')

# a = 12345
# b = str(a)
# c = len(b)
# if len(str(a)) == 5:
#     print('yeas')

a = int(input())
b = 'NO'
while len(str(a)) >= 2:
    if a % 10 < a // 10 % 10:
        b = 'YES'
    else:
        b = 'NO'
    a // 10
print(b)