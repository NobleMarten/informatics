#5

# a = []
# def f(n):
#     s = ''
#     while n > 0:
#         s = str(n%3) + s
#         n = n // 3
#     return s
# for n in range(1, 1000):
#     n3 = f(n)
#     if n % 3 == 0:
#         n3 = '1' + n3
#         n3 += '02'
#     else:
#         m = n % 3 * 4
#         m3 = f(m)
#         n3 += m3
#     R = int(n3, 3)
#     if R < 199:
#         a.append(n)
# print(max(a))


#12


# for n in range(4, 10000):
#     s = '1' + n*'8'
#     while '18' in s or '388' in s or '888' in s:
#         if '18' in s:
#             s = s.replace('18', '8', 1)
#         if '388' in s:
#             s = s.replace('388', '81', 1)
#         if '888' in s:
#             s = s.replace('888', '3', 1)
#     if s.count('1') == 3:
#         print(n)


#14


m = 7 * 23**6 + 3 * 23**4 + 8 * 23**3 + 5 * 23**2 + 9 * 23 + 6 #x*23**5
n = 1 * 23**4 + 4 * 23**3 + 3 * 23 + 6 #x*23**2
s = 6 * 23**3 + 1 * 23**2 + 7 #x*23
for x in range(1, 23):
    if (m + x * 23**5 + n + x * 23**2 + s + x * 23) % 22 == 0:
        print((m + x * 23**5 + n + x * 23**2 + s + x * 23) // 22)


#23

# def task23(start, end):
#     if start < end:
#         return 0
#     if start == 7:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start-1, end) + task23(start-3, end) + task23(start//2, end)
# print(task23(19, 10) * task23(10, 3))