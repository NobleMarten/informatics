# f = open('26.1.txt')
# n = f.readline()
# data = [list(map(int, s.split())) for s in f]
# data.sort()
# for i in range(1, len(data)):
#     if (data[i][0] == data[i-1][0]) and (data[i][1] - data[i-1][1] == 3):
#         print(data[i], data[i-1])
# #3 252


# f = open('26.2.txt')
# n, k = map(int, f.readline().split())
# data = [list(map(int, s.split())) for s in f]
# data.sort()
# for i in range(1, n):
#     if (data[i][0] == data[i-1][0]) and (data[i][1] - data[i-1][1] == k+1):
#         print(data[i], data[i-1])
# #983 192


f = open('26.2.txt')
n, k = map(int, f.readline().split())
data = []
for s in f:
    r, m = map(int, s.split())
    if [r, m] not in data:
        data.append([r, m])
data.sort()

cur = 1
for i in range(1, len(data)):
    if data[i][0] == data[i-1][0] and (data[i][1] - data[i-1][1] == 1):
        cur += 1
        print(cur, data[i], data[i-1])
    else:
        cur = 1

