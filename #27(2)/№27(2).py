# f = open('27.1.A (2).txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         pari.append((a[i]+a[j]))
# print(max(pari))
# a.sort(reverse=True)
# print(sum(a[:2])) #19919


# f = open('27.2.B.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# mx_sum = 0
# mx_elem = 0
# for i in range(1, n):
#     mx_elem = max(mx_elem, a[i-1] - (i-1))
#     mx_sum = max(mx_sum, mx_elem + a[i] + 1)
# print(mx_sum)


# f = open('27.4.B.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# kr33, kr11, kr3 = [], [], []
# for x in a:
#     if x % 33 == 0:
#         kr33.append(x)
#     elif x % 3 == 0:
#         kr3.append(x)
#     elif x % 11 == 0:
#         kr11.append(x)
# kr3.sort(reverse=True)
# kr33.sort(reverse=True)
# kr11.sort(reverse=True)
# a.sort(reverse=True)
# print(kr3[:2], kr11[:2], kr33[:2], a[:2])
# print(9999*10000)
# print(9996*9988)
# # 99990000


f = open('27.5.B.txt')
n = int(f.readline())
a = [int(s) for s in f]
kr21, kr3, kr7, nekr = 0, 0, 0, 0
cnt = 0
for i in range(1, n):
    if a[i - 1] % 21 == 0:
        kr21 += 1
    elif a[i - 1] % 3 == 0:
        kr3 += 1
    elif a[i - 1] % 7 == 0:
        kr7 += 1
    else:
        nekr += 1

    if a[i] % 21 == 0:
        cnt += kr21 + kr3 + kr7 + nekr
    elif a[i] % 7 == 0:
        cnt += kr21 + kr3
    elif a[i] % 3 == 0:
        cnt += kr21 + kr7
    else:
        cnt += kr21
print(cnt) #73388312645