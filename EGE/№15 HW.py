# def dell(n, m):
#     return n % m == 0
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if ((dell(x, A) and dell(x, 8)) <= ((not(dell(x, 8))) or dell(x, 513))) == False:
#             break
#     else:
#         print(A)


# def dell(n, m):
#     return n % m == 0
# for A in range(1, 100000):
#     for x in range(1, 100000):
#         if (((dell(x, 24) and dell(x, 36)) <= dell(x, A)) and (A*A - A - 5000 < 112)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if ((x & 75 == 0) or ((x & 80 == 0) <= (x & A != 0))) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if (((x & 56 != 0) or (x & 17 != 0)) <= ((x & 15 == 0) <= (x & A != 0))) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((x > 15) or (y < x) or (x*x*2 < A)) == False:
#                 break
#         if ((x > 15) or (y < x) or (x * x * 2 < A)) == False:
#             break
#     else:
#         print(A)
#         break


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((x + 2*y > A) or (x <= 15) or (y <= 30)) == False:
#                 break
#         if ((x + 2 * y > A) or (x <= 15) or (y <= 30)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((10*y - x + 31 != 0) or (A < x) or (A < y)) == False:
#                 break
#         if ((10 * y - x + 31 != 0) or (A < x) or (A < y)) == False:
#             break
#     else:
#         print(A)


# cnt = 0
# for A in range(0, 1000):
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if (((x > 10) <= (x*y + 11*x >= A)) and ((y*x + y > A) <= (y >= 1))) == False:
#                 break
#         if (((x > 10) <= (x * y + 11 * x >= A)) and ((y * x + y > A) <= (y >= 1))) == False:
#             break
#     else:
#         cnt += 1
# print(cnt)


# def dell(n, m):
#     return n % m == 0
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if ((dell(x, A) and dell(x, 7)) <= ((not(dell(x, 7))) or (dell(x, 311)))) == False:
#             break
#     else:
#         print(A)


# def dell(n, m):
#     return n % m == 0
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if (((x + 40 < A) or (x + A < 40)) <= (dell(x, A))) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((x*x - 11*x + 28 > 0) or (y*y - 9*y + 14 > 0) or (x*x + y*y > A)) == False:
#                 break
#         if ((x * x - 11 * x + 28 > 0) or (y * y - 9 * y + 14 > 0) or (x * x + y * y > A)) == False:
#             break
#     else:
#         print(A)


# def Treug(a, b, c):
#     return (a+b > c) and (a+c > b) and (b+c > a)
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((not(((Treug(x, 11, 24) == ((not(max(x, 7) > 32)))) and (Treug(x, A, 7)))))) == False:
#             break
#     else:
#         print(A)


# def ugol(a, b, c):
#     return (a + b + c) == 180
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (ugol(47, A, x+40) == (ugol(A, x, 45) and (not(A + 30 < 156)))) == False:
#             break
#     else:
#         print(A)


# def dell(n, m):
#     return n % m == 0
# for A in range(1, 10000000):
#     for x in range(1, 10000000):
#         if ((dell(x, A) and (not(dell(x, 11074)))) <= ((not(dell(x, 2369))) and dell(x, 193123))) == False:
#             break
#     else:
#         print(A)
#         break


for A in range(1, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((x * y != A) or (x > 81) or (y < 35)) and (abs(x + y - A) > x + y + A)) == False:
                break
        if (((x * y != A) or (x > 81) or (y < 35)) and (abs(x + y - A) > x + y + A)) == False:
            break
    else:
        print(A)