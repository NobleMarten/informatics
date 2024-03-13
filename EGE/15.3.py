# p = list(range(11, 29))
# q = list(range(21, 43))
# a = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in p) == (x in q)) <= (not(x in a))) == False:
#         a.remove(x) #когда просят наибольшую длину
# print(a)
# 11 - 20 11-21
# 29 - 42 28-42
# ответ 14


# r = list(range(16, 35))
# p = list(range(19, 27))
# q = list(range(4, 18))
# a = []
# for x in range(1, 100):
#     if (((x in a) or (x in p)) or ((x in q) <= (x in r))) == False:
#         a.append(x) #когда просят наименьшую длину
# print(a) #12


# q = list(range(18, 43))
# p = list(range(10, 22))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in q) <= (x in p)) <= (not(x in A))) == False:
#         A.remove(x)
# print(A)
# 21-42  21


# q = list(range(40, 81))
# p = list(range(20, 61))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in p) <= (not(x in q))) <= (not(x in A))) == False:
#         A.remove(x)
# print(A) #20


# q = list(range(10, 31))
# p = list(range(5, 16))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in A) <= (x in p)) or (x in q)) == False:
#         A.remove(x)
# print(A) #25


# q = [i/10 for i in range(100, 201)]
# p = [i/10 for i in range(250, 301)]
# A = []
# for x in range(1*10, 100*10+1):
#     x0 = x / 10
#     if ((not(((x0 in q) or (x0 in p)) <= (x0 in A)))) == True:
#         A.append(x0)
# print(A) #20


# def dell(n, m):
#     return n % m == 0
# p = list(range(25, 56))
# q = list(range(13, 31))
# A = []
# for x in range(1, 100):
#     if (((x in p) <= (dell(x, 14) or (x in q))) <= (x in A)) == True:
#         A.append(x)
# print(A) #25


# def dell(n, m):
#     return n % m == 0
# d = list(range(30, 46))
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (((not(dell(x, 7))) and (x in [52, 60, 68])) <= (((abs(x-25) <= 10) <= (x in d)) or (x & A != 0))) == False:
#             break
#         else:
#             print(A)