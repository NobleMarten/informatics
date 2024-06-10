# from itertools import *
# cnt = 0
# for i in product('ЕГЭ', repeat=5):
#     s = ''.join(i)
#     if s.count('Е') == 1:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('EIGHT', repeat=8):
#     s = ''.join(i)
#     if s.count('G') > 0:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('СМАРТ', repeat=6):
#     s = ''.join(i)
#     if s.count('Р') <= 1 and 'РТ' not in s and 'ТР' not in s and s[0] != 'Р' and s[-1] != 'Р':
#         cnt += 1
# print(cnt)


# from itertools import *
# numb = 0
# for i in product('EILMS', repeat=4):
#     numb += 1
#     s = ''.join(i)
#     if 'LIME' in s:
#         print(numb)


# from itertools import *
# numb = 0
# for i in product('AINRT', repeat=5):
#     numb += 1
#     s = ''.join(i)
#     if numb == 400:
#         print(s)


# from itertools import *
# numb = 0
# for i in product('АЙЛФ', repeat=4):
#     numb += 1
#     s = ''.join(i)
#     if 'А' not in s and 'Л' not in s:
#         print(numb)


# from itertools import *
# cnt = 0
# numb = 0
# for i in product('АЕЖМНОРТ', repeat=6):
#     numb += 1
#     s = ''.join(i)
#     if s[0] == 'О' and (s.count('Ж') == 2 or s.count('Ж') == 3) and numb % 3 == 0:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('ABCD5129', repeat=6):
#     s = ''.join(i)
#     if (s.count('1') + s.count('2') + s.count('5') + s.count('9')) == 4:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('345678', repeat=7):
#     s = ''.join(i)
#     if s.count('5') == 2:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in set(product('ПРОЦЕССОР', repeat=6)):
#     s = ''.join(i)
#     if s.count('П') >= 2 and 'ЦС' not in s and 'СЦ' not in s:
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product('0123456', repeat=6):
#     s = ''.join(i)
#     if (s.count('5') == 2 and s[0] != '0' and ('50' not in s and '05' not in s
#                                                and '52' not in s and '25' not in s
#                                                and '54' not in s and '45' not in s
#                                                and '56' not in s and '65' not in s)):
#         cnt += 1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in permutations('ГЕЛИЙ', r=5):
#     s = ''.join(i)
#     if s[0] != 'Й' and 'ИЕЙ' not in s:
#         cnt += 1
# print(cnt)


from itertools import *
cnt = 0
for i in set(permutations('ДИАНА', r=5)):
    s = ''.join(i)
    if 'АА' not in s:
        cnt += 1
print(cnt)