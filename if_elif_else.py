# Пример самописного простого калькулятора

a, b, c = int(input()), int(input()), str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/' and b == 0:
    print('На ноль делить нельзя!')
else:
    print(a / b)