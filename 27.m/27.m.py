# f = open('27.1.A.txt')
# n, m = map(int, f.readline().split())
# foods = [int(s) for s in f]
# res = []
# for i in range(m, n - m + 1):
#     res.append(sum(foods[i-m: i+m+1]))
# print(max(res))


# f = open('27.1.B.txt')
# n, m = map(int, f.readline().split())
# foods = [int(s) for s in f]
# ans = sum(foods[0:m+m+1])  # m-m:m+m+1
# res = [ans]
# for i in range(m + 1, n - m):
#     res.append(res[-1] - foods[i - m - 1] + foods[i + m])
# print(max(res))


# f = open('27.2.A.txt')
# n, m = map(int, f.readline().split())
# milk = [0]*10000
# for s in f:
#     km, litr = map(int, s.split())
#     if litr % 15 == 0:
#         milk[km] = litr // 15
#     else:
#         milk[km] = litr // 15 + 1
#     # milk[km] = litr // 15 + bool(litr % 15)
# res = []
# for i in range(m, len(milk) - m):
#     if milk[i] != 0:
#         res.append(sum(milk[i - m: i + m + 1]))
# print(max(res))


f = open('27.2.B.txt')
n, m = map(int, f.readline().split())
milk = [0]*1000000
for s in f:
    km, litr = map(int, s.split())
    milk[km] = litr // 15 + bool(litr % 15)
cur = sum(milk[0:m+m+1])
res = []
if milk[m] != 0:
    res.append(cur)
for i in range(m+1, len(milk) - m):
    cur = cur - milk[i - m - 1] + milk[i + m]
    if milk[i] != 0:
        res.append(cur)
print(max(res))
