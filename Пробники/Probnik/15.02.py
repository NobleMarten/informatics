# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((y <= z) <= (x and y)) and (x <= w)
#                 if F == 1:
#                     print(x, y, z, w)
# # x y z w
# # 0 1 0 0
# # 0 1 0 1
# # 1 1 0 1



# for n in range(2, 1000):
#     n2 = bin(n)[2:]
#     n2 += n2[1]
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     if n2.count('1') % 2 == 0:
#         n2 += '1'
#     else:
#         n2 += '0'
#     R = int(n2, 2)
#     if R > 160:
#         print(n)



# from turtle import *
# tracer(0)
# k = 30
# pendown()
# for i in range(4):
#     forward(3*k)
#     right(90)
#     forward(3*k)
#     right(90)
#     forward(1*k)
#     right(90)
#     forward(1*k)
#     right(90)
# penup()
# for x in range(0, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(4)
# done()



# from itertools import *
# numb = 0
# for i in product('АМРТ', repeat=3):
#     numb += 1
#     if i.count('А') == 0:
#         print(numb, i)



# s = '7'*40
# while '7777' in s or '3333' in s:
#     if '3333' in s:
#         s = s.replace('3333', '77', 1)
#     else:
#         s = s.replace('7777', '33', 1)
# print(s)



# for x in '01234567890ABCDEF':
#     if (int(f'{x}432', 16) + int(f'234{x}', 16)) % 15 == 0:
#         print((int(f'{x}432', 16) + int(f'234{x}', 16)) // 15)



# def dell(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((not(dell(x, A))) and dell(x, 8)) <= (not(dell(x, 36)))) == False:
#             break
#     else:
#         print(A)


# def f(n):
#     if n < 3:
#         return 1
#     if n >= 3:
#         return f(n-2) * (n+3)
# print(f(7))



# f = open('17.2 (2).txt')
# a = [int(s) for s in f]
# pari = []
# for i in range(0, len(a)-1):
#     if (a[i] + a[i+1]) % 4 == 0 and (a[i] + a[i+1]) % 7 != 0 and (str(a[i]*a[i+1])[-1]) == '3':
#         pari.append(a[i]+a[i+1])
# print(len(pari), min(pari))
# #174-15856 ответ


# def win1(x, s):
#     return (x+s < 234) and (x + s + 1) >= 234 or (x + s * 5) >= 234 or (s + x * 5) >= 234
# def loss1(x, s):
#     return (not(win1(x, s))) and win1(x+1, s) and win1(s+1, x) and win1(x*5, s) and win1(s*5, x)
# def win2(x, s):
#     return loss1(x+1, s) or loss1(s+1, x) or loss1(x*5, s) or loss1(s*5, x)
# def loss12(x, s):
#     return (win1(x+1, s) or win2(x+1, s)) and (win1(s+1, x) or win2(s+1, x)) \
#         and (win1(x*5, s) or win2(x*5, s)) and (win1(s*5, x) or win2(s*5, x))
#
# x = 7
# for s in range(1, 226+1):
#     if loss12(x, s):
#         print(s)


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start*3, end)
# print(task23(1, 28))



# from fnmatch import *
# for x in range(127, 10**9 + 1, 127):
#     if fnmatch(str(x), '215*414?'):
#         print(x, x // 127)
# #ответ
# #21504148 169324