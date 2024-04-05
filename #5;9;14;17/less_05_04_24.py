# def to_bases5(x):
#     s = ''
#     while x > 0:
#         s = str(x % 5) + s
#         x = x // 5
#     return s
# min_r = []
# for n in range(1, 100000):
#     n5 = to_bases5(n)
#     if n % 7 == 0:
#         n5 = n5[:4] + n5 + '0'*(4 - len(n5)) + n5[-4:]
#     else:
#         n5 += bin((n % 7) * 2)[2:]
#     R = int(n5, 5)
#     if R % 760 == 0 and R > 1000:
#         min_r.append(R)
# print(min(min_r)) #13680


# from string import *
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
#
# for n in range(10000000, 0 , -1):
#     n39 = to_base39(n)
#     if n % 7 == 0:
#         n39 = 'F32' + n39 + '32Z'
#     else:
#         n39 += to_base39((n % 123) * 54)
#     R = from_base39(n39)
#     if R < 1000000:
#         print(n)
#         break #999990




# for x in '0123456789ABCDEFGHIJKLM':
#     if (int(f'2{x}2{x}2{x}2{x}2', 23) + int(f'20{x}23', 23) + int(f'1{x}235', 23)) % 25 == 0:
#         print((int(f'2{x}2{x}2{x}2{x}2', 23) + int(f'20{x}23', 23) + int(f'1{x}235', 23)) // 25)
#8187098290


# s = 1331**650 - 15 * 121**610 + 22 * 11**510 - 3 * 11**100 - 121
# cnt = 0
# while s > 0:
#     if s % 11 == 10:
#         cnt += 1
#     s = s // 11
# print(cnt)


# for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:21]:
#     for y in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:21]:
#         if (int(f'13{y}{x}9', 21) + int(f'39{y}99', 21)) % 18 != 0:
#             break
#     else:
#         print((int(f'133{x}9', 21) + int(f'39399', 21)) // 18) #45554


# for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:26]:
#     for y in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:26]:
#         s = (int(f'13{y}{x}9', 26)) + int(f'23{y}13', 26)
#         if s % 4 != 0:
#             break
#     else:
#         y = 3
#         s = (int(f'13{y}{x}9', 26)) + int(f'23{y}13', 26)
#         print(x, s // 8) #185141


