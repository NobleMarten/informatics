# def to_base3(x):
#     s = ''
#     while x > 0:
#         s = str(x % 3) + s
#         x = x // 3
#     return s
# for n in range(1, 1000):
#     n3 = to_base3(n)
#     if n % 3 == 0:
#         n3 += n3[-3:]
#     else:
#         n3 += to_base3((n % 3) * 3)
#     r = int(n3, 3)
#     if r > 344:
#         print(n)


# def to_base39(x):
#     s = ''
#     alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#     while x > 0:
#         s = alph[x % 39] + s
#         x = x // 39
#     return s
# def from_base39(x):
#     x = x[::-1]
#     s = 0
#     alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#     for i in range(len(x)):
#         s += alph.index(x[i]) * (39**i)
#     return s
# for n in range(10000000, 0 , -1):
#     n39 = to_base39(n)
#     if n % 13 == 0:
#         n39 = '222' + n39 + '32F'
#     else:
#         n39 += to_base39((n % 123) * 58)
#     r = from_base39(n39)
#     if r < 100000:
#         print(n)
#         break


# for x in '0123456789ABCDEFGHIJ':
#     if (int(f'13{x}CF', 20) + int(f'47GH{x}', 20)) % 19 == 0:
#         print((int(f'13{x}CF', 20) + int(f'47GH{x}', 20)) // 19)


# s = 16**161 - 16**61 - 16**6
# # print(hex(s).count('f'))
# cnt = 0
# while s > 0:
#     if s % 16 == 15:
#         cnt += 1
#     s = s // 16
# print(cnt)


# for x in '0123456789ABCD':
#     for y in '0123456789ABCD':
#         if (int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14)) % 107 == 0:
#             print(x, y)
# print((int(f'ABCD3A241', 14) + int(f'19249', 14)) // 107)


# for x in '0123456789ABCDEFGHIJKLM':
#     for y in '0123456789ABCDEFGHIJKLM':
#         if (int(f'13{y}{x}9', 23) + int(f'22{y}22', 23)) % 2 != 0:
#             break
#     else:
#         print((int(f'136{x}9', 23) + int(f'22622', 23)) // 18)


# f = open('17.14 (1).txt')
# a = [int(s) for s in f]
# troiki = []
# max13 = max([x for x in a if abs(x) % 100 == 13])
# for i in range(len(a)-2):
#     if ((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i+1]))) == 5) + (len(str(abs(a[i+2]))) == 5)) == 2 and \
#             (a[i] + a[i+1] + a[i+2]) <= max13:
#         troiki.append(a[i]+a[i+1]+a[i+2])
# print(len(troiki), max(troiki))


# f = open('17.13 (1).txt')
# a = [int(s) for s in f]
# troiki = []
# min600 = min([x for x in a if abs(x) % 1000 == 600])
# for i in range(len(a)-2):
#     if (int((len(str(abs(a[i])))) == 5) + int((len(str(abs(a[i+1])))) == 5) + int((len(str(abs(a[i+2]))) == 5))) <= 2 and \
#             (a[i]+a[i+1]+a[i+2]) >= min600:
#         troiki.append(a[i]+a[i+1]+a[i+2])
# print(len(troiki), min(troiki))


# f = open('17_NnhR8gR.txt')
# a = [int(s) for s in f]
# pari = []
# max11 = max([x for x in a if abs(x) % 100 == 11])
# for i in range(len(a)-1):
#     if (oct(a[i])[-1] == oct(a[i+1])[-1]) and ((a[i] % 5 == 0 and a[i+1] % 7 == 0) or \
#             (a[i+1] % 5 == 0 and a[i] % 7 == 0)) and (a[i] % 35 != 0 and a[i+1] % 35 != 0) and \
#             (a[i]**2 + a[i+1]**2) <= max11**2:
#         pari.append(a[i]+a[i+1])
# print(len(pari), min(pari))


# f = open('9.1')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(povt) == 2 and len(ne_povt) == 2 and povt[0] % 2 != 0 and ne_povt[0] % 2 == 0 \
#         and ne_povt[1] % 2 == 0:
#         cnt += 1
# print(cnt)


# f = open('9.2')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(set(povt)) == 1:
#         n = povt[0]**2
#         summ = sum(int(x) for x in str(n))
#         if oct(summ**2)[-1] == '0':
#             cnt += 1
# print(cnt)


# f = open('9.3')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(set(povt)) == 2 and len(ne_povt) == 4 and min(a) in povt:
#         cnt += 1
# print(cnt)


f = open('9 (1).txt')
cnt = 0
for s in f:
    a = list(map(float, s.split()))
    povt = [x for x in a if a.count(x) > 1]
    ne_povt = [x for x in a if a.count(x) == 1]
    if len(povt) == 2 and len(ne_povt) == 3 and sum(povt) < sum(ne_povt):
        cnt += 1
print(cnt)