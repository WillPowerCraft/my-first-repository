# finish = False
# for a in range(1, 151):
#     for b in range(a + 1, 151):
#         for c in range(b + 1, 151):
#             for d in range(c + 1, 151):
#                 print(a, b, c, d)
#                 e = (a ** 5 + b ** 5 + c ** 5 + d ** 5) ** (1 / 5)
#
#                 if a ** 5 + b ** 5 + c ** 5 + d ** 5 == int(e) ** 5:
#                     print(a + b + c + d + e)
#                     finish = True
#                 if finish: break
#             if finish: break
#         if finish: break
#     if finish: break


# Это ФАКРТОРИАЛ ЧИСЛА n
# n = int(input())
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(res)

# a ** 3 + b ** 3 == c ** 3 + d ** 3
# for a in range(1, 33):
#     for b in range(1, 33):
#         for c in range(1, 33):
#             for d in range(1, 33):
#                 if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != c and b != d and a!= d and b!= c and a!= b and c != d:
#                     print(a ** 3 + b ** 3)

#n, b = 14, 'fsfftsfufksttskskt'
#for i in range(len(b)):
#    if ord(b[i]) - n >= ord('a'):
#        print(chr(ord(b[i]) - n), end='')
#    else:
#        print(chr(ord(b[i]) - n + 26), end='')

# s = 'aaffective'
# s[2].replace('f', '')
# print()