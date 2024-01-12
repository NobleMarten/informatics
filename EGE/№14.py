# n = 32**7 + 8**5 + 16
# print(bin(n)[2:].count('1'))


# n = 512**11 + 64**6 - 8
# print(oct(n)[2:].count('7'))


# n = 11**2222 + 7**1111 - 3**777
# print(bin(n)[2:].count('1'))


# n = 512**125 + 128**625 - 32**125
# print(bin(n)[2:].count('0'))


# s = 256**123 + 64**12 - 16
#1
# zifri = []
# while s > 0:
#     zifri.append(s % 4)
#     s = s // 4
# print(zifri.count(3))
#2
# cnt = 0
# while s > 0:
#     if s % 4 == 3:
#         cnt += 1
#     s = s // 4
# print(cnt)


# s = 200**3333 - 100**2222 + 50**1111 - 11

# zifri = []
# while s > 0:
#     zifri.append(s % 3)
#     s = s // 3
# print(zifri.count(2))

# cnt2 = 0
# while s > 0:
#     if s % 3 == 2:
#         cnt2 += 1
#     s = s // 3
# print(cnt2)


# s = 64**2023 + 32**2022 - 8**2021 - 2
# print(len(set(hex(s)[2:])))#6


# s = 64**2023 + 32**2022 - 8**2021 - 2
# zifri = []
# while s > 0:
#     zifri.append(s % 20)
#     s = s // 20
# print(len(set(zifri))) #20


# for n in range(3, 10):
#     if int('121', n + 1) == (int('121', n) + int('13', 16)):
#         print(n) #8


# for x in range(2, 20):
#     if (int('111', x) + int('13', 5)) == int('515', 6):
#         print(x)


# for x in range(0, 10):
#     if (int('1234' + str(x), 15) + int('5' + str(x) + '678', 15)) % 11 == 0:
#         print((int('1234' + str(x), 15) + int('5' + str(x) + '678', 15)) // 11) #28734

# n = 1 * 15**4 + 2 * 15**3 + 3 * 15**2 + 4 * 15
# m = 5 * 15**4 + 6 * 15**2 + 7 * 15 + 8
# for x in range(1, 10):
#     if (n + x + m + x * 15**3) % 11 == 0:
#         print((n + x + m + x * 15**3) // 11)


# for x in '0123456789ABCDEFGH':
#     if (int('2671' + x, 18) + int('8513' + x, 18)) % 13 == 0:
#         print((int('2671' + x, 18) + int('8513' + x, 18)) // 13)


# for x in '0123456789ABCDEF':
#     if (int(f'D49{x}1', 16) + int(f'48A3{x}', 16)) % 14 == 0:
#         print((int(f'D49{x}1', 16) + int(f'48A3{x}', 16)) // 14)


#СтатГрад

# for x in range(0, 37):
#     if ((6 * 37**3 + 5 * 37**2 + 4 * 37 + x) + 5 * 37**3 + x * 37**2 + 4 * 37 + 7) % 79 == 0:
#         print(((6 * 37**3 + 5 * 37**2 + 4 * 37 + x) + 5 * 37**3 + x * 37**2 + 4 * 37 + 7) // 79)


# for x in '0123456789ABCDEFGHIJ':
#     for y in '0123456789ABCDEFGHIJ':
#         if (int(f'B{y}11CB{x}G17', 20) + int(f'8A{x}17', 20)) % 107 == 0:
#             print(x, y, (int(f'B{y}11CB{x}G17', 20) + int(f'8A{x}17', 20)) // 107) #55280238722

# for p in range(9, 36):
#     for x in range(0, p):
#         for y in range(0, p):
#             if (((1*p**3 + 7*p**2 + x*p + 8) + (y*p**3 + x*p**2 + y*p + 6)) ==
#                 (9*p**3 + y*p**2 + y*p + 0)):
#                 print(x*p**2 + x*p + y) #2737

# from string import *
# zifri = '0123456789' + ascii_uppercase #заглавные буквы латинского алфавита
# for p in range(10, 37):
#     for x in zifri[:p]:
#         for y in zifri[:p]:
#             if (int(f'17{x}8', p) + int(f'{y}{x}{y}6', p)) == int(f'9{y}{y}0', p):
#                 print(int(f'{x}{x}{y}', p))



