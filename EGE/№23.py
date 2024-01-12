# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start + 1, end) + task23(start*2, end)
# print(task23(1, 14)) #26


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start + 1, end) + task23(start*3, end)
# print(task23(2, 56)) #54


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start*3, end) + task23(start**2, end)
# print(task23(4, 93))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == 27:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*2, end)
# print(task23(3,15) * task23(15, 72))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == 44:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*3, end)
# print(task23(2,24) * task23(24,144))


# def task23(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start -1 , end) + task23(start // 3, end)
# print(task23(49,11) * task23(11, 1))


# def task23(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start-2, end) + task23(start//2, end) + task23(start//3, end)
# print()


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start+10, end)
# print(task23(2,45))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*2, end) + task23(start*2+1, end)
# print(task23(3, 90))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(int(str(start) + '1'), end) #start * 10 + 1
# print(task23(1,928))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(int('1' + bin(start)[2:], 2), end)
# print(task23(1, int('1111111', 2)))

# print('1' + bin(4)[2:]) перевод в двоичную запись; bin возвращает строчку


# def task23(start, end, cnt):
#     if start > end or cnt > 1:
#         return 0
#     if start == end and cnt == 1:
#         return 1
#     return task23(start+1, end, cnt+0) + task23(start+2, end, cnt+0) \
#         + task23(start*2, end, cnt+1) + task23(start*3, end, cnt+1)
# print(task23(1, 13, 0)) #411


# def task23(start, end, commandi):
#     if start > end or '***' in commandi or '+++' in commandi:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end, commandi + '+') + task23(start*2, end, commandi + '*')
# print(task23(1, 18, '')) #5



#ДЗ



#def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start + 2, end) + task23(start*2, end)
# print(task23(1, 25))


# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     if x < y:
#         return f(x+1, y) + f(x*4, y)
# print(f(2, 55))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start*2, end) + task23(start**2, end)
# print(task23(3, 27))

# def task23(start, end):
#     if start > end:
#         return 0
#     if start == 26:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*2, end)
# print(task23(2, 14) * task23(14, 56))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == 20:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2, end) + task23(start*3, end)
# print(task23(2, 24) * task23(24, 100))


# def task23(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start-1, end) + task23(start//2, end)
# print(task23(156, 63) * task23(63, 3))

# def task23(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#     if start > end:
#         return task23(start-1, end) + task23(start//2, end) + task23(start//3, end)
# print(task23(131, 41) * task23(41, 3))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start+10, end)
# print(task23(3, 35))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start*2, end) + task23(start*2+1, end)
# print(task23(2, 16))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(int(str(start) + '1'), end)
# print(task23(1, 875))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(int('1' + bin(start)[2:], 2), end)
# print(task23(1, int('1111011', 2)))


# def task23(start, end):
#     if start > end:
#         return 0
#     if start == 5:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end) + task23(start*3, end)
# print(task23(1, 21)) #писал для проверки решения руками


# def task23(start, end, cnt):
#     if start > end or cnt > 2:
#         return 0
#     if start == end and cnt == 2:
#         return 1
#     return task23(start+2, end, cnt+0) + task23(start+3, end, cnt+0) \
#         + task23(start*2, end, cnt+1) + task23(start*3, end, cnt+1)
# print(task23(1, 51, 0))


# def task23(start, end, commandi):
#     if start > end or '****' in commandi or '++++' in commandi:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+1, end, commandi + '+') + task23(start*3, end, commandi + '*')
# print(task23(1, 30, ''))


