# f = open('1')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     if a[0] + a[1] == a[2]:
#         cnt += 1
# print(cnt)


# f = open('2')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     chet = [x for x in a if x % 2 == 0]
#     if len(chet) == 0 and (a[0]*a[0] > (a[1] + a[2] + a[3])):
#         cnt += 1
# print(cnt)


# f = open('3')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(ne_povt) == 5 and (3*(min(a) + max(a)) >= 2*(sum(a) - max(a) - min(a))):
#         cnt += 1
# print(cnt)


# f = open('4')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     ne_povt.sort()
#     if len(set(povt)) == 1 and len(ne_povt) == 4 and (ne_povt[0] + ne_povt[-1] <= povt[0]*2):
#         cnt += 1
# print(cnt)


# f = open('5')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(set(povt)) == 2 and len(ne_povt) == 3 and (sum(povt)/4 < sum(ne_povt)/3):
#         cnt += 1
# print(cnt)


# f = open('6')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(set(povt)) == 1 and len(ne_povt) == 3 and ((ne_povt[0]*ne_povt[1]*ne_povt[2]) > sum(povt)):
#         cnt += 1
# print(cnt)


# f = open('7')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(set(povt)) == 2 and len(ne_povt) == 4 and (min(a) in povt):
#         cnt += 1
# print(cnt)


# f = open('8')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     if (a[0]*a[-1] == a[1]*a[2]) and a[-1]**2 > a[0]*a[-1]:
#         cnt += 1
# print(cnt)