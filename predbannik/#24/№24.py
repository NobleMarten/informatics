# f = open('24.3.txt')
# s = f.readline()
# a = s.split('O')
# new_a = []
# for i in range(len(a)-1):
#     new_a.append((a[i] + 'O' + a[i+1]))
# print(len(max(new_a, key=len)))


# f = open('24.5.txt')
# s = f.readline()
# s = s.replace('FJN', '*')
# s = s.replace('JFN', '*')
# for n in range(1, 100):
#     if '*'*n in s:
#         print(n)


# f = open('24.6.txt')
# s = f.readline()
# s = s.replace('FJW', 'FJ JW')
# s = s.replace('FJ', '*')
# s = s.replace('JW', '*')
# for n in range(1, 100):
#     if '*'*n in s:
#         print(n)


# f = open('24.7.txt')
# s = f.readline()
# s = s.replace('YCRR', 'YCR CRR')
# a = s.split()
# print(len(max(a, key=len)))


# f = open('24.8.txt')
# s = f.readline()
# s = s.replace('I', 'N')
# s = s.replace('F', 'N')
# s = s.replace('NN', 'N N')
# s = s.replace('NN', 'N N')
# a = s.split()
# print(len(max(a, key=len)))


# f = open('24.9.txt')
# s = f.readline()
# s = s.replace('B', 'A')
# s = s.replace('C', 'A')
# s = s.replace('8', '9')
# s = s.replace('AA', 'A A')
# s = s.replace('AA', 'A A')
# s = s.replace('99', '9 9')
# s = s.replace('99', '9 9')
# a = s.split()
# print(len(max(a, key=len)))

#важные задачи!
# максимальное кол-во (100 раз)
# f = open('24.10.txt')
# s = 'M' + f.readline() +'M'
# ind_M = []
# for i in range(len(s)):
#     if s[i] == 'M':
#         ind_M.append(i)
# res = []
# for i in range(len(ind_M) - 101):
#     res.append(ind_M[i+101] - ind_M[i] - 1)
# print(max(res))
#
# минимальное кол-во (210 раз)
# f = open('24.11.txt')
# s = f.readline()
# ind_T = []
# for i in range(len(s)):
#     if s[i] == 'T':
#         ind_T.append(i)
# res = []
# for i in range(len(ind_T) - 209):
#     res.append(ind_T[i+209] - ind_T[i] + 1)
# print(min(res))
#
# f = open('24.12.txt')
# s = f.readline()
# ind_AC = []
# for i in range(len(s)):
#     if s[i:i+2] == 'AC':
#         ind_AC.append(i)
# res = []
# for i in range(len(ind_AC)-24):
#     res.append((ind_AC[i+24] + 1) - ind_AC[i] + 1)
# print(min(res))


# f = open('24.13.txt')
# s = f.readline()
# cnt = 1
# max_cnt = 1
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         cnt += 1
#     else:
#         cnt = 1
#     max_cnt = max(max_cnt, cnt)
# print(max_cnt)
#
# f = open('24.14.txt')
# s = f.readline()
# cnt = 1
# max_cnt = 1
# for i in range(len(s)-1):
#     if s[i] >= s[i+1] > '5':
#         cnt += 1
#     else:
#         cnt = 1
#     max_cnt = max(max_cnt, cnt)
# print(max_cnt)

from string import *
f = open('24.15.txt')
s = f.readline()
# for symb in ascii_letters:
#     s = s.replace(symb, ' ')
# for i in '13579':
#     s = s.replace(i, '1')
# for i in '02468':
#     s = s.replace(i, '0')
# s = s.replace('11', '1 1').replace('11', '1 1')
# s = s.replace('00', '0 0').replace('00', '0 0')
# a = s.split()
# print(max(a, key=len))
cnt = 1
max_cnt = 1
for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isdigit() and int(s[i]) % 2 != int(s[i+1]) % 2:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)