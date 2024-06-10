# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and (not(z))) or (y == z) or (not(w))
#                 if F == 0:
#                     print(x, y, z, w)
# x y z w
# 0 0 1 1
# 0 1 0 1
# 1 0 1 1
# wyzx
import sys
# for n in range(1, 10000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += '01'
#     else:
#         n2 = '1' + n2 + '1'
#     r = int(n2, 2)
#     if r > 156:
#         print(n)


# from turtle import *
# left(90)
# tracer(0)
# pendown()
# k = 20
# for i in range(2):
#     forward(13*k)
#     right(90)
#     forward(18*k)
#     right(90)
# penup()
# forward(5*k)
# right(90)
# forward(9*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(11*k)
#     right(90)
#     forward(7*k)
#     right(90)
# penup()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         setpos(x*k, y*k)
#         dot(4)
# done()


# from itertools import *
# numb = 0
# for i in product('АПРСУ', repeat=5):
#     numb += 1
#     s = ''.join(i)
#     if i.count('У') <= 1 and 'АА' not in s:
#         print(numb)


# f = open('9')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     if (max(a) < (a[0] + a[1] + a[2])) and ((a[0]+a[-1]) == (a[1]+a[2])):
#         cnt += 1
# print(cnt)



# s = '8'*45
# while '1111' in s or '8888' in s:
#     if '1111' in s:
#         s = s.replace('1111', '88', 1)
#     else:
#         s = s.replace('8888', '11', 1)
# print(s)


# s = 3 * 2187**2020 + 3 * 729**2021 - 2 * 81**2022 + 27**2023 - 4 * 3**2024 - 2029
# cnt = 0
# while s > 0:
#     if s % 27 > 9:
#         cnt += 1
#     s = s // 27
# print(cnt)


# for x in '0123456789ABCDEFGHIJKLMNOPQ':
#     if (int(f'123{x}24', 27) + int(f'135{x}78', 27)) % 26 == 0:
#         print((int(f'123{x}24', 27) + int(f'135{x}78', 27)) // 26)


# def dell(n, m):
#     return n % m == 0
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if ((not(dell(x, A))) <= (dell(x, 28) <= (not(dell(x, 49))))) == False:
#             break
#     else:
#         print(A)


# b = list(range(24, 91))
# c = list(range(47, 116))
# A = []
# for x in range(1, 10000):
#     if ((x in c) <= (((not(x in A)) and (x in b)) <= (not(x in c)))) == False:
#         A.append(x)
# print(A)


# from sys import *
# sys.setrecursionlimit(30000)
# def f(n):
#     if n <= 7:
#         return 1
#     if n > 7:
#         return n + 2 + f(n-1)
# print(f(2024)-f(2020))


# f = open('17.txt')
# a = [int(s) for s in f]
# max_19 = []
# pari = []
# for i in range(len(a)):
#     if a[i] % 19 == 0:
#         max_19.append(a[i])
# max19 = max(max_19)
# for i in range(len(a)-1):
#     if (a[i] > max19) or (a[i+1] > max19):
#         pari.append(a[i]+a[i+1])
# print(len(pari), max(pari))



# (x+1, s) (x*2, s) (x, s+1) (x, s*2)
def win1(x, s):
    return (x+s) > 123 and (x+1+s) >= 123 or (x*2+s) >= 123 or (x+s*2) >= 123
def los1(x, s):
    return (not(win1(x, s))) and win1(x+1, s) and win1(x*2, s) and win1(x, s+1) and win1(x, s*2)
def win2(x, s):
    return los1(x + 1, s) or los1(x * 2, s) or los1(x, s + 1) or los1(x, s * 2)
def los12(x, s):
    return (win1(x+1, s) or win2(x+1, s)) and (win1(x*2, s) or win2(x*2, s)) and \
        (win1(x, s+1) or win2(x, s+1)) and (win1(x, s*2) or win2(x, s*2)) and \
        (win2(x + 1, s) or win2(x * 2, s) or win2(x, s + 1) or win2(x, s * 2))


x = 13
# for s in range(1, 110):
#     if win1(x+1, s) or win1(x*2, s) or win1(x, s+1) or win1(x, s*2):
#         print(s)
# for s in range(1, 110):
#     if win2(x, s):
#         print(s)
# for s in range(1, 110):
#     if los12(x, s):
#         print(s)