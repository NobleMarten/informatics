# f = open('9')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     if (a[0] + a[1]) == a[2]:
#         cnt += 1
# print(cnt) #15


# f = open('10')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     # (a[0] % 2 == 0 and a[1] % 2 == 0 and a[2] % 2 == 0 and a[3] % 2 == 0)
#     chet = [x for x in a if x % 2 == 0]
#     if len(chet) == 4 and (a[0]**2 > (a[1]+a[2]+a[3])):
#         cnt += 1
# print(cnt)


# f = open('11')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     chet = [x for x in a if x % 2 == 0]
#     nechet = [x for x in a if x % 2 != 0]
#     if len(set(a)) == 5 and len(chet) > len(nechet) and sum(chet) > sum(nechet):
#         cnt += 1
# print(cnt)


# f = open('12')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(ne_povt) == 4 and max(ne_povt) + min(ne_povt) <= povt[0]*2:
#         cnt += 1
# print(cnt)


# f = open('13')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(ne_povt) == 3 and len(set(povt)) == 2 and (sum(povt) / len(povt) < sum(ne_povt)/len(ne_povt)):
#         cnt += 1
# print(cnt)


# f = open('14')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(ne_povt) == 2 and len(set(povt)) == 3 and min(a) not in povt:
#         cnt += 1
# print(cnt)


# f = open('15')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     povt4 = [x for x in a if a.count(x) == 4]
#     povt2 = [x for x in a if a.count(x) == 2]
#     if (len(set(povt4)) == 1 and len(set(povt2)) == 1 and len(ne_povt) == 2 and (sum(ne_povt)/2) >= max(povt)):
#         cnt += 1
# print(cnt)


f = open('16')
cnt = 0
for s in f:
    a = sorted(list(map(int, s.split())))
    if (sum(a) - min(a))/min(a) > 5 and a[0]*a[-1] == a[1]*a[2]:
        cnt += 1
print(cnt)