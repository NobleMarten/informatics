# s = 4**3000 + 8**2000 - 2**12 - 256
# s2 = bin(s)[2:]
# print(s2.count('1'))

# s = 281474976710656**22 - 1099511627776**10 - 48**19
# s16 = hex(s)
# print(s16.count('b'))

# s = 256**205 + 64**56 - 16**30
# s2 = bin(s)[2:]
# print(s2.count('0'))


# s = 6542**324 - 3560**67 + 730**12 - 510
# cnt = 0
# while s > 0:
#     if s % 3 == 2:
#         cnt += 1
#     s = s // 3
# print(cnt)


# for x in '0123456789ABCDEF':
#     if (int(f'{x}432', 16) + int(f'234{x}', 16)) % 15 == 0:
#         print(x, (int(f'{x}432', 16) + int(f'234{x}', 16)) // 15)


# for x in '01234':
#     if (int(f'10{x}01', 5) + int(f'{x}0000', 5)) % 4 == 0:
#         print(x, (int(f'10{x}01', 5) + int(f'{x}0000', 5)) // 4)


# for x in '0123456789ABCDEFGHIJ':
#     if (int(f'13{x}CF', 20) + int(f'47GH{x}', 20)) % 19 == 0:
#         print(x, (int(f'13{x}CF', 20) + int(f'47GH{x}', 20)) // 19)


for x in '0123456789ABCD':
    for y in '0123456789ABCD':
        if (int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14)) % 107 == 0:
            print(x, (int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14)) // 107)