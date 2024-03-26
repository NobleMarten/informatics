# f = open('17.1.txt')
# a = [int(s) for s in f]
# pari = []
# min_a = min(a)
# for i in range(len(a)-1):
#     if (a[i] % 123 == min_a) or (a[i+1] % 123 == min_a):
#         pari.append(a[i]+a[i+1])
# print(len(pari), max(pari))


# f = open('17.2.txt')
# a = [int(s) for s in f]
# pari = []
# ne_chet = [x for x in a if x % 2 != 0]
# sr_a = sum(ne_chet) / len(ne_chet) #553.2192369693713
# for i in range(len(a)-1):
#     if (a[i] % 7 == 0 and a[i+1] % 7 != 0 and a[i+1] > sr_a) or (a[i+1] % 7 == 0 and a[i] % 7 != 0 and a[i] > sr_a):
#         pari.append(a[i]+a[i+1])
# print(len(pari), min(pari))


# f = open('17.3.txt')
# a = [int(s) for s in f]
# pari = []
# max_a = max(a)
# for i in range(len(a)-1):
#     if ((str(a[i])[-1] == '6' and str(a[i+1])[-1] != '6' and ((a[i]*a[i] + a[i+1]*a[i+1]) < max_a*max_a)) or
#             (str(a[i+1])[-1] == '6' and str(a[i])[-1] != '6' and ((a[i]*a[i] + a[i+1]*a[i+1]) < max_a*max_a))):
#         pari.append(a[i]**2+a[i+1]**2)
# print(len(pari), max(pari))


# f = open('17.4.txt')
# a = [int(s) for s in f]
# pari = []
# min_a = []
# for x in a:
#     if 9 < x < 100:
#         min_a.append(x)
# min_dv = min(min_a) #12
# for i in range(len(a)-1):
#     if ((9 < a[i] < 100) and (9 < a[i+1] < 100)) and ((a[i]+a[i+1]) % min_dv == 0):
#         pari.append(a[i]+a[i+1])
# print(len(pari), max(pari))


# f = open('17.5.txt')
# a = [int(s) for s in f]
# troiki = []
# max_13 = []
# for x in a:
#     if str(x)[-2:] == '13':
#         max_13.append(x)
# max13 = max(max_13)
# for i in range(len(a)-2):
#     if (((9999 < abs(a[i]) < 100000) and (9999 < abs(a[i+1]) < 100000) and (9999 > abs(a[i+2]) or a[i+2] > 100000) and (a[i]+a[i+1]+a[i+2] <= max13)) or
#         ((9999 < abs(a[i]) < 100000) and (9999 < abs(a[i+2]) < 100000) and (9999 > abs(a[i+1]) or a[i+1] > 100000) and (a[i]+a[i+1]+a[i+2] <= max13)) or
#         ((9999 < abs(a[i+1]) < 100000) and (9999 < abs(a[i+2]) < 100000) and (9999 > abs(a[i]) or a[i] > 100000) and (a[i]+a[i+1]+a[i+2] <= max13))):
#         troiki.append(a[i]+a[i+1]+a[i+2])
# print(len(troiki), max(troiki))


f = open('17.6.txt')
a = [int(s) for s in f]
troiki = []
min_600 = []
for x in a:
    if str(x)[-3:] == '600':
        min_600.append(x)
min600 = min(min_600)
for i in range(len(a)-2):
    if (((9999 < abs(a[i]) < 100000) and (9999 < abs(a[i+1]) < 100000) and (9999 > abs(a[i+2]) or a[i+2] > 100000) and (a[i]+a[i+1]+a[i+2] >= min600)) or
        ((9999 < abs(a[i]) < 100000) and (9999 < abs(a[i+2]) < 100000) and (9999 > abs(a[i+1]) or a[i+1] > 100000) and (a[i]+a[i+1]+a[i+2] >= min600)) or
        ((9999 < abs(a[i+1]) < 100000) and (9999 < abs(a[i+2]) < 100000) and (9999 > abs(a[i]) or a[i] > 100000) and (a[i]+a[i+1]+a[i+2] >= min600))):
        troiki.append(a[i]+a[i+1]+a[i+2])
print(len(troiki), min(troiki))