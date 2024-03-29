# f = open('24var18-20.txt')
# s = f.readline()
# # s = '1112344444452421'
# cnt = 1
# max_cnt = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         cnt += 1
#         max_cnt = max(max_cnt, cnt)
#     else:
#         cnt = 1
# print(max_cnt)


# f = open('24var18-20.txt')
# s = f.readline()
# s = '1121212122222'
# cnt = 1
# max_cnt = 1
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         cnt += 1
#         max_cnt = max(max_cnt, cnt)
#     else:
#         cnt = 1
# print(max_cnt)


# f = open('24var18-20.txt')
# s = f.readline()
# # s = '112345333'
# cnt = 1
# max_cnt = 1
# for i in range(len(s)-1):
#     if s[i] < s[i+1]:
#         cnt += 1
#         max_cnt = max(max_cnt, cnt)
#     else:
#         cnt = 1
# print(max_cnt)


# f = open('24var13-17.txt')
# s = f.readline()
# # s = 'SWABCEGN'
# cnt = 1
# max_cnt = 1
# for i in range(len(s)-1):
#     if s[i] >= s[i+1]:
#         cnt += 1
#         max_cnt = max(max_cnt, cnt)
#     else:
#         cnt = 1
# print(max_cnt)


# f = open('24var13-17.txt')
# s = f.readline()
# cnt = 1
# max_cnt = 1
# s = s.split('Z')
# for i in range(len(s)):
#     max_cnt = max(len(s[i]), max_cnt)
# print(max_cnt)


# f = open('24var13-17.txt')
# s = f.readline()
# cnt = 1
# max_cnt = 1
# s = s.split('Z')
# print(s)
# for i in range(len(s)-1):
#     max_cnt = max(len(s[i]) + len(s[i+1]) + 1, max_cnt)
# print(max_cnt)


# f = open('24var13-17.txt')
# s = f.readline()
# cnt = 1
# max_cnt = 1
# s = s.split('Z')
# for i in range(len(s)-2):
#     max_cnt = max(len(s[i]) + len(s[i+1]) + len(s[i+2]) + 2, max_cnt)
# print(max_cnt)


# f = open('24var09-12.txt') #11
# s = f.readline()
# cnt = 1
# max_cnt = 1
# s = s.replace('12', '*')
# s = s.replace('21', '*')
# s = s.split('*')
# for i in range(len(s)-1):
#     if len(s[i]) > max_cnt:
#         max_cnt = len(s[i])
#         k = i
# print(s[k])
# print(len(s[k])+2)


# f = open('24var09-12.txt') #12
# s = f.readline()
# cnt = 1
# max_cnt = 1
# s = s.replace('12', '1 2')
# s = s.replace('21', '2 1')
# s = s.replace('13', '1 3')
# s = s.replace('31', '3 1')
# s = s.split(' ')
# for i in range(len(s)-1):
#     if len(s[i]) > max_cnt:
#         max_cnt = len(s[i])
#         k = i
# print(s[k])
# print(s[k-1])
# print(len(s[k]))


# f = open('24var09-12.txt') #9
# s = f.readline()
# max_cnt = 1
# s = s.replace('00', '0 0')
# s = s.split(' ')
# for i in range(len(s)):
#     max_cnt = max(max_cnt, len(s[i]))
# print(max_cnt)


# f = open('24var09-12.txt') #10
# s = f.readline()
# max_cnt = 1
# s = s.replace('000', '00 0')
# # s = s.replace('000', '0 00')
# s = s.split(' ')
# for i in range(len(s)):
#     if max_cnt < len(s[i]):
#         max_cnt = len(s[i])
#         k = i
# print(s[k-1])
# print(s[k])
# print(len(s[k])+1)


# f = open('24var06.txt')
# s = f.readline()
# # s = 'ABCCADADEEEBCADABBEDCA'
# k = 35
# a = []
# for i in range(len(s)):
#     if s[i] == 'A':
#         a.append(i)
# # print(a)
# min_zn = 10000000
# for j in range(len(a)-k+1):
#     min_zn = min(min_zn, a[j+k-1] - a[j] + 1)
# print(min_zn)


# f = open('24var01.txt')
# s = f.readline()
# k = 2024
# a = []
# min_zn = 1000000000
# for i in range(len(s)):
#     if s[i] == 'A':
#         a.append(i)
# for j in range(len(a)-k+1):
#     min_zn = min(min_zn, a[j+k-1] - a[j] + 1)
# print(min_zn)


# f = open('24var07.txt')
# s = f.readline()
# k = 21
# a = []
# min_zn = 1000000000
# s = s.replace('AB', '*')
# for i in range(len(s)):
#     if s[i] == '*':
#         a.append(i)
# for j in range(len(a)-k+1):
#     min_zn = min(min_zn, a[j+k-1] - a[j] + 22)
# print(min_zn)


f = open('24var02.txt')
s = f.readline()
k = 350
a = []
max_zn = 0
for i in range(len(s)):
    if s[i] == 'A':
        a.append(i)
for j in range(len(a)-k-1):
    max_zn = max(max_zn, a[j+k+1] - a[j] - 1)
print(max_zn)
