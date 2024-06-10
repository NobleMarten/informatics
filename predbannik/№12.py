# s = '2' + '8'*89
# while '28' in s or '188' in s or '3888' in s:
#     if '28' in s:
#         s = s.replace('28', '1', 1)
#     else:
#         if '188' in s:
#             s = s.replace('188', '3', 1)
#         else:
#             s = s.replace('3888', '2', 1)
# print(s)


# s = '>' + 24*'7' + 15*'5' + 11*'3'
# while '>7' in s or '>5' in s or '>3' in s:
#     if '>7' in s:
#         s = s.replace('>7', '555>', 1)
#     if '>5' in s:
#         s = s.replace('>5', '5>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '7>', 1)
#     summ = s.count('5')*5 + s.count('7')*7 + s.count('3')*3
# print(summ)


# def sum_digits(n):
#     return sum(map(int, n))
# for n in range(4, 10000):
#     s = '5' + n*'2'
#     while '52' in s or '1122' in s or '2222' in s:
#         if '52' in s:
#             s = s.replace('52', '11', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#         if '1122' in s:
#             s = s.replace('1122', '25', 1)
#     # summ = s.count('5') + s.count('2') + s.count('1')
#     if sum_digits(s) == 64:
#         print(n)


for n in range(1, 1000):
    s = '>' + 30*'1' + 20*'2' + n*'3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 2)
    summ = s.count('1') + s.count('2')*2 + s.count('3')*3
    if summ % 11 == 0:
        print(n)