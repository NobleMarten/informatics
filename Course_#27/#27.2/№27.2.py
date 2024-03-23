# f = open('27.1.A.txt')
# n = int(f.readline())
# max_sum = 0
# for s in f:
#     a, b = map(int, s.split())
#     max_sum += max(a, b)
# print(max_sum, max_sum % 6) #6735507


# f = open('27.1.B.txt')
# n = int(f.readline())
# max_sum = 0
# min_razn = 100000
# for s in f:
#     a, b = map(int, s.split())
#     max_sum += max(a, b)
#     if abs(a-b) != 0:
#         min_razn = min(min_razn, abs(a-b))
# print(max_sum - min_razn, max_sum % 6) #6670074131





# f = open('27.2.A.txt')
# n = int(f.readline())
# min_sum = 0
# for s in f:
#     a, b = map(int, s.split())
#     min_sum += min(a, b)
# print(min_sum, min_sum % 34) #3337425


# f = open('27.2.B.txt')
# n = int(f.readline())
# min_sum = 0
# min_razn = 1000000
# for s in f:
#     a, b = map(int, s.split())
#     if abs(a-b) != 0:
#         min_razn = min(min_razn, abs(a-b))
#     min_sum += min(a, b)
# print(min_sum + min_razn, min_sum % 34) #3332707031




# f = open('27.3.A.txt')
# n = int(f.readline())
# min_sum = 0
# for s in f:
#     a = sorted(list(map(int, s.split())))
#     min_sum += (a[0] + a[1])
# print(min_sum, min_sum % 65) #7523683


# f = open('27.3.B.txt')
# n = int(f.readline())
# min_sum = 0
# min_razn = 100000
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     min_sum += (a[0] + a[1])
#     if abs(a[1]-a[2]) % 65 != 0:
#         min_razn = min(min_razn, abs(a[1]-a[2]))
#     if abs(a[0]-a[2]) % 65 != 0:
#         min_razn = min(min_razn, abs(a[0]-a[2]))
# print(min_sum + min_razn, min_sum % 65) #7507356936
# print(min_razn)




# f = open('27.4.B.txt')
# n = int(f.readline())
# max_sum = 0
# min_razn = 100000
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort(reverse=True)
#     if (a[0]-a[1]) % 24 != 0:
#         min_razn = min(min_razn, a[0]-a[1])
#     if (a[0]-a[2]) % 24 != 0:
#         min_razn = min(min_razn,  a[0]-a[2])
#     max_sum += max(a)
# print(max_sum - min_razn, max_sum % 24) #7498482505
# print(min_razn)




f = open('27.5.A.txt')
n = int(f.readline())
min_sum = 0
for s in f:
    a, b = map(int, s.split())
    min_sum += min(a, b)
print(min_sum, min_sum % 9, min_sum % 11) #3205087


f = open('27.5.B.txt')
n = int(f.readline())
min_sum = 0
min_razn = []
for s in f:
    a, b = map(int, s.split())
    min_sum += min(a, b)
    if abs(a - b) != 0:
        min_razn.append(abs(a-b))
print(min_sum + min(min_razn), min_sum % 9, min_sum % 11) #3205087
print(min(min_razn))