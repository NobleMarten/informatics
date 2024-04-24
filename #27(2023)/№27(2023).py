# f = open('27.1.A (10).txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = []
# for i in range(n):
#     for j in range(i + k, n):
#         pari.append(a[i]+a[j])
# print(max(pari))


# f = open('27.1.B (4).txt')
# # f = open('27.1.A (10).txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# max1 = 0
# max_sum = 0
# for i in range(k, n):
#     max1 = max(max1, a[i-k])
#     max_sum = max(max_sum, a[i] + max1)
# print(max_sum)



# f = open('27.2.A (7).txt')
# n = int(f.readline())
# k = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+k, n):
#         for j2 in range(j+k, n):
#             res.append(a[i]+a[j]+a[j2])
# print(max(res))


# f = open('27.2.B (5).txt')
# n = int(f.readline())
# k = int(f.readline())
# a = [int(s) for s in f]
# max1, max2, max_sum = 0, 0, 0
# for i in range(2*k, n):
#     max1 = max(max1, a[i-k-k])
#     max2 = max(max2, a[i-k] + max1)
#     max_sum = max(max_sum, a[i] + max2)
# print(max_sum)



f = open('27.3.A (7).txt')
n = int(f.readline())
a = [int(s) for s in f]
res = []
for i in range(n):
    for j in range(i+1, n):
        res.append(a[i]+a[j] + (j-i))
print(max(res))


f = open('27.3.B (5).txt')
n = int(f.readline())
a = [int(s) for s in f]
max1 = 0
max_sum = 0
for i in range(1, n):
    max1 = max(max1, a[i-1]-(i-1))
    max_sum = max(max_sum, a[i] + i + max1)
print(max_sum)