#2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(x <= z)) or (y == w) or y
#                 if F == 0:
#                     print(x, y, z, w)
#zxyw


#5
# def chet(x):
#     s = ''
#     while x > 0:
#         s = str(x%4) + s
#         x = x // 4
# for n in range(1, 1000):
#     n4 = chet(n)
#     if n % 4 == 0:
#         n4 += n4[-2:]
#     else:
#         n4 += chet((n % 4) * 2)
#     r = int(n4, 4)
#     if r < 261:
#         print(n)


#6
# from turtle import *
# k = 10
# left(90)
# tracer(0)
# for i in range(3):
#     pendown()
#     for j in range(2):
#         forward(10*k)
#         right(90)
#         forward(10*k)
#         right(90)
#     penup()
#     forward(5*k)
#     right(90)
#     forward(5*k)
#     left(90)
# penup()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         setpos(x*k, y*k)
#         dot(4)
# done()


#8
# from itertools import *
# cnt = 0
# numb = 0
# for i in product('АГИЛМНОФ', repeat=5):
#     numb += 1
#     if i[0] != 'Н' and i.count('О') <= 1 and numb % 2 != 0:
#         cnt += 1
# print(cnt)


#9
# f = open('9')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt3 = [x for x in a if a.count(x) == 3]
#     povt2 = [x for x in a if a.count(x) == 2]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(set(povt3)) == 1 and len(set(povt2)) == 1 and len(ne_povt) == 3 and sum(ne_povt)/ 3 <= povt3[0]:
#         cnt += 1
# print(cnt)


#13
# from ipaddress import *
# cnt = 0
# ip_net = ip_network('122.159.136.144/255.255.255.248')
# for ip_add in ip_net:
#     if bin(int(ip_add)).count('1') % 4 != 0:
#         cnt += 1
# print(cnt)


#14
# for x in '0123456789ABCDEFGHIJK':
#     for y in '0123456789ABCDEFGHIJK':
#         if (int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) % 18 != 0:
#             break
#     else:
#         print(x, (int(f'125{x}9', 21) + int(f'36599', 21)) // 18)
#3 47594


#17
# f = open('17 (7).txt')
# a = [int(s) for s in f]
# min700 = [x for x in a if str(x)[-3:] == '700']
# troiki = []
# for i in range(len(a)-2):
#     if ((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i+1]))) == 5) + (len(str(abs(a[i+2]))) == 5)) <= 2 and\
#         sum(a[i:i+3]) >= min(min700):
#         troiki.append(sum(a[i:i+3]))
# print(len(troiki), min(troiki))
# #2268 -85393


#19-21
# from math import prod
# def moves(x, s):
#     return (x+2, s), (x+5, s), (x, s+2), (x, s+5)
#
# @lru_cache(None)
# def game(x, s):
#     if any(prod(m) >= 102 for m in moves(x, s)): return 'WIN1'
#     # if any(game(*m) >= 'Win1' for m in moves(x, s)): return 'ans19'
#     if all(game(*m) >= 'WIN1' for m in moves(x, s)): return 'LOSS1'
#     if any(game(*m) >= 'LOSS1' for m in moves(x, s)): return 'WIN2'
#     if all(game(*m) >= 'WIN1' or game(*m) >= 'WIN2' for m in moves(x, s)): return 'LOSS12'
# x = 4
# for s in range(1, 26):
#     if game(x, s) == 'LOSS12':
#         print(s)


#24
# f = open('24 (10).txt')
# s = 'A' + f.readline() + 'A'
# ind_A = []
# for i in range(len(s)):
#     if s[i] == 'A':
#         ind_A.append(i)
# res = []
# for i in range(499, len(ind_A)):
#     res.append((ind_A[i] - ind_A[i - 499] + 1))
# print(min(res))


#27
f = open('27.A.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(s) for s in f]
res = []
for i in range(n):
    for j in range(i+k, n):
        for j2 in range(j+k, n):
            res.append(a[i]*a[j]*a[j2])
print(min(res))