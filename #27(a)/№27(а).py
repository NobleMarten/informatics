# f = open('27.1.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if (a[i]+a[j]) % 6 == 0:
#             cnt += 1
# print(cnt) #83256


# f = open('27.2.txt')
# cnt = 0
# n = int(f.readline())
# a = [int(s) for s in f]
# for i in range(n):
#     for j in range(i+9, n):
#         if (a[i]*a[j]) % 21 == 0:
#             cnt += 1
# print(cnt) #65954


# f = open('27.3.txt')
# cnt = 0
# n = int(f.readline())
# a = [int(s) for s in f]
# for i in range(n):
#     for j in range(i+9, n):
#         if (a[i]+a[j]) % 24 == 0:
#             cnt += 1
# print(cnt) #20240


# f = open('27.4.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j+1]) % 101 == 0:
#             res.append([sum(a[i:j+1]), (j+1) - i])
# res.sort(reverse=True)
# print(res[:5])



# def cnt_nechet(a):
#     return sum([1 for x in a if x % 2 != 0])
#     # cnt = 0
#     # for x in a:
#     #     if x % 2 != 0:
#     #         cnt += 1
#     # return cnt

# f = open('27.5.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt_nechet = [int(x % 2 != 0) for x in a]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         # if cnt_nechet(a[i:j+1]) % 20 == 0:
#         if sum(cnt_nechet[i : j+1]) % 20 == 0:
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