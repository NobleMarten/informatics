# a = [2, 5, 19, 54, 4]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         print(a[i], a[j])


# f = open('27.1.A.txt')
# n = int(f.readline())
# a = []
# for s in f:
#     a.append(int(s))
# cnt = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i]+a[j]) % 6 == 0:
#             cnt += 1
# print(cnt) #83591


# f = open('27.2.A.txt')
# n = int(f.readline())
# a = []
# for s in f:
#     a.append(int(s))
# cnt = 0
# for i in range(len(a)):
#     for j in range(i+9, len(a)):
#         if (a[i] * a[j]) % 15 == 0:
#             cnt += 1
# print(cnt) #99899


# f = open('27.3.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(len(a)):
#     for j in range(i+9, len(a)):
#         if (a[i] + a[j]) % 24 == 0:
#             cnt += 1
# print(cnt) #20575


# f = open('27.4.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         pari.append(a[i] + a[j] + (j-i))
# print(max(pari)) #2891


# f = open('27.3.A (1).txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = [] #сумма пар
# for i in range(len(a)):
#     for j in range(i+k, len(a)):
#         pari.append(a[i]+a[j])
# print(max(pari)) #1994


# f = open('27.6.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# troyki = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         for y in range(j+1, len(a)):
#             troyki.append(a[i]*a[j]*a[y])
# print(max(troyki)) #998500140000


# f = open('27.7.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# podposl = []
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if sum(a[i:j+1]) % 101 == 0:
#             podposl.append([sum(a[i:j+1]), (j+1)-i])
# podposl.sort(reverse=True)
# print(podposl[:5]) #992


# def cnt_nechet(a):
#     cnt = 0
#     for x in a:
#         # cnt += (x%2) #можно так
#         if x % 2 != 0:
#             cnt += 1
#     return cnt
# f = open('27.8.A.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# podposl = []
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if cnt_nechet(a[i:j+1]) % 20 == 0:
#             podposl.append(sum(a[i:j+1]))
# print(max(podposl)) #4754298




#ДЗ




# f = open('27-3-A_lzymlw8.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#        if (a[i]+a[j]) % 6 == 0:
#            cnt += 1
# print(cnt)


# f = open('27-3-A_AY47Dff.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(len(a)):
#     for j in range(i+9, len(a)):
#         if (a[i] * a[j]) % 15 == 0:
#             cnt += 1
# print(cnt)


# f = open('27.1.A (1).txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# pari = []
# for i in range(len(a)):
#     for j in range(i+k, len(a)):
#         pari.append(a[i]+a[j])
# print(max(pari))


# f = open('27_1428Udh.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# troiki = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         for t in range(j+1, len(a)):
#             troiki.append(a[i]*a[j]*a[t])
# print(max(troiki))


# f = open('27.1.A_BlQdp91.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# podposl = []
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if sum(a[i:j+1]) % 51 == 0:
#             podposl.append([sum(a[i:j+1]), (j+1)-i])
# podposl.sort(reverse=True)
# print(podposl[:5])


# def cnt_chet(a):
#     cnt = 0
#     for x in a:
#         if x % 2 == 0:
#             cnt += 1
#     return cnt
# f = open('27.3.A_WIueE2u.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# podposl = []
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if cnt_chet(a[i:j+1]) % 17 == 0:
#             podposl.append(sum(a[i:j+1]))
# print(max(podposl))



# q = list(range(11, 65))
# p = list(range(4, 33))
# A = []
# for x in range(1, 1000):
#     if ((x in A) or ((not(x in p)) <= (not(x in q)))) == False:
#         A.append(x)
# print(A)