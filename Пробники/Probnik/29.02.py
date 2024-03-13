# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = ((not(y)) or z) <= x
#             if F == False:
#                 print(x, y, z)


# R = []
# for n in range(2, 10000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += n2[:2]
#     else:
#         n2 = '1' + n2 + '0'
#     r = int(n2, 2)
#     if r > 2999:
#         R.append(r)
# print(min(R))


# from turtle import *
# tracer(0)
# pendown()
# left(90)
# k = 50
# for i in range(40):
#     right(100)
#     forward(5*k)
# penup()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(4)
# done()


# from itertools import *
# cnt = 0
# for i in product('КОСА', repeat=7):
#     if i[-1] == 'О' or i[-1] == 'А':
#         print(i)
#         cnt += 1
# print(cnt)


# s = '1'*37
# while '111' in s or '777' in s:
#     if '111' in s:
#         s = s.replace('111', '7', 1)
#     else:
#         s = s.replace('777', '1', 1)
# print(s)


# s = 6542**324 - 3560**67 + 730**12 - 510
# zifri = []
# while s > 0:
#     zifri.append(s % 3)
#     s = s // 3
# print(zifri.count(2))
# cnt = 0
# while s > 0:
#     if s % 3 == 2:
#         cnt += 1
#     s = s // 3
# print(cnt)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x & A != 0) <= (((x & 16 != 0) or (x & 30 == 0)) <= (x & 55 != 0))) == False:
#             break
#     else:
#         print(A)


# def f(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 2
#     if n % 2 == 0 and n > 1:
#         return 5 * n + int(f(n-2)/2) - 1
#     if n % 2 != 0 and n > 1:
#         return 2 + int((f(n-1) + f(n-2)) / 4)
# print(f(15))


# f = open('17.7_6fADpmL.txt')
# a = [int(s) for s in f]
# troiki = []
# for i in range(len(a)-2):
#     if ((a[i] < 0) and (a[i+1] < 0) and (a[i+2] < 0)):
#         troiki.append(a[i]+a[i+1]+a[i+2])
# print(len(troiki), min(troiki))


# def win1(x, s):
#     return (x+s < 222) and (((x+3)*s) >= 222) or (((x+6)*s) >= 222)
#
# def loss1(x, s):
#     return (not(win1(x, s))) and win1(x+3, s) and win1(x+6, s) and win1(x, s+3) and win1(x, s+6)
#
# def win2(x, s):
#     return loss1(x+3, s) or loss1(x+6, s) or loss1(x, s+3) or loss1(x, s+6)
#
# def loss12(x, s):
#     return (win1(x+3, s) or win2(x+3, s)) and (win1(x+6, s) or win2(x+6, s)) and \
#         (win1(x, s+3) or win2(x, s+3)) and (win1(x, s+6) or win2(x, s+6))
#
# x = 8
# for s in range(1, 27+1):
#     if loss12(x, s):
#         print(s)

# (x+3, s) (x+6, s) (x, s+3) (x, s+6)


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*3, end)
# print(task23(1, 15) * task23(15, 53))


