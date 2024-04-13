from fnmatch import *
# for x in range(98, 10**8, 98):
#     if fnmatch(str(x), '12*678?'):
#         print(x, x // 98)
# # 12946780 132110


# for x in range(34, 10**9, 34):
#     if fnmatch(str(x), '145*51?2'):
#         print(x, x // 34)


# from fnmatch import *
# for x in range(123, int('FFFFFF', 16)+1, 123):
#     if fnmatch(hex(x)[2:], 'f5*1?4'):
#         print(hex(x)[2:], x // 123)
# # f5a1d4 130876
# # f5b134 130908


# from fnmatch import *
# prime = [2, 3, 5, 7]
# fib = [0, 1, 1, 2, 3, 5, 8]
# for x in range(534, 10**8, 534):
#     if int(str(x)[2]) in prime and int(str(x)[3]) in fib and fnmatch(str(x), '15??0?8'):
#         print(x, x // 534)
# # 1555008 2912
# # 1571028 2942




# f = open('24 (2).txt')
# s = f.readline()
# s = s.replace('M', 'U')
# s = s.replace('S', 'U')
# s = s.replace('UU', 'U U')
# s = s.replace('UU', 'U U')
# s = s.split(' ')
# print(len(max(s, key=len)))


# f = open('24.6 (3).txt')
# s = f.readline()
# index_xz = []
# for i in range(len(s)-1):
#     if s[i:i+2] == 'XZ':
#         index_xz.append(i)
# lens = []
# for i in range(28, len(index_xz)):
#     lens.append(index_xz[i] - index_xz[i-28] + 2)
# print(min(lens))


# f = open('24.1_eJcm4Bt (1).txt')
# s = f.readline()
# index_o = []
# for i in range(len(s)):
#     if s[i] == 'O':
#         index_o.append(i)
# lens = []
# for i in range(151, len(index_o)):
#     lens.append(index_o[i] - index_o[i-151] - 1)
# print(max(lens))


# f = open('24.2_OBzavDP.txt')
# s = f.readline()
# index_K = []
# for i in range(len(s)-1):
#     if s[i] == 'K':
#         index_K.append(i)
# lens = []
# for i in range(309, len(index_K)):
#     lens.append(index_K[i] - index_K[i-309] + 1)
# print(min(lens))



from fnmatch import *
for x in range(666, 10**9+1, 666):
    if fnmatch(str(x), '18*628?'):
        print(x, x // 666)

# for i in range(666, 10**9 + 1, 666):
#
#     if str(i)[:2] == "18" and str(i)[3:6] == "628":
#
#         print(i, i // 666)