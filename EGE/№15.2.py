# Задачи на отрезки

# p = list(range(3, 19))
# q = list(range(11, 25))
# A = []
# for x in range(1, 100):
#     if (((x in p) and (x in q)) <= (x in A)) == False:
#         A.append(x)
# print(A) #7


# p = list(range(16, 60))
# q = list(range(27, 72))
# A = []
# for x in range(1, 100):
#     if ((not(x in A)) <= ((x in p) <= (not(x in q)))) == False:
#         A.append(x)
# print(A) #32


# p = list(range(13, 34))
# q = list(range(22, 45))
# A = []
# for x in range(1, 100):
#     if ((not(x in A)) <= (((x in p) and (x in q)) <= (x in A))) == False:
#         A.append(x)
# print(A) #11


# p = list(range(11, 29))
# q = list(range(21, 43))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in p) <= (x in q)) <= (not(x in A))) == False:
#         A.remove(x)
# print(A) #10


# p = list(range(13, 33))
# q = list(range(15, 21))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in A) <= (x in p)) or (x in q)) == False:
#         A.remove(x)
# print(A) #19


# p = list(range(11, 29))
# q = list(range(21, 43))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in p) == (x in q)) <= ((not(x in A)))) == False:
#         A.remove(x)
# print(A) #14


# p = list(range(26, 55))
# q = list(range(19, 75))
# A = []
# for x in range(1, 100):
#     if (((x in q) <= (x in p)) or (x in A)) == False:
#         A.append(x)
# print(A) #55
# # [19 26] и [54 74]  [19, 74]



# r = list(range(16, 35))
# p = list(range(19, 27))
# q = list(range(4, 18))
# A = []
# for x in range(1, 100):
#     if (((x in A) or (x in p)) or ((x in q) <= (x in r))) == False:
#         A.append(x)
# print(A) #12


# q = [i / 10 for i in range(180, 421)]
# p = [i / 10 for i in range(100, 211)]
# A = [i / 10 for i in range(10, 1000)]
# for x in range(10, 1000):
#     if (((x/10 in q) <= (x/10 in p)) <= (not(x/10 in A))) == False:
#         A.remove(x/10)
# print(max(A) - min(A)) #21.1 - 42.0 (21,42] #21


# q = [i / 10 for i in range(400, 801)]
# p = [i / 10 for i in range(200, 601)]
# A = [i / 10 for i in range(10, 1001)]
# for x in range(10, 1001):
#     x0 = x / 10
#     if (((x0 in p) <= (not(x0 in q))) <= (not(x0 in A))) == False:
#         A.remove(x0)
# print(max(A) - min(A)) #20


# q = [i / 10 for i in range(100, 301)]
# p = [i / 10 for i in range(50, 151)]
# A = [i / 10 for i in range(10, 1001)]
# for x in range(10, 1001):
#     x0 = x / 10
#     if (((x0 in A) <= (x0 in p)) or (x0 in q)) == False:
#         A.remove(x0)
# print(A) #25



# def Del(n, m):
#     return n % m == 0
# D = list(range(30, 46))
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((not(Del(x, 7))) and (x not in {52, 60, 68}))
#             <= ((abs(x - 25) <= 10) <= (x in D)) or (x & A != 0)) == False:
#             break
#     else:
#         print(A) #17


# def Del(n, m):
#     return n % m == 0
# p = list(range(25, 56))
# q = list(range(13, 31))
# A = []
# for x in range(1, 1000):
#     if ((((x in p) <= (Del(x, 14)) or (x in q))) <= (x in A)) == True:
#         A.append(x)
# print(A) #25


# def Del(n, m):
#     return n % m == 0
# p = list(range(26, 53))
# A = []
# for x in range(1, 100):
#     if ((x in p) <= ((Del(x, 14) <= (x in A)))) == False:
#         A.append(x)
# print(A) #14


# q = list(range(39, 72))
# p = list(range(15, 100))
# A = []
# for x in range(1, 1000):
#     if ((x in p) <= (((x in q) and (x in p)) or ((not(x in q)) <= (x in A)))) == False:
#         A.append(x)
# print(A) #84 #разрыв не влияет, потому что все эти числа должны войти



# ДЗ

# q = list(range(42, 103))
# p = list(range(22, 73))
# A = []
# for x in range(1, 100):
#     if ((not((not(x in A)) and (x in p))) or (x in q)) == False:
#         A.append(x)
# print(A) #20


# q = list(range(32, 93))
# p = list(range(12, 62))
# A = []
# for x in range(1, 100):
#     if ((not(x in A) and (x in q)) <= (x in p)) == False:
#         A.append(x)
# print(A) #30


# p = list(range(15, 31))
# q = list(range(8, 26))
# A = []
# for x in range(1, 100):
#     if (((x in p) and (x in q)) <= (x in A)) == False:
#         A.append(x)
# print(A) #10


# q = list(range(21, 59))
# p = list(range(1, 40))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in q) <= (not(x in p))) <= (not(x in A))) == False:
#         A.remove(x)
# print(A)


# q = list(range(8, 18))
# p = list(range(3, 12))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in A) <= (x in p)) or (x in q)) == False:
#         A.remove(x)
# print(A)


# q = list(range(15, 40))
# p = list(range(10, 18))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in q) <= (x in p)) <= (not(x in A))) == False:
#         A.remove(x)
# print(A)


# p = list(range(25, 121))
# q = list(range(54, 76))
# A = []
# for x in range(1, 1000):
#     if ((x in q) <= (((x in p) == (x in q)) or ((not(x in p)) <= (x in A)))) == False:
#         A.append(x)
# print(A)


# q = list(range(12, 69))
# p = list(range(10, 58))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in q) <= (x in p)) <= (not(x in A))) == False:
#         A.remove(x)
# print(A)


# def Del(n, m):
#     return n % m == 0
# p = list(range(13, 38))
# q = list(range(22, 51))
# A = []
# for x in range(1, 100):
#     if (((x in q) <= (Del(x, 18) or (x in p))) <= (x in A)) == True:
#         A.append(x)
# print((A))


# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((9*x + y < A) or (x + 14*y > 49) or (x + y < 25)) == False:
#                 break
#         if ((9 * x + y < A) or (x + 14 * y > 49) or (x + y < 25)) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
# B = list(range(100, 121))
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((x in B) <= ((Del(x, 35) == Del(x, A)) or Del(x, A))) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
# B = list(range(45, 91))
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (Del(x, 52) and (not((not(x in B)) or Del(x, A)))) == True:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         if ((Del(x, A) and Del(x, 42)) <= ((Del(x, 8)) and Del(x, 150))) == False:
#             break
#     else:
#         print(A)
