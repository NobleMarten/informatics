# №2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = y and (not(x)) and ((not(z)) or w)
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 1 0 0
# 0 1 0 1
# 0 1 1 1
# xwzy


# №5
# for n in range(1, 10000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#         n2 = '10' + n2[2:]
#     else:
#         n2 += '11'
#         n2 = '11' + n2[2:]
#     R = int(n2, 2)
#     if R < 99:
#         print(n)


# №6
# from turtle import *
# left(90)
# pendown()
# tracer(0)
# k = 50
# for i in range(7):
#     right(90)
#     forward(3*k)
#     for g in range(2):
#         left(90)
#         forward(3*k)
# left(20)
# for i in range(7):
#     right(90)
#     forward(3*k)
#     for g in range(2):
#         left(90)
#         forward(3*k)
# penup()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(4)
# done()


# №8
# from itertools import *
# cnt = 0
# for i in permutations('РАКЕТ', r=5):
#     # s = i.split( )
#     if i[0] != 'А' and 'ТР' not in i:
#         cnt += 1
#         print(i)
# print(cnt)


# №9
# f = open('9')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     if (max(a) - (sum(a)/5)) < ((sum(a)/5) - min(a)):
#         cnt += 1
# print(cnt)


# №12
# for i in range(94, 1000):
#     s = '0'*i
#     while '000' in s:
#         s = s.replace('000', '8', 1)
#         s = s.replace('8888', '00', 1)
#         if s == '00':
#             print(i)


# №14
# for x in '0123456789ABCDEF':
#     if (int(f'{x}ABC', 16) + int(f'DEF{x}', 16)) % 15 == 0:
#         print((int(f'{x}ABC', 16) + int(f'DEF{x}', 16)) // 15)


# №15
# def dell(n, m):
#     return n % m == 0
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((not(dell(x, A))) <= (dell(x, 20) <= (dell(x, 40)))) == False:
#             break
#     else:
#         print(A)


# №16
# import sys
# sys.setrecursionlimit(3000)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * n * f(n-1) + 1000
# print(f(2000)/f(1997))


# # №17
# f = open('17.txt')
# a = [int(s) for s in f]
# max_22 = []
# pari = []
# for i in range(len(a)):
#     if a[i] % 22 == 0:
#         max_22.append(a[i])
# max22 = max(max_22) #99814
# for i in range(len(a)-1):
#     if (a[i] < max22) and (a[i+1] < max22) and (a[i] % 13 == 0 or a[i+1] % 13 == 0):
#         pari.append(a[i]+a[i+1])
# print(len(pari), max(pari)) #5382 199042


# №19-21
def win1(x, s):
    return (x+s > 40) and (x-1+s) <= 40 or (x//2+s) <= 40 or (x+s-1) <= 40 or (x+s//2) <= 40


def loss1(x, s):
    return not (win1(x, s)) and win1(x-1, s) and win1(x // 2, s) and win1(x, s-1) and win1(x, s // 2)


def win2(x, s):
    return loss1(x-1, s) or loss1(x // 2, s) or loss1(x, s-1) or loss1(x, s // 2)


def loss12(x, s):
    return ((win1(x-1, s) or win2(x-1, s)) and (win1(x // 2, s) or win2(x // 2, s)) and
            (win1(x, s-1) or win2(x, s-1)) and (win1(x, s // 2) or win2(x, s // 2)) and
            (win2(x - 1, s) or win2(x // 2, s) or win2(x, s - 1) or win2(x, s // 2)))


x = 6
for s in range(34, 10000):
    if win1(x-1, s) or win1(x // 2, s) or win1(x, s-1) or win1(x, s // 2):
        print(s)
# for s in range(34, 10000):
#     if win2(x, s):
#         print(s)
# for s in range(34, 100000):
#     if loss12(x, s):
#         print(s)
# (x-1, s) (x // 2, s) (x, s-1) (x, s // 2)


# №23
# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*2, end) + task23(start*2+1, end)
# print(task23(2, 90))


# №25
# from fnmatch import *
# for x in range(46, 10**7, 46):
#     if fnmatch(str(x), '12*345*'):
#         print(x, x // 46)
