# f = open('26.1 (1).txt')
# n = int(f.readline())
# minutes = [0]*1441
# for s in f:
#     start, end = map(int, s.split())
#     for t in range(start, end):
#         minutes[t] += 1
# print(minutes)
# print(max(minutes))
# piki = []
# for t in range(1441):
#     if minutes[t] == 5062:
#         piki.append(t)
# print(piki) #5067 2


# f = open('26.2 (3).txt')
# n = int(f.readline())
# sec = [0]*(86400)
# for s in f:
#     start, end = map(int, s.split())
#     for t in range(start, end):
#         sec[t] += 1
# print(max(sec[8*60*60:14*60*60+1]))
# print(sec[8*60*60:14*60*60+1].count(4951))


# f = open('26.3 (3).txt')
# n = int(f.readline())
# minutes = [0]*1440
# for s in f:
#     start, end = map(int, s.split())
#     for t in range(start, end):
#         minutes[t] += 1
# cur = 1
# max_len = 1
# for t in range(len(minutes)-1):
#     if minutes[t] == minutes[t+1]:
#         cur += 1
#     else:
#         cur = 1
#     max_len = max(max_len, cur)
# print(max_len)
#
# print(max(minutes))
# print(minutes.count(508)) # 7 4
# # 508 покупателя
# # 4 минуты по 508


# f = open('26.4 (3).txt')
# n = int(f.readline())
# izmenenia = [0]*1000001
# for s in f:
#     start, end = map(int, s.split())
#     izmenenia[start] += 1
#     izmenenia[end] -= 1
# minutes = [0]*1000001
# cur = 0
# for t in range(len(minutes)):
#     cur += izmenenia[t]
#     minutes[t] = cur
# print(max(minutes)) #5094
# print(sum([1 for t in minutes if t >= 1]))



f = open('26.2 (3).txt')
n = int(f.readline())
izmenenia = [0]*(86401)
for s in f:
    start, end = map(int, s.split())
    izmenenia[start] += 1
    izmenenia[end] -= 1
sec = [0]*(86401)
cur = 0
for t in range(len(sec)):
    cur += izmenenia[t]
    sec[t] = cur
print(max(sec[8*60*60:14*60*60+1]))
print(sec[8*60*60:14*60*60+1].count((max(sec[8*60*60:14*60*60+1]))))