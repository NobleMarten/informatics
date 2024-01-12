# №8
# s = '3' * 30
# while '333' in s or '555' in s:
#     if '333' in s:
#         s = s.replace('333', '5', 1)
#     else:
#         s = s.replace('555', '3', 1)
# print(s)


# s = '1' * 9 + '2' * 22
# while '111' in s or '222' in s:
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#     while '222' in s:
#         s = s.replace('222', '1', 1)
# print(s)


# s = '5' + '4' * 99
# while '54' in s or '644' in s or '7444' in s:
#     if '54' in s:
#         s = s.replace('54', '6', 1)
#     else:
#         if '644' in s:
#             s = s.replace('644', '7', 1)
#         else:
#             s = s.replace('7444', '5', 1)
# print(s)


# s = '3' * 76 + '5' * 24
# while '3333' in s or '5555' in s:
#     if '3333' in s:
#         s = s.replace('3333', '55', 1)
#     else:
#         s = s.replace('5555', '33', 1)
# print(s)


# s = '1' + '4' * 81
# while '14' in s or '244' in s or '3444' in s:
#     if '14' in s:
#         s = s.replace('14', '3', 1)
#     if '244' in s:
#         s = s.replace('244', '1', 1)
#     if '3444' in s:
#         s = s.replace('3444', '2', 1)
# print(s)


# s = '123' * 456
# while '12' in s or '3333' in s:
#     s = s.replace('12', '3', 1)
#     s = s.replace('3333', '3', 1)
# print(s)

# for n in range(91, 1000):
#     s = '3'*n
#     while '333' in s:
#         s = s.replace('333', '1', 1)
#         s = s.replace('111', '3', 1)
#     if s == '133':
#         print(n) #93
#         #break


# for n in range(4, 10000):
#     s = '5' + '2'*n
#     while '52' in s or '2222' in s or '3322' in s:
#         if '52' in s:
#             s = s.replace('52', '33', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#         if '3322' in s:
#             s = s.replace('3322', '25', 1)
#     summ = s.count('2')*2 + s.count('3')*3 + s.count('5')*5
#     if summ == 83:
#         print(n) #65


# ДЗ


# s = '1' * 113
# while '1111' in s:
#     s = s.replace('1111', '22', 1)
#     s = s.replace('222', '11', 1)
# print(s)


# s = '3' * 12 + '4' * 20
# while '333' in s or '444' in s:
#     while '333' in s:
#         s = s.replace('333', '4', 1)
#     while '444' in s:
#         s = s.replace('444', '3', 1)
# print(s)


# s = '1' + '8'*80
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s:
#         s = s.replace('18', '2', 1)
#     else:
#         if '288' in s:
#             s = s.replace('288', '3', 1)
#         else:
#             s = s.replace('3888', '1', 1)
# print(s)


# s = '7'*96 + '4'*24
# while '4444' in s or '7777' in s:
#     if '4444' in s:
#         s = s.replace('4444', '77')
#     else:
#         s = s.replace('7777', '44')
# print(s)


# s = '1' + '8'*90
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s:
#         s = s.replace('18', '2')
#     else:
#         if '288' in s:
#             s = s.replace('288', '3')
#         else:
#             s = s.replace('3888', '1')
# print(s)


# s = '5'*675
# while '555' in s or '333' in s:
#     if '555' in s:
#         s = s.replace('555', '3', 1)
#     else:
#         s = s.replace('333', '5', 1)
# print(s)


# s = '2006'*498
# while '200' in s or '666' in s:
#     s = s.replace('200', '66')
#     s = s.replace('666', '66')
# print(s)


# for n in range(342, 1000, 9):
#     s = '8'*n
#     while '888' in s or '44' in s or '5' in s:
#         if '888' in s:
#             s = s.replace('888', '4', 1)
#         if '44' in s:
#             s = s.replace('44', '58', 1)
#         if '5' in s:
#             s = s.replace('5', '8', 1)
#     print(n, s)


# for n in range(101, 1000):
#     s = '1'*n
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222', '1', 1)
#     if s == '11':
#         print(n)


# s = '>' + '7'*24 + '5'*15 + '3'*11
# while '>7' in s or '>5' in s or '>3' in s:
#     if '>7' in s:
#         s = s.replace('>7', '555>', 1)
#     if '>5' in s:
#         s = s.replace('>5', '5>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '7>', 1)
#     summ = s.count('7')*7 + s.count('5')*5 + s.count('3')*3
# print(summ)


# for n in range(0, 10000):
#     s = '3' + '5'*n
#     while '355' in s or '25' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '5', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     summ = s.count('3')*3 + s.count('5')*5 + s.count('2')*2
#     if summ == 27:
#         print(n)


for n in range(4, 10000):
    s = '5' + '2'*n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    summ = s.count('1')*1 + s.count('2')*2 + s.count('5')*5
    if summ == 64:
        print(n)


# s = '3'*60 + '1'*60 + '2'*60
# while '21' in s or '31' in s or '23' in s:
#     if '21' in s:
#         s = s.replace('21', '12', 1)
#     if '31' in s:
#         s = s.replace('31', '13', 1)
#     if '23' in s:
#         s = s.replace('23', '32', 1)
# print(s)
#
# d = s.find('3')
# print(d)