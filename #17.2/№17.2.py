# f = open('17.1 (1).txt')
# a = []
# for s in f:
#     a.append(int(s))
# sum_troyki = []
# for i in range(len(a) - 2):
#     if (a[i] > 0 or a[i+1] > 0 or a[i+2] > 0):
#         sum_troyki.append(a[i] + a[i+1] + a[i+2])
# print(len(sum_troyki), min(sum_troyki))


# f = open('17.2 (1).txt')
# a = [int(s) for s in f]
# chet = []
# for x in a:
#     if x % 2 == 0:
#         chet.append(x)
# sr_arifm = sum(chet) / len(chet)
# sum_pari = []
# for i in range(len(a) - 1):
#     if (((a[i] % 9 == 0) and (a[i+1] % 9 != 0) or
#         (a[i] % 9 != 0) and (a[i+1] % 9 == 0)) and
#         (a[i] < sr_arifm or a[i+1] < sr_arifm)):
#         sum_pari.append(a[i]+a[i+1])
# print(len(sum_pari), max(sum_pari))


f = open('17.3 (1).txt')
a = [int(s) for s in f]
a6 = []
for x in a:
    if str(x)[-1] == '6':
        a6.append(x)
max6 = max(a6)
sum_pari = []
for i in range(len(a)-1):
    if (((a[i] % 10 == 6 and a[i+1] % 10 != 6) or
        (a[i] % 10 != 6 and a[i+1] % 10 == 6)) and
        (a[i]**2 + a[i+1]**2) < max6**2):
        sum_pari.append(a[i]**2 + a[i+1]**2)
print(len(sum_pari), max(sum_pari))