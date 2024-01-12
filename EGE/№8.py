# from itertools import *
# numb = 1
# for i in product('АБВГДЕЖЗИК', repeat=3):
#     s = ''.join(i)
#     # print(numb, i)
#     if s == 'АГА':
#         print(numb)
#     numb += 1
# # 31 ('А', 'Г', 'А')


# from itertools import *
# numb = 1
# for i in product('АДИН', repeat=5):
#     s = ''.join(i)
#     if s == 'ДИАНА':
#         print(numb)
#     numb += 1
# # 397


# x = 1054
# s = ''
# while x > 0:
#     s += str(x % 5)
#     x = x // 5
# print(s[::-1])
# 13204 'MONEY'

# from itertools import *
# numb = 1
# for i in product('EMNOY', repeat=5):
#     if numb == 1055:
#         print(i)
#     numb += 1
# # ('M', 'O', 'N', 'E', 'Y')


# from itertools import *
# numb = 1
# for i in product('CLMSU', repeat=5):
#     if i[0] == 'S':
#         print(numb)
#     numb += 1
# # 1876


# from itertools import *
# numb = 1
# for i in product('АДИН', repeat=5):
#     if i.count('А') == 0:
#         print(numb)
#     numb += 1
# #342


# from itertools import *
# numb = 1
# for i in product('АЕКНРС', repeat=6):
#     if i.count('А') <= 3 and i.count('Н') == 2:
#         print(numb)
#         break
#     numb += 1
# #58


# from itertools import *
# numb = 1
# for i in product('АИЛПС', repeat=5):
#     if numb == 2791:
#         print(i)
#     numb += 1
# #('С', 'Л', 'И', 'П', 'А')


# from itertools import *
# cnt = 0
# for i in product('LOST', repeat=7):
#     if i.count('O') == 3:
#         cnt += 1
# print(cnt) #2835


# from itertools import *
# cnt = 0
# for i in product('PLAN', repeat=6):
#     if 0 < i.count('A') <= 4:
#         cnt += 1
# print(cnt) #3348


# from itertools import *
# cnt = 0
# for i in product('QWER123', repeat=5):
#     if i.count('1') + i.count('2') + i.count('3') == 2:
#         cnt += 1
# print(cnt) #5760


# from itertools import *
# cnt = 0
# sogl = 'БНДРЛ'
# gl = 'АЕО'
# for i in product('БАНДЕРОЛЬ', repeat=7):
#     # if (i.count('Б') + i.count('Н') + i.count('Д') + i.count('Р') + i.count('Л')) < (i.count('А') + i.count('Е') + i.count('О')):
#     gl = 0
#     sogl = 0
#     for j in i:
#         if j in 'БНДРЛ':
#             sogl += 1
#         elif j in 'АЕО':
#             gl += 1
#     if gl > sogl:
#         cnt += 1
# print(cnt) #995403


# from itertools import *
# cnt = 0
# for i in product('012345678', repeat=6):
#     s = ''.join(i)
#     if (i.count('3') == 1 and i[0] != '0'
#         and '30' not in s and '03' not in s
#         and '32' not in s and '23' not in s
#         and '34' not in s and '43' not in s
#         and '36' not in s and '63' not in s
#         and '38' not in s and '83' not in s):
#         cnt += 1
# print(cnt) #39744


# from itertools import *
# cnt = 0
# for i in product('01234567', repeat=5):
#     s = ''.join(i)
#     if (i.count('5') == 2 and i[0] != '0'
#         and '12' not in s and '21' not in s
#         and '32' not in s and '23' not in s
#         and '52' not in s and '25' not in s
#         and '72' not in s and '27' not in s):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('КОРСЕТ', repeat=4):
#     s = ''.join(i)
#     if (i.count('О') <= 1 and i[0] != 'О' and i[-1] != 'О'
#         and 'ОР' not in s and 'РО' not in s):
#         cnt += 1
# print(cnt) #785


# from itertools import *
# cnt = 0
# for i in permutations('КАСПЕР', r=6): #буква по одному разу
#     cnt += 1
# print(cnt) #720


# from itertools import *
# cnt = 0
# for i in permutations('QWERTYU', r=5): #буква по одному разу
#     s = ''.join(i)
#     if i[0] != 'W' and 'QE' not in s:
#         cnt += 1
# print(cnt) #1956


