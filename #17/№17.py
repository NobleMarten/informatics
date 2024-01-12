# f = open(r'C:\Users\user\PycharmProjects\informatics\#17\17.1.txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_pari = []
# for i in range(0, len(a)-1):
#     if a[i] % 11 == 0 and a[i + 1] % 11 == 0:
#         sum_pari.append(a[i] + a[i+1])
# print(len(sum_pari), min(sum_pari))
# # 85 -19613



# f = open('17.2.txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_pari = []
# for i in range(len(a)-1):
#     if a[i] > 1234 or a[i+1] > 1234:
#         sum_pari.append(a[i]**2 + a[i+1]**2)
# print(len(sum_pari), max(sum_pari))
# # 6868 196147530


# f = open('17.3.txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_pari = []
# for i in range(len(a)-1):
#     if (a[i] * a[i+1]) % 74 == 0:
#         sum_pari.append(a[i] + a[i+1])
# print(len(sum_pari), max(sum_pari))
# # 406 19546


# f = open('17.4.txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_pari = []
# for i in range(len(a)-1):
#     if (str(a[i])[-1] == str(a[i+1])[-1] and
#             str(a[i])[-1] in '13579'):
#     # if (abs(a[i]) % 10 == abs(a[i+1]) % 10) and (a[i] % 10) % 2 != 0:
#         sum_pari.append(abs(a[i]) + abs(a[i+1]))
# print(len(sum_pari), max(sum_pari))
# # 451 19510



# f = open('17.5.txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_pari = []
# for i in range(len(a) - 1):
#     if ((a[i] > 0 and a[i]**(1/3) % 1 == 0) or
#             (a[i+1] > 0 and a[i+1]**(1/3) % 1 == 0)):
#         sum_pari.append(a[i] + a[i+1])
# print(len(sum_pari), max(sum_pari))
# # 4 3811