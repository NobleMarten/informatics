#5




#12


# a = []
# for n in range(4, 10000):
#     s = '1' + '2'*n
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s:
#             s = s.replace('12', '2', 1)
#         if '322' in s:
#             s = s.replace('322', '21', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#         summ = s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3
#         a.append(summ)
# print(max(a)) #19995


#14

n = 1 * 22**7 + 8 * 22**6 + 8 * 22**4 + 9 * 22**3 + 9 * 22**2 + 5 * 22 + 7 # x * 22**5
m = 8 * 22**4 + 3 * 22 + 3 # x * 22**2
k = 5 * 22**4 + 2 * 22**3 + 1 * 22**2 + 6 # x * 22
for x in range(0, 22):
    if (n + x * 22**5 + m + x * 22**2 + k + x * 22) % 21 == 0:
        print((n + x * 22**5 + m + x * 22**2 + k + x * 22) // 21) #162947670


#16

# import sys
# sys.setrecursionlimit(3000)
# def f(n):
#     if n < 7:
#         return 7
#     if n >= 7:
#         return n + 1 + f(n-2)
# print(f(2024)-f(2020)) #4048


#23


# def task23(start, end):
#     if start < end:
#         return 0
#     if start == 9:
#         return 0
#     if start == 16:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start-1, end) + task23(start-2, end) + task23(start//3, end)
# print(task23(19, 3)) #180