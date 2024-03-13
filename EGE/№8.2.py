# from itertools import product
# numb = 0
# for i in product('CLMSU', repeat=5):
#     numb += 1
#     if i[0] == 'S':
#         print(numb, i) #1876


# from itertools import *
# numb = 0
# for i in product('АЕКНРС', repeat=6):
#     numb += 1
#     if i.count('А') <= 3 and i.count('Н') == 2:
#         print(numb, i) #58


# from itertools import *
# numb = 0
# cnt = 0
# for i in product('АИМНОРТФ', repeat=5):
#     numb += 1
#     if i[0] != 'О' and (i.count('Н') == 1 or i.count('Н') == 2) and numb % 2 != 0:
#         cnt += 1
# print(cnt) #5992


# from itertools import *
# numb = 0
# cnt = 0
# for i in product('АВГДИРЯ', repeat=6):
#     numb += 1
#     if numb % 2 == 0 and i[0] != 'Д' and i.count('Р') >= 2:
#         cnt += 1
# print(cnt) #10804


# from itertools import *
# cnt = 0
# for i in product('QWER123', repeat=5):
#     if (i.count('1') + i.count('2') + i.count('3')) == 2:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# gl = 'АЕО'
# sogl = 'БНДРЛ'
# for i in product('БАНДЕРОЛЬ', repeat=7):
#     if sum(i.count(x) for x in gl) > sum(i.count(x) for x in sogl):
#         cnt += 1
#     # cnt_gl = 0
#     # for x in gl:
#     #     cnt_gl += i.count(x)
#     # cnt_sogl = 0
#     # for x in sogl:
#     #     cnt_sogl += i.count(x)
#     # if cnt_gl > cnt_sogl:
#     #     cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('012345678', repeat=6):
#     s = ''.join(i)
#     if (i.count('3') == 1 and i[0] != '0' and
#             all('3' + x not in s and x + '3' not in s for x in '02468')):
#         # '03' not in s and '30' not in s and \
#         # '23' not in s and '32' not in s and \
#         # '43' not in s and '34' not in s and \
#         # '63' not in s and '36' not in s and \
#         # '83' not in s and '38' not in s:
#
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('0123456', repeat=5):
#     s = ''.join(i)
#     if (i.count('2') == 2 and i[0] != '0' and
#         all(x+'2' not in s and '2'+x not in s for x in '135')):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in set(permutations('КАРЕТА', r=4)):
#     s = ''.join(i)
#     if 'АА' not in s:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for x in permutations('0123456789', r=6):
#     cnt_ok = 0
#     if x[0] != '0':
#         for i in range(len(x) - 1):
#             if (int(x[i]) % 2 != int(x[i + 1]) % 2):
#                 cnt_ok += 1
#         if cnt_ok == 5:
#             cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for x in permutations('01234', r=4):
#     if all(x[i] > x[i+1] for i in range(len(x)-1)):
#         cnt += 1
# print(cnt)



#ДЗ



# from itertools import *
# numb = 0
# for i in product('ELMNO', repeat=5):
#     numb += 1
#     if i[0] == 'N':
#         print(numb, i)
#         break


# from itertools import *
# numb = 0
# for i in product('DGLO', repeat=4):
#     numb += 1
#     if i.count('D') == 0:
#         print(numb, i)


# from itertools import *
# numb = 0
# cnt = 0
# for i in product('АЕЖМНОРТ', repeat=6):
#     numb += 1
#     if numb % 3 == 0 and i[0] == 'О' and (i.count('Ж') == 2 or i.count('Ж') == 3):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('ABCD5129', repeat=6):
#     if i.count('5') + i.count('1') + i.count('2') + i.count('9') == 4:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# gl = 'ИАОЕ'
# sogl = 'ЧКБМНЩ'
# for i in product('ЧКИБАМОНЩЕ', repeat=6):
#     if (i.count('Щ') == 1 and (i[0] in 'ИАОЕ') and
#         sum(i.count(x) for x in gl) > sum(i.count(x) for x in sogl)):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('0123456', repeat=6):
#     s = ''.join(i)
#     if i[0] != '0' and i.count('5') == 2 and all('5'+x not in s and x+'5' not in s for x in '0246'):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in set(permutations('АДЖИКА', r=6)):
#     s = ''.join(i)
#     if 'АА' not in s:
#         cnt += 1
# print(cnt)


from itertools import *
cnt = 0
for i in permutations('0123456789AB', r=9):
    if i[0] != '0':
        s = ''.join(i)
        s = s.replace('0', '*')
        s = s.replace('2', '*')
        s = s.replace('4', '*')
        s = s.replace('6', '*')
        s = s.replace('8', '*')
        s = s.replace('A', '*')
        if s.count('*') == 5 and int(''.join(i), 12) % 2 != 0:
            cnt += 1
print(cnt)