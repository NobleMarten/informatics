# def age(year_born, year_today):
#     return year_today - year_born
# print(age(2000, 2024))


# def kvadrat(x):
#     return x**2
# print(kvadrat(7))


# def privet_4_raza():
#     print('privet')
#     print('privet')
#     print('privet')
#     print('privet')
#
# privet_4_raza()
# print(privet_4_raza())


# 0

# в тетради

# 1
# def F(n):
#     if n < 2:
#         return 1
#     if n >= 2:
#         return F(n-1) * (n+5)
# print(F(9))


# 2
# def F(n):
#     if n == 1:
#         return 3
#     if n > 1:
#         return 4*F(n-1) - 3*n
# print(F(5))

# 3
# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0 and n > 1:
#         return F(n - 1) + 7
#     if n % 2 != 0 and n < 1:
#         return F(n - 2) + 4*n
# print(F(100))


# import sys
# sys.setrecursionlimit(3000)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * F(n-1)
# print(F(2023) / F(2021))

# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0 and n > 1:
#         return F(n-1) + 7
#     if n % 2 != 0 and n > 1:
#         return F(n-2) + 4*n
# print(F(100))

# def F(n):
#     if n <= 4:
#         return 0
#     if n > 4 and n % 4 == 0:
#         return F(n - 1) + 3*n
#     if n > 4 and n % 4 > 0:
#         return F(n - (n % 4)) + 8 * n - 2
# print(F(43))


# def F(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n % 2 == 0 and n > 1:
#         return 2 + int(4 * F(n - 2) / 3) # берем целое число (по условию)
#     if n % 2 != 0 and n > 1:
#         return 2 * n + int((F(n - 1) + F(n - 3) + 7) / 4)
# print(F(32))


# def F(n):
#     if n == 2:
#         return 1
#     if n > 2:
#         return 3 * F(n - 1) + 4*G(n-1) - n*2 + 4
# def G(n):
#     if n == 2:
#         return 1
#     if n > 2:
#         return 4 * F(n-1) + 3*G(n-1) + 6
# print(G(8) + F(8))


# +++
# def F(n):
#     if n > 17:
#         return n*n*n*n + 9
#     if n % 2 == 0 and n <= 17:
#         return 2*F(n+3) + F(n+2)
#     if n % 2 != 0 and n <= 17:
#         return F(n+9) + F(n+4) + n
# cnt = 0
# for n in range(1, 251):
#     if str(F(n)).count('4') == 0: #if '4' not in str(F(n))
#         cnt += 1
# print(cnt)


# def F(n):
#     if n <= 2:
#         return n*n
#     if n % 2 == 0 and n > 2:
#         return n + 7 * F(n-1)
#     if n % 2 != 0 and n > 2:
#         return 3*n*n + F(n-2)
# cnt = 0
# for n in range(1, 664+1):
#     if F(n) % 5 == 0:
#         cnt += 1
# print(cnt)


# def F(n):
#     if n <= 4:
#         return 2
#     if n % 2 == 0 and n > 4:
#         return F(n/6 - 2)
#     if n % 2 != 0 and n > 4:
#         return n*n*n*n
# for n in range(1, 1000):
#     if F(n) > 783:
#         print(n) #7
#         break


# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 5 + F(n-1) - G(n-1)- 4 * n
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) + 3 * G(n-1) + 2 * n
# print(G(21))
# print(2+0+9+7+1+4+3+1)


# import functools
# @lru_cache перед функцией

# def F(n, m):
#     if n == 0 and m == 0:
#         return 0
#     if n > m:
#         return F(n-1, m) + m
#     if n <= m and m > 0:
#         return F(n, m-1) + n
#
# # F(n, m) = 41943204
# cnt = 0
# for n in range(1, 41943204):
#     if 41943204 % n == 0:
#         cnt += 1
# print(cnt)


#ДЗ


# def f(n):
#     if n < 3:
#         return 1
#     if n >= 3:
#         return f(n-2) * (n+3)
# print(f(7))


# def f(n):
#     if n == 1:
#         return 4
#     if n > 1:
#         return 5 * f(n-1) - 2 * n
# print(f(6))


# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0 and n > 1:
#         return f(n-1) + 3
#     if n % 2 != 0 and n > 1:
#         return f(n-3) + 2*n
# print(f(50))


# import sys
# sys.setrecursionlimit(3000)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n-1) + 1
# print(f(2123)/f(2120))


# def f(n):
#     if n == 0 or n == 1:
#         return 5
#     if n > 1 and n % 5 == 0:
#         return f(n-5) / 3 + 9
#     if n > 1 and n % 5 > 0:
#         return f(n-(n % 5)) + n * 2
#
# print(f(42))


# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 2
#     if n % 2 == 0 and n > 1:
#         return 7 + int(3 * f(n-2) / 2)
#     if n % 2 != 0 and n > 1:
#         return 6 * n + int((f(n-2) + f(n-1) + 8) / 5)
# print(f(71))


# def f(n):
#     if n == 2:
#         return 1
#     if n > 2:
#         return 4 * f(n-1) + 2 * g(n-1) - n * 3 + 8
# def g(n):
#     if n == 2:
#         return 1
#     if n > 2:
#         return 3 * f(n-1) + 3 * g(n-1) + n
# print(f(16)+g(16))


# def f(n):
#     if n <= 19:
#         return n * n * n + 22
#     if n % 3 == 0 and n > 19:
#         return f(n-4) + f(n-8)
#     if n % 3 != 3 and n > 19:
#         return f(n-9) + n + 7
# cnt = 0
# for n in range(1, 101):
#     if "1" not in str(f(n)) and "3" not in str(f(n)) and "5" not in str(f(n)) and "7" not in str(
#             f(n)) and "9" not in str(f(n)):
#         cnt += 1
# print(cnt)


# def f(n):
#     if n <= 3:
#         return 1
#     if n % 2 == 0 and n > 3:
#         return f(n / 5 - 3)
#     if n % 2 != 0 and n > 3:
#         return n * n * n
# for n in range(1, 1000):
#     if f(n) > 559:
#         print(n)
#         break
# print(f(8))

