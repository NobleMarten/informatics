# f = open('27.1.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+1, n):
#         res.append(a[i]+a[j] + (j-i))
# print(max(res))


# f = open('27.2.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+k, n):
#         res.append(a[i]+a[j])
# print(max(res))


# f = open('27.3.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+1, n):
#         for j2 in range(j+1, n):
#             res.append(a[i]*a[j]+a[j2])
# print(max(res))


# f = open('27.4.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[i]+a[j]) % 6 == 0:
#             res.append(a[i]+a[j])
# print(len(res))


# f = open('27.5.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i+9, n):
#         if (a[i]*a[j]) % 21 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.6.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j+1]) % 101 == 0:
#             res.append([sum(a[i:j+1]), len(a[i:j+1])])
# res.sort(reverse=True)
# print(res[:3])


# f = open('27.7.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# chet_nechet = [x % 2 for x in a]
# k = 20
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(chet_nechet[i:j+1]) % k == 0:
#             res.append(sum(a[i:j+1]))
# print(max(res))


# f = open('27.8.txt')
# n, m = map(int, f.readline().split())
# a = [int(s) for s in f]
# res = []
# for i in range(m, n-m+1):
#     res.append(sum(a[i-m:i+m+1]))
# print(max(res))


from math import *
f = open('27.9.txt')
n, m = map(int, f.readline().split())
bidoni = [0]*1000
for s in f:
    km, litr = map(int, s.split())
    bidoni[km] = ceil(litr / 15)
res = []
for i in range(m, len(bidoni)):
    if bidoni[i] != 0:
        res.append(sum(bidoni[i-m:i+m+1]))
print(max(res))


f = open('27.10.txt')
n, m = map(int, f.readline().split())
mails = [int(s) for s in f]
mails += mails
res = []
for i in range(m, n+m):
    res.append(sum(mails[i-m:i+m+1]))
print(max(res))


f = open('27.11.txt')
n = int(f.readline())
mails = [int(s) for s in f]
res = []
for i in range(n):
    price = 0
    for j in range(n):
        price += abs(i-j) * mails[j]
    res.append(price)
print(max(res))


f = open('27.12.txt')
n = int(f.readline())
trash = [int(s) for s in f]
res = []
for i in range(n):
    price = 0
    for j in range(n):
        price += trash[j] * min(abs(i-j), n - abs((i-j)))
    res.append([price, i])
print(min(res))