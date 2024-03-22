# f = open('27.1.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[i]+a[j]) % 12 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.2.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i+9, n):
#         if (a[i]*a[j]) % 22 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.3.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i+9, n):
#         if (a[i]+a[j]) % 10 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.4.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j+1]) % 71 == 0:
#             res.append([sum(a[i:j+1]), (j+1) - i])
# res.sort(reverse=True)
# print(res[:5])


# f = open('27.5.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# cnt_chet = [int(x % 2 == 0) for x in a]
# for i in range(n):
#     for j in range(i, n):
#         if sum(cnt_chet[i:j+1]) % 22 == 0:
#             res.append(sum(a[i:j+1]))
# print(max(res))


# f = open('27.6.txt')
# n, m = map(int, f.readline().split())
# a = [int(s) for s in f]
# res = []
# for i in range(m, n-m):
#     res.append(sum(a[i-m:i+m+1]))
# print(max(res))


f = open('27.7.txt')
n = int(f.readline())
a = [int(s) for s in f]
res = []
for i in range(n):
    cost = 0
    for j in range(n):
        cost += abs(j-i)*a[j]
    res.append(cost)
print(max(res))