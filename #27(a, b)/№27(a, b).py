# f = open('27.1.A.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i + k, n):
#         for j2 in range(j + k, n):
#             res.append(a[i]+a[j]+a[j2])
# print(max(res)) #2970343


# f = open('27.1.B.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# max_1, max_2, max_3 = 0, 0, 0
# for i in range(2*k, n):
#     max_1 = max(max_1, a[i-k-k])
#     max_2 = max(max_2, a[i-k] + max_1)
#     max_3 = max(max_3, a[i] + max_2)
# print(max_3) #2999985


# f = open('27.2.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# # res = []
# # for i in range(n):
# #     for j in range(i+1, n):
# #         for j2 in range(j+1, n):
# #             res.append(a[i]*a[j]*a[j2])
# # print(max(res))
# a.sort()
# print(a[:3], a[-3:])


# f = open('27.3.A.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i+1, n):
#         for j2 in range(j+1, n):
#             if (j-i) == 2*k or (j2-i) == 2*k or (j2-j) == 2*k:
#                 res.append(a[i]+a[j]+a[j2])
# print(max(res)) #2927586


f = open('27.3.B.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(s) for s in f]
max2 = 0
for i in range(n):
    if a[i - 2*k] + a[i] > max2:
        max2 = a[i - 2*k] + a[i]
        print(a[i - 2*k], a[i])
print(max2 + max(a))
print(max(a)) #2996532