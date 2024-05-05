#2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or y) and (not(y == z)) and (not(w))
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 1 0 0
# 1 0 1 0
# 1 1 0 0
# xzyw


#5
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') > n2.count('0'):
#         n2 += '1'
#     else:
#         n2 += '0'
#     r = int(n2, 2)
#     if r > 80:
#         print(r) #82


#6
# from turtle import *
# tracer(0)
# left(90)
# k = 20
# pendown()
# for i in range(8):
#     right(45)
#     forward(6*k)
# penup()
# for x in range(-10, 15):
#     for y in range(-11, 10):
#         setpos(x*k, y*k)
#         dot(4)
# done() #15


#8
# from itertools import *
# cnt = 0
# for i in product('ТИМОФЕЙ', repeat=5):
#     s = ''.join(i)
#     if s.count('Й') <= 1 and s[0] != 'Й' and s[-1] != 'Й' and 'ЙИ' not in s and 'ИЙ' not in s:
#         cnt += 1
#         print(s)
# print(cnt) #10476


#9
# f = open('9')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(povt) == 4 and sum(set(povt)) > sum(ne_povt):
#         cnt += 1
# print(cnt) #456


#12
# s = '1'*100
# while '111' in s:
#     s = s.replace('11', '2', 1)
#     s = s.replace('22', '1', 1)
# print(s)


#14
# s = 49**8 + 7**24 - 7
# cnt = 0
# while s > 0:
#     if s % 7 == 0:
#         cnt += 1
#     s = s // 7
# print(cnt)


#15
# def dell(n, m):
#     return n % m == 0
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((dell(x, 3) <= (not(dell(x, 5)))) or (x + A >= 90)) == False:
#             break
#     else:
#         print(A)


#16
# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     if n > 2:
#         return f(n-2) * n
# print(f(7))


# 17
# f = open('17.txt')
# a = [int(s) for s in f]
# pari = []
# naim5 = []
# for i in range(len(a)):
#     if 99 < a[i] < 1000 and str(a[i])[-1] == '5':
#         naim5.append(a[i])
# naim5tr = min(naim5)
# for i in range(len(a)-1):
#     if ((len(str(a[i])) == 4) + (len(str(a[i+1])) == 4)) == 1 and (a[i]**2 + a[i+1]**2) % naim5tr == 0:
#         pari.append(a[i]**2 + a[i+1]**2)
# print(len(pari), max(pari))


#23
# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start*2, end)
# print(task23(3, 13)*task23(13, 30)*task23(30, 60))


#24
# f = open('24 (9).txt')
# s = f.readline()
# cnt = 0
# s = s.replace('O', 'A')
# s = s.replace('C', 'F')
# s = s.replace('D', 'F')
# print(s)


#25
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '3?2258*4'):
        print(x, x // 2024)


#27
# f = open('27_A.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(len(a)):
#     for j in range(i+k, n):
#         for j2 in range(j+k, n):
#             res.append(a[i]+a[j]+a[j2])
# print(min(res))