# from itertools import *
# cnt = 0
# for i in permutations('МАСЛО', r=5): #буква по одному разу
#     s = ''.join(i)
#     if i[0] != 'С' and 'МО' not in s:
#         cnt += 1
# print(cnt) #78


# from itertools import *
# cnt = 0
# for i in set(permutations('КАПРАЛ', r=6)):
#     s = ''.join(i)
#     if 'АА' not in s:
#         cnt += 1
# print(cnt) #240


# from itertools import *
# cnt = 0
# for i in set(permutations('КАРЕТА', r=4)):
#     s = ''.join(i)
#     if 'АА' not in s:
#         cnt += 1
# print(cnt) #156


# from itertools import *
# cnt = 0
# for i in permutations('012345678', r=5):
#     s = ''.join(i)
#     if (i[0] != '0' and i.count('1') + i.count('3')
#             + i.count('5') + i.count('7') == 3):
#         cnt += 1
# print(cnt) #4416






#ДЗ


# from itertools import *
# numb = 0
# for i in product('ABCDEFGHIJ', repeat=3):
#     s = ''.join(i)
#     numb += 1
#     if s == 'GIF':
#         print(numb)
#     print(numb, i)


# from itertools import *
# numb = 0
# for i in product('АИЛП', repeat=5):
#     numb += 1
#     s = ''.join(i)
#     if s == 'ПИАЛА':
#         print(numb, i)


# from itertools import *
# numb = 0
# for i in product('EIQTU', repeat=6):
#     numb += 1
#     if numb == 9115:
#         print(i)


# from itertools import *
# numb = 0
# for i in product('FNOST', repeat=3):
#     numb += 1
    # s = ''.join(i)
    # if 'F' not in s:
    #     print(numb, i)


# from itertools import *
# numb = 0
# for i in product('АЙЛФ', repeat=4):
#     numb += 1
#     s = ''.join(i)
#     if ('А' not in s) and ('Л' not in s):
#         print(numb, i)


# from itertools import *
# numb = 0
# cnt = 0
# for i in product('CHAIN', repeat=5):
#     numb += 1
#     if i.count('H') == 1:
#         print(numb, i)
#         cnt += 1
# print(cnt)


# from itertools import *
# numb = 0
# cnt = 0
# for i in product('WXYZ', repeat=5):
#     numb += 1
#     if (i.count('X') == 1) or (i.count('X') == 2) or (i.count('X') == 3):
#         print(numb, i)
#         cnt += 1
# print(cnt)


# from itertools import *
# numb = 0
# cnt = 0
# for i in product('ABCD123', repeat=4):
#     numb += 1
#     # if ((i.count('1') == 1 and i.count('2') == 0 and i.count('3') == 0) or
#     #     (i.count('1') == 0 and i.count('2') == 1 and i.count('3') == 0) or
#     #         (i.count('1') == 0 and i.count('2') == 0 and i.count('3') == 1)):
#     if i.count('1') + i.count('2') + i.count('3') == 1:
#         print(numb, i)
#         cnt += 1
# print(cnt)


# from itertools import *
# numb = 0
# cnt = 0
# gl = 'АОИ'
# sogl = 'ЛГРТМ'
# for i in product('АЛГОРИТМ', repeat=7):
#     if (i.count('А') + i.count('И') + i.count('О') < (i.count('Л') + i.count('Г') +
#     i.count('Р') + i.count('Т') + i.count('М'))):
#         cnt += 1
# #     gl = 0
# #     sogl = 0
# #     for j in i:
# #         if j in 'АОИ':
# #             gl += 1
# #         elif j in 'ЛГРТМ':
# #             sogl += 1
# #     if sogl > gl:
# #         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('01234567', repeat=5):
#     s = ''.join(i)
#     if (s.count('4') == 2 and s[0] != '0'
#         and '14' not in s and '41' not in s
#         and '34' not in s and '43' not in s
#         and '54' not in s and '45' not in s
#         and '74' not in s and '47' not in s):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('ПАЛЬТО', repeat=5):
#     s = ''.join(i)
#     if ((s.count('О') <= 2) and
#         s[0] != 'О' and s[-1] != 'О' and 'ЛО' not in s and 'ОЛ' not in s):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in permutations('БИГМЭН', r=6):
#     cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in permutations('ПАРНИК', r=5):
#     s = ''.join(i)
#     if s[0] != 'П' and 'ИА' not in s:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in set(permutations('ДИАНА', r=5)):
#     s = ''.join(i)
#     if 'АА' not in s:
#         cnt += 1
# print(cnt)