#ДЗ



# s = 64**13 + 32**6 - 16**2
# print(bin(s)[2:].count('1'))


# s = 4096**3125 - 512**625 + 64**125 - 8**25
# print(oct(s)[2:].count('7'))


# s = 32**540 + 16**231 - 2**10
# print(bin(s)[2:].count('1'))


# s = 512**230 + 256**64 - 32**23
# print(bin(s)[2:].count('0'))

# def f(n):
#     s = ''
#     while n > 0:
#         s = str(n % 5) + s
#         n = n // 5
#     return s
# s = 625**134 * 125**32 + 25**52 - 5
# print(f(s).count('4'))


# s = 343**21 + 49**14 + 7
# cnt = 0
# while s > 0:
#     if s % 7 == 0:
#         cnt += 1
#     s = s // 7
# print(cnt)


# s = 7777**290 - 777**29 + 77**2 - 7
# def f(n):
#     s = ''
#     while n > 0:
#         s = str(n % 20) + s
#         n = n // 20
#     return s
# k = f(s)
# print(len(set(k)))

# s = 7777 ** 290 - 777 ** 29 + 77 ** 2 - 7
#
# a = set()
#
# while s > 0:
#
#     a.add(s % 20)
#
#     s //= 20
#
# print(len(a))

# for x in range(4, 36):
#     if (int('132', x + 1)) == (int('132', x) + int('34', 8)):
#         print(x)

#
# for x in range(7, 37):
#     if (int('165', x) + int('18', 9)) == int('416', 7):
#         print(x)


# for x in '0123456789ABCDEFGH':
#     if (int(f'AB5{x}3', 18) + int(f'EF{x}13', 18)) % 17 == 0:
#         print((int(f'AB5{x}3', 18) + int(f'EF{x}13', 18)) // 17)


# for x in '0123456789ABCDEFGHIJ':
#     if (int(f'13{x}CF', 20) + int(f'47GH{x}', 20)) % 19 == 0:
#         print((int(f'13{x}CF', 20) + int(f'47GH{x}', 20)) // 19)


# for x in '01234':
#     if (int(f'10{x}01', 5) + int(f'{x}0000', 5)) % 4 == 0:
#         print((int(f'10{x}01', 5) + int(f'{x}0000', 5)) // 4)


# s = 3 * 37**3 + 2 * 37**2 + 4 #x * 37
# m = 5 * 37**3 + 2 * 37 + 9 #x * 37**2
# for x in range(0, 37):
#     if (s + x * 37 + m + x * 37**2) % 63 == 0:
#         print((s + x * 37 + m + x * 37**2) // 63)


# for x in '0123456789ABCD':
#     for y in '0123456789ABCD':
#         if (int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14)) % 107 == 0:
#             print((int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14)) // 107)


# for p in range(14, 37):
#     for x in range(0, p):
#         for y in range(0, p):
#             if (((1*p**3 + x*p**2 + y*p + 1) + (x*p**3 + y*p**2 + x*p + 9)) ==
#                     (13*p**3 + 6*p**2 + 5*p + y)):
#                 print(x*p**2 + x*p + y)


# from string import *
# zifri = '0123456789' + ascii_uppercase + 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭ'
# # s = 5*67**4 + 1 #y*67**3 + x*67**2 + y*67
# # m = 4*67**4 + 2*67 + 7 #x*67**3 + y*67**2
# for p in range(5, 67):
#     for x in zifri:
#         for y in zifri:
#             if (int(f'5{y}{x}{y}1', p) + int(f'4{x}{y}27', p)) % 5437 == 0:
#                 print(x, y, (int(f'5{y}{x}{y}1', p) + int(f'4{x}{y}27', p)) // 5437)


def f(n):
    s = ''
    while n > 0:
        s = str(n % 9) + s
        n = n // 9
    return s
for x in '0123456789ABCDEFGHIJKL':
    p = int(f'5AG{x}2', 22) + int(f'6{x}2{x}7', 22)
    if f(p).count('7') == 2:
        print(x, p)
