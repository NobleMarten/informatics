# нужно разобрать!!!
# №5
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n // 3 == 0:
#         n2 += n2[-3::]
#     else:
#         n2 += bin((n // 3) * 3)[2:]
#     R = int(n2, 2)
#     if R < 170:
#         print(R) #169
#
# №12
# for n in range(4, 10000):
#     s = '5' + '2'*n
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72', '2', 1)
#         if '522' in s:
#             s = s.replace('522', '27', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#     summ = s.count('2')*2 + s.count('5')*5 + s.count('7')*7
#     if summ == 63:
#         print(n)
#         break
#
# №14
# n = 9 * 19**7 + 8 * 19**6 + 7 * 19**4 + 9 * 19**3 + 6 * 19**2 + 4 * 19 + 1 #x* 19**5
# m = 3 * 19**4 + 6 * 19**3 + 1 * 19 + 4 #x * 19**2
# k = 7 * 19**3 + 3 * 19**2 + 4 #x * 19
# for x in range(0, 19):
#     if (n + x * 19**5 + m + x * 19**2 + k + x * 19) % 18 == 0:
#         print((n + x * 19**5 + m + x * 19**2 + k + x * 19) // 18)
#
# №16
# import sys
# sys.setrecursionlimit(3000)
# def f(n):
#     if n < 11:
#         return n
#     if n >= 11:
#         return n + f(n-1)
# print(f(2024)-f(2021))
#
#
# №23
def task23(start, end):
    if start > end:
        return 0
    if start == 17:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+2, end) + task23(start+3, end) + task23(start*2, end)
print(task23(3, 10) * task23(10, 25))
