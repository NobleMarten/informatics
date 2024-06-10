# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) * (n+1) + 5
# print(f(7))
import sys
# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 != 0 and n > 1:
#         return n + 5*f(n-2)
#     if n % 2 == 0 and n > 1:
#         return 2*n*f(n-1)
# print(f(9))


# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) - 4 * g(n-1)
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) + 2 * g(n-1)
# print(g(10))
# print(f(21))
# print(abs(9-27))


# def f(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 3
#     if n % 2 != 0 and n > 2:
#         return int((f(n-2) + f(n-2)) // 7)
#     if n % 2 == 0 and n > 2:
#         return 7*n - int(f(n-1)/2 + 5)
# print(f(40))


# def f(n):
#     if n < 2:
#         return n
#     if n % 2 == 0 and n >= 2:
#         return f(n//2) + 1
#     if n % 2 != 0 and n >= 2:
#         return f(3*n+1) + 1
# for n in range(1, 10000):
#     if f(n) > 150:
#         print(n)


from sys import *
# sys.setrecursionlimit(3000)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * n * f(n-1) - 1
# print(f(2000)/f(1997))

# sys.setrecursionlimit(3000)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (2 * n - 2) * f(n-1)
# print(f(2012)/f(2010))




# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*3, end)
# print(task23(1, 15))


def task23(start, end):
    if start > end:
        return 0
    if start == 5:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start*3, end)
print(task23(1, 21))