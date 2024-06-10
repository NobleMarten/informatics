# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     n2 += str(n2.count('1') % 2)
#     n2 += str(n2.count('1') % 2)
#     r = int(n2, 2)
#     if r > 123:
#         print(r)


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 != 0:
#         n2 += '0'
#     else:
#         n2 = '1' + n2
#     if n2.count('1') % 2 == 0:
#         n2 += '1'
#     else:
#         n2 += '0'
#     r = int(n2, 2)
#     if r > 300:
#         print(n)


# res = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += n2[-2:]
#     else:
#         n2 = '1' + n2 + '0'
#     r = int(n2, 2)
#     if r > 320:
#         res.append(r)
# print(min(res))


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = n2 + bin(n2.count('1'))[2:]
#     else:
#         n2 = '1' + n2 + '00'
#     r = int(n2, 2)
#     if r > 403:
#         print(n)


# a = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 3 == 0:
#         n2 += n2[-3:]
#     else:
#         n2 += bin(3*(n % 3))[2:]
#     r = int(n2, 2)
#     if r > 54:
#         a.append(r)
# print(min(a))


# def chetv(x):
#     s = ''
#     while x > 0:
#         s = str(x % 4) + s
#         x = x // 4
#     return s
# for n in range(1, 1000):
#     n4 = chetv(n)
#     if n % 4 == 0:
#         n4 += n4[-2:]
#     else:
#         n4 += chetv(2*(n % 4))
#     r = int(n4, 4)
#     if r < 245:
#         print(n)


# def base3(x):
#     s = ''
#     while x > 0:
#         s = str(x % 3) + s
#         x = x // 3
#     return s
# for n in range(1, 1000):
#     n3 = base3(n)
#     if n % 3 == 0:
#         n3 = '1' + n3 + '02'
#     else:
#         n3 += base3(4*(n % 3))
#     r = int(n3, 3)
#     if r < 208:
#         print(n)


def base5(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x = x // 5
    return s
for n in range(1, 1000):
    n5 = base5(n)
    if n % 5 == 0:
        n5 += n5[:2]
    else:
        n5 += base5(7*(n % 5))
    r = int(n5, 5)
    if r < 245:
        print(n)