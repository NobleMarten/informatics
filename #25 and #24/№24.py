# f = open('24.5.txt')
# s = f.readline()
# s = s.replace('I', 'F')
# s = s.replace('N', 'F')
# s = s.replace('FF', 'F F')
# s = s.replace('FF', 'F F')
# s = s.split(' ')
# max_ = 0
# # for x in range(len(s)):
# #     max_ = max(max_, len(s[x]))
# # print(max_)
# print(len(max(s, key=len)))


# f = open('24.6.txt')
# s = f.readline()
# s = s.replace('A', 'B')
# s = s.replace('C', 'B')
# s = s.replace('BB', 'B B')
# s = s.replace('BB', 'B B')
# s = s.replace('9', '8')
# s = s.replace('88', '8 8')
# s = s.replace('88', '8 8')
# s = s.split(' ')
# print(len(max(s, key=len)))


f = open('24.7.txt')
s = f.readline()
# s = 'xxACxACxxACxxxACxACxxAAC'
index_AC = []
for i in range(len(s) - 1):
    if s[i:i+2] == 'AC':
        index_AC.append(i)
lens = []
for i in range(24, len(index_AC)):
    lens.append(index_AC[i] - index_AC[i-24] + 2)
print(min(lens))


f = open('24.8.txt')
s = 'M' + f.readline() + 'M'
# s = 'M' + 'xxxMxMxxxMxxxMxxMxMxxxx' + 'M' #3 раза 'M' тогда разность 4 (т.к max)
index_M = []
for i in range(len(s)):
    if s[i] == 'M':
        index_M.append(i)
lens = []
for i in range(101, len(index_M)):
    lens.append(index_M[i] - index_M[i - 101] - 1)
print(max(lens))


f = open('24.9.txt')
s = f.readline()  # должно 210 раз, тогда разность 209
index_T = []
for i in range(len(s) - 1):
    if s[i] == 'T':
        index_T.append(i)
lens = []
for i in range(209, len(index_T)):
    lens.append(index_T[i] - index_T[i-209] + 1)
print(min(lens))
