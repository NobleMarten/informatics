# f = open('27.1.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[i]+a[j]) % 6 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.2.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i+9, n):
#         if (a[i]*a[j]) % 15 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.3.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+k, n):
#         res.append(a[i]+a[j])
# print(max(res))


# f = open('27.4.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# print(a[:3], a[-3:])
# print(-99972 * -99698 * 99755)
# print(99755 * 99750 * 99416)


# f = open('27.5.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j+1]) % 51 == 0:
#             res.append([sum(a[i:j+1]), (j+1)-i])
# res.sort(reverse=True)
# print(res[:5])


f = open('27.6.txt')
n = int(f.readline())
a = [int(s) for s in f]
res = []
cnt_chet = [int(x % 2 == 0) for x in a]
for i in range(n):
    for j in range(i, n):
        if sum(cnt_chet[i:j+1]) % 17 == 0:
            res.append(sum(a[i:j+1]))
print(max(res))