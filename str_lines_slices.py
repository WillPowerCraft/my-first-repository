# Python поддерживает emoji
# Индексация символов в строке - указать конкретный символ внутри []
# s = 'Hello'
# print(s[0])
# # Python индексирует символы в строке по возрастающей и по убывающей '-1' - последний символ строки
# print(s[-1])
# # Пример сканирования каждого символа в строке
# # Такой способ удобен, если нужно узнать не только символ, но и индекс символа (i)
# for i in range(len(s)):
#     print(s[i])
# # Тот же результат без индекса - короче
# for c in s:
#     print(c)
#
# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# Slice - срез для работы с целыми частями строки в диапазоне
s = 'abcdefghij'
print(s)
print(s[2:5])
print(s[0:6])
print(s[2:7])
# Slice from digit to end or from start to digit
print(s[2:])
print(s[:2])
print(s[:])

# Slice with '-digits'
print(s[-9:-4])
print(s[-3:])
print(s[:-3])

# Slice step - 3d not mandatory param in Slice what mean slice digit every X
print()
print(s)
print(s[::-1]) # turn last to start digit
print(s[::-2])
print(s[1:7:2])
print(s[3::2])
print(s[:7:3])
print(s[::2])

# Changing string digits
# if i need change digit in string i do this code
s = s[:4] + 'XXX' + s[5:]
print(s)