# f = open('27.1.A.txt')
# n = int(f.readline())
# min_sum = 0
# for s in f:
#     a, b = map(int, s.split())
#     min_sum += min(a, b)
# print(min_sum, min_sum % 75)


# f = open('27.1.B.txt')
# n = int(f.readline())
# min_sum = 0
# min_razn = 10000
# for s in f:
#     a, b = map(int, s.split())
#     min_sum += min(a, b)
# print(min_sum, min_sum % 75)



# f = open('27.B.3.txt')
# n = int(f.readline())
# max_sum = 0
# min_razn = 100000
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort(reverse=True)
#     max_sum += (a[0]+a[1])
# print(max_sum, max_sum % 56)



# f = open('27.B.4.txt')
# n = int(f.readline())
# min_sum = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     min_sum += (a[0]+a[1])
# print(min_sum, min_sum % 65)



f = open('27_02_B.txt')
n = int(f.readline())
min_sum = 0
for s in f:
    a, b = map(int, s.split())
    min_sum += min(a, b)
print(min_sum, min_sum % 5, min_sum % 7)