# №16

# f = [0]*10000
# for n in range(10000):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (2*n-2) * f[n-1]
# print(f[2012] // f[2010])


# f = [0]*10000
# for n in range(10000):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n + 2 + f[n-1]
# print(f[2028] + f[2022])


# f = [0]*1000
# for n in range(1000):
#     if n == 1:
#         f[n] = 2
#     if n == 2:
#         f[n] = 3
#     if n % 2 != 0 and n > 2:
#         f[n] = int((f[n-2] + f[n-2]) / 7)
#     if n % 2 == 0 and n > 2:
#         f[n] = 7 * n - int(f[n-1] / 2 + 5)
# print(f[40])


# def f(n):
#     if n <= 14:
#         return n * n * n + 22
#     if n % 3 == 0 and n > 14:
#         return f(n-4) + f(n-8)
#     if n % 3 != 0 and n > 14:
#         return f(n-9) + n + 7
# cnt = 0
# for n in range(1, 199+1):
#     if (str(f(n)).count('1') + str(f(n)).count('3') + str(f(n)).count('5') + str(f(n)).count('7') +
#         str(f(n)).count('9') == 0):
#         cnt += 1
# print(cnt)


# def f(n):
#     if n <= 4:
#         return n
#     if n > 4 and n % 2 == 0:
#         return n + 4 * f(n-1)
#     if n > 4 and n % 2 != 0:
#         return 2 * n * n * n + f(n-1)
# cnt = 0
# for n in range(1, 401):
#     if f(n) % 8 == 0:
#         cnt += 1
# print(cnt)


# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3 * f(n-1) - g(n-1)
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * f(n-1) + 2 * g(n-1) + n * n
# print(g(5))


# from functools import *
# def p(n):
#     a = []
#     for i in range(len(str(n))):
#         a.append(str(n)[i])
#     return sum([int(item) for item in a])
# @lru_cache
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3 * f(n - 1) + 2 * g(n - 1) + n * n
# @lru_cache
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * f(n-1) + 3 * g(n-1) + n * 5
# print(p(g(222))) #685
# print(p(f(333))) #1049



# №23


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start == 5:
#         return 0
#     if start < end:
#         return task23(start+1, end) + task23(start*3, end)
# print(task23(1, 21))


# def task23(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start-1, end) + task23(start//2, end)
# print(task23(43,10) * task23(10, 1))


# def task23(start, end, k):
#     if start == end and k == 2:
#         return 1
#     if k < 2:
#         return task23(start+2, end, k) + task23(start+3, end, k) \
#                 + task23(start*2, end, k+1) + task23(start*3, end, k+1)
#     if k >= 2:
#         task23(start + 2, end, k) + task23(start + 3, end, k)
#     return 0
# print(task23(1, 51, 0))


# def task23(start, end, hist):
#     if start > end or '++++' in hist or '****' in hist:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end, hist+'+') + task23(start*3, end, hist+'*')
# print(task23(1, 30, ''))


# def task23(start, end, hist=''):
#     if start-1 > end or '--' in hist or '****' in hist:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start-1, end, hist+'-') + task23(start*2, end, hist+'*') + task23(start*3, end, hist+'*')
# print(task23(4, 116))