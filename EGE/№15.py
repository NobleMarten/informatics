# def Del(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     A_podoshel = True
#     for x in range(1, 1000):
#         if ((Del(x, A) and Del(x, 24)) <= Del(x, 36)) == False:
#             A_podoshel = False
#             break
#     if A_podoshel:
#         print(A) #9


# def Del(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     A_podoshel = True
#     for x in range(1, 1000):
#         if ((Del(x, 64) and (not(Del(x, 24)))) <= (not(Del(x, A)))) == False:
#             A_podoshel = False
#             break
#     if A_podoshel:
#         print(A) #3


# def Del(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     A_podoshel = True
#     for x in range(1, 1000):
#         if ((not(Del(x, A))) <= (Del(x, 45) <= (not(Del(x, 75))))) == False:
#             A_podoshel = False
#             break
#     if A_podoshel:
#         print(A) #225


# 2 способ
# def Del(n, m):
#     return n % m == 0
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if (Del(A, 5) and ((not(Del(2025, A))) <= (Del(x, 1888) <= Del(2023, A)))) == False:
#             break
#     else:
#         print(A) #2025


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x & 79 != 0) <= ((x & 64 == 0) <= (x & A != 0))) == False:
#             break
#     else:
#         print(A) #15


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((x & 14 != 0) and (x & 61 != 0)) <= ((x & A != 0) and (x & 78 != 0))) == False:
#             break
#     else:
#         print(A) #14


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((x & 14 != 0) or (x & 64 != 0)) <= ((x & 23 == 0) <= (x & A != 0))) == False:
#             break
#     else:
#         print(A)
#         break #72


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x & A != 0) <= ((x & 21 == 0) <= (x & 66 != 0))) == False:
#             break
#     else:
#         print(A) #87

# 3 способ
# for A in range(1, 1000):
#     if all([(x & A != 0) <= ((x & 21 == 0) <= (x & 66 != 0)) for x in range(1, 1000)]) == True:
#         print(A) #87

# 1 способ
# for A in range(1, 1000):
#     A_podoshel = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((17*x - 3*y + 17 != 0) or (A < x) or (A < y)) == False:
#                 A_podoshel = False
#                 break
#         if A_podoshel == False:
#             break
#     if A_podoshel:
#         print(A) #16


# for A in range(1, 1000):
#     A_podoshel = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (((x >= 17) or (3*x < y)) or (y*x < A)) == False:
#                 A_podoshel = False
#                 break
#         if A_podoshel == False:
#             break
#     if A_podoshel:
#         print(A)
#         break #769

# 2 способ
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((y - 13*x < A) or (x > 88) or (y > 77)) == False:
#                 break
#         if ((y - 13 * x < A) or (x > 88) or (y > 77)) == False:
#             break
#     else:
#         print(A) #65


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (((y + 7*x != 36) or (A > x - 2)) or (A < y + 27)) == False:
#                 break
#         if (((y + 7 * x != 36) or (A > x - 2)) or (A < y + 27)) == False:
#             break
#     else:
#         print(A) #1


# 3 способ
# for A in range(1, 1000):
#     if all([((y + 7*x != 36) or (A > x -2)) or (A < y + 27) for x in range(1, 1000) for y in range(1, 1000)]) == True:
#         print(A) #1


# def Del(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((Del(64, x) <= (not(Del(128, x)))) or (A - x > 75)) == False:
#             break
#     else:
#         print(A) #140


# + способ
# def Del(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#         if all(((Del(64, x) <= (not(Del(128, x)))) or (A - x > 75)) for x in range(1, 1000)):
#             print(A) #140


# ДЗ


# def Del(n, m):
#     return n % m == 0
# for A in range(1, 100):
#     for x in range(1, 100):
#         if ((Del(x, A) and Del(x, 17)) <= Del(x, 34)) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
# for A in range(1, 100):
#     for x in range(1, 100):
#         if (Del(x, 15) <= ((not(Del(x, A))) <= (not(Del(x, 3))))) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if ((Del(x, A) and Del(x, 8)) <= ((not(Del(x, 8))) or Del(x, 240))) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x & 23 == 0) <= ((x & 13 != 0) <= (x & A != 0))) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((x & 41 != 0) and (x & 50 != 0)) <= ((x & A != 0) or (x & 76 != 0))) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x & 60 != 0) or (x & 47 == 0) or (x & A != 0)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((2*y + x != 17) or (A > 7*x) and (A > 3*y)) == False:
#                 break
#         if ((2 * y + x != 17) or (A > 7 * x) and (A > 3 * y)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((y - 2*x < A) or (x >= 25) or (y >= 40)) == False:
#                 break
#         if ((y - 2 * x < A) or (x >= 25) or (y >= 40)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((10*x - y + 37 != 0) or (A < x) or (A < y)) == False:
#                 break
#         if ((10 * x - y + 37 != 0) or (A < x) or (A < y)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (((x >= 8) or (2*x < y)) or (x*x < A)) == False:
#                 break
#         if (((x >= 8) or (2 * x < y)) or (x * x < A)) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((x + 40 < A) or (x + A < 40)) <= (Del(x, A))) == False:
#             break
#     else:
#         print(A)


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and z) or ((z <= y) <= (w <= x))
#                 if F == False:
#                     print(x, y, z, w)
# x y z w
# 0 0 0 1
# 0 1 0 1
# 0 1 1 1
# ywzx


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#                 F = (x or (not(y))) <= (y == z)
#                 if F == False:
#                     print(x, y, z)
# x y z
# 0 0 1
# 1 0 1
# 1 1 0
# zyx


# ДОП


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((A < y) or (A < x) or (x + y <= 150)) == False:
#                 break
#         if ((A < y) or (A < x) or (x + y <= 150)) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0


# p = list(range(27, 131))
# q = list(range(50, 63))
# p = list(range(38, 95))
# a = []
# for x in range(1, 1000):
#     if ((x in p) and (x not in q) and (Del(x, 3) <= Del(x, 2))) == False:
#         a.append(x)
# print(a)


for a in range(1, 10000):
    for x in range(1, 1000):
        if ((((x & 15 == 0) <= (x & 20 != 0)) <= ((x & 25 == 0) <= (x & 30 != 0))) and (x & a != 0)) == False:
            break
    else:
        print(a)  # 1023
