# q = list(range(20, 41))
# p = list(range(10, 26))
# A = []
# for x in range(1, 100):
#     if (((x in p) and (not(x in q))) <= (x in A)) == False:
#         A.append(x)
# print(A)


# q = list(range(25, 41))
# p = list(range(8, 17))
# A = []
# for x in range(1, 100):
#     if (((x in p) or (x in q)) <= (x in A)) == False:
#         A.append(x)
# print(A)


# p = list(range(7, 16))
# q = list(range(20, 38))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((not(x in p)) <= (x in q)) or (not(x in A))) == False:
#         A.remove(x)
# print(A)


# q = list(range(15, 41))
# p = list(range(5, 26))
# A = []
# for x in range(1, 100):
#     if (((x in p) and (not(x in q))) <= (x in A)) == False:
#         A.append(x)
# print(A)


# q = list(range(8, 31))
# p = list(range(12, 24))
# A = []
# for x in range(1, 100):
#     if (((x in p) and (x in q)) <= (x in A)) == False:
#         A.append(x)
# print(A)


# p = list(range(2, 21, 2))
# q = list(range(3, 31, 3))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in A) <= (not(x in p))) and ((not(x in q)) <= (not(x in A)))) == False:
#         A.remove(x)
# print(A)


# def dell(n, m):
#     return n % m == 0
#
# p = list(range(13, 38))
# q = list(range(22, 52))
# A = []
# for x in range(1, 100):
#     if (((x in q) <= (dell(x, 18) or (x in p))) <= (x in A)) == True:
#         A.append(x)
# print(A)


# d = list(range(28, 70))
# c = list(range(40, 92))
# A = []
# for x in range(1, 100):
#     if ((x in d) <= (((not(x in c)) and (not(x in A))) <= (not(x in d)))) == False:
#         A.append(x)
# print(A)
# print(40-28)


V = list(range(14, 6411))
I = list(range(16, 6410))
K = list(range(15, 6412))
A = []
for y in range(1, 10000):
    if (((y**5 in V) <= (y in I)) <= ((y in K) <= (y in A))) == False:
        A.append(y)
print(A)