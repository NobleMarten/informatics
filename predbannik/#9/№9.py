# f = open('9.1')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(ne_povt) == 5 and 3*(a[0]+a[-1]) >= 2*(a[1]+a[2]+a[3]):
#         cnt += 1
# print(cnt)


# f = open('9.2')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     nechet = []
#     # print(a)
#     # print(len(a))
#     for i in range(len(a)):
#         if a[i] % 2 != 0:
#             nechet.append(a[i])
#     if len(nechet) == 4 and a[0]**2 > (a[1]+a[2]+a[3]):
#         cnt += 1
# print(cnt)


# f = open('9.3')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     if ((a[0]*a[-1]) == (a[1]*a[2])) and (a[-1]**2 > (a[0]*a[-1])):
#         cnt += 1
# print(cnt)


# f = open('9.4')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(ne_povt) == 3 and len(set(povt)) == 2 and ((sum(povt) / 4) < (sum(ne_povt) / 3)):
#         cnt += 1
# print(cnt)


f = open('9.5')
cnt = 0
for s in f:
     a = list(map(int, s.split()))
     a.sort()
     povt = [x for x in a if a.count(x) > 1]
     ne_povt = [x for x in a if a.count(x) == 1]
     if len(ne_povt) == 4 and len(set(povt)) == 2 and (min(a) in povt):
         cnt += 1
print(cnt)