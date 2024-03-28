#2

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w <= x) and ((y and z) == (x or y))
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 0 1 0
# 0 1 1 0
# 1 1 1 0
#yxzw


#5

# for n in range(1, 10000):
#     n2 = bin(n)[2:]
#     n2 = n2[::-1]
#     R = int(n2, 2)
#     if R == 41:
#         print(n)


#8

# from itertools import product
# numb = 1
# for x in product('EHMO', repeat=4):
#     print(numb, x)
#     numb += 1


#12

# s = '1'*72
# while '888' in s or '111' in s:
#     if '111' in s:
#         s = s.replace('111', '8', 1)
#     else:
#         s = s.replace('888', '1', 1)
# print(s)


#14

# s = 16**3300 + 18**2200 - 2**120 - 256
# cnt = 0
# while s > 0:
#     if s % 2 == 1:
#         cnt += 1
#     s = s // 2
# print(cnt)


#15

# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x & 32 != 0) <= ((x & 64 == 0) or (x & A != 0))) == False:
#             break
#     else:
#         print(A)


#16

# def f(n):
#     if n == 5:
#         return 5
#     if n > 5:
#         return 3 * f(n-1) + 5 * g(n-1)
# def g(n):
#     if n == 5:
#         return 5
#     if n > 5:
#         return 5 * f(n-1) - g(n-1)
#
# print(g(9))


#17

# f = open('15_mvwl3ku.txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_pari = []
# for i in range(len(a)-1):
#     if (a[i] % 2 == 0) and (a[i+1] % 2 == 0) or (a[i] % 2 != 0) and (a[i+1] % 2 != 0):
#         sum_pari.append(a[i]+a[i+1])
# print(len(sum_pari), min(sum_pari))
#2501-19660


#19

# def win1(x, s):
#     return (x+2+s) >= 103 or (x+s+2) >= 103 or (x*4 + s) >= 103 or (x + s*4) >= 103
# def loss1(x, s):
#     return not(win1(x, s)) and win1(x+2, s) and win1(x*4, s) and win1(x, s+4) and win1(x, s*4)
# def win2(x, s):
#     return loss1(x+2, s) or loss1(x*4, s) or loss1(x, s+4) or loss1(x, s*4)
# def loss12(x, s):
#     return (win1(x+2, s) or win2(x+2, s)) and (win1(x*4, s) or win2(x*4, s)) and \
#         (win1(x, s+4) or win2(x, s+4)) and (win1(x, s*4) or win2(x, s*4)) and \
#     (win2(x + 2, s) or win2(x * 4, s) or win2(x, s + 4) or win2(x, s * 4))
#
# # (x+2, s) (x*4, s) (x, s+4) (x, s*4)
# x = 5
# for s in range(1, 98):
#     if loss12(x, s):
#         print(s)


#23

# def task23(start, end):
#     if start > end:
#         return 0
#     if start == 50:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*4, end)
# print(task23(1,12)*task23(12,100))


#27


f = open('27_3_A_dz.txt')
n = int(f.readline())
a = [s for s in f]
print(a)