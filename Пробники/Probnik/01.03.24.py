# def p_ch(n, k):
#     s = ''
#     while n > 0:
#         s = str(n % k) + s
#         n = n // k
#     return s
#
# for n in range(1, 1000):
#     n5 = p_ch(n, 5)
#     if n % 25 == 0:
#         n5 = n5[-3:] + n5
#     else:
#         n5 += p_ch(n % 25, 5)
#     r = int(n5, 5)
#     if r > 10000:
#         print(n)


# from itertools import *
# cnt = 0
# numb = 0
# for i in product('АЕКПТЧ', repeat=7):
#     numb += 1
#     s = ''.join(i)
#     # if 'АПТЕЧКА' < s < 'ПЕЧАТКА':
#     #     cnt += 1
#     if s == 'АПТЕЧКА':
#         k1 = numb
#     if s == 'ПЕЧАТКА':
#         k2 = numb
# print(k2 - k1 - 1)


# n = abs(18 * 7**108 - 5 * 49**76 + 343**35 - 50)
# summ = 0
# while n > 0:
#     summ = (n % 49) + summ
#     n = n // 49
# print(summ)


# f = open('17.txt')
# a = [int(s) for s in f]
# pari = []
# for i in range(2, len(a)-3):
#     if ((a[i] + a[i+1]) > (a[i-2] + a[i-1])) and ((a[i] + a[i+1]) > (a[i+2] + a[i+3])) and \
#             (a[i] + a[i+1]) > 0 and (a[i-2] + a[i-1]) > 0 and (a[i+2] + a[i+3]) > 0:
#         pari.append(a[i] * a[i+1])
# print(len(pari), min(pari))