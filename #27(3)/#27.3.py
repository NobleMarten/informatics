# def is_special(x):
#     if x < 0:
#         x0 = abs(x)
#         digit7 = []
#         while x0 > 0:
#             digit7.append(x0 % 7)
#             x0 = x0 // 7
#         if digit7[-1] == 5:
#             return True
#     return False
#
# f = open('27.1.A (4).txt')
# n, k = map(int, f.readline().split())
# # a = [int(s) for s in f]
# # a_special = [is_special(x) for x in a]
# # res = []
# # for left in range(n):
# #     for right in range(left, n):
# #         if sum(a_special[left:right + 1]) % k == 0:
# #             res.append(sum(a_special[left:right + 1]))
# # print(max(res)
# summ_special_cnt = [0]*k
# res = []
# # summ_special_cnt[2] - сумма в которой 2 особых числа
# summ, cnt_special = 0, 0
# for s in f:
#     summ += int(s)
#     if is_special(int(s)):
#         cnt_special += 1
#     if cnt_special % k == 0:
#         res.append(summ)
#     if summ_special_cnt[cnt_special % k] != 0:
#         res.append(summ - summ_special_cnt[summ % k])
#     else:
#         summ_special_cnt[cnt_special % k] = min(summ, summ_special_cnt[cnt_special % k])
# print(max(res))




# f = open('27.2.A (3).txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for left in range(n):
#     for right in range(left, n):
#         if sum(a[left: right + 1]) % 1001 == 0:
#             res.append(sum(a[left: right + 1]) % 1001)
# print(len(res))



# f = open('27.2.B (2).txt')
# n = int(f.readline())
# cnt_summ_ost = [0]*1001
# cnt = 0
# summ = 0
# for s in f:
#     summ += int(s)
#     if summ % 1001 == 0:
#         cnt += 1
#     cnt += cnt_summ_ost[summ % 1001]
#     cnt_summ_ost[summ % 1001] += 1
# print(cnt)



# f = open('27.3.A (4).txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# is_cr9 = [x % 9 == 0 for x in a]
# is_cr11 = [x % 11 == 0 for x in a]
# res = []
# for left in range(n):
#     for right in range(left, n):
#         if sum(is_cr9[left:right + 1]) == sum(is_cr11[left:right + 1]):
#             res.append(sum(a[left:right + 1]))
# print(max(res))


f = open('27.3.B (2).txt')
n = int(f.readline())
summ, cnt_kr9, cnt_kr11 = 0, 0, 0
res = []
ost = {}
for s in f:
    summ += int(s)
    if int(s) % 9 == 0:
        cnt_kr9 += 1
    if int(s) % 11 == 0:
        cnt_kr11 += 1
    if cnt_kr9 == cnt_kr11:
        res.append(summ)
    elif cnt_kr9 - cnt_kr11 in ost:
        res.append(summ - ost[cnt_kr9 - cnt_kr11])
    else:
        ost[cnt_kr9 - cnt_kr11] = summ
print(max(res))