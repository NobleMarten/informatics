# f = open('26.1(1).txt')
# vmestimost, n = map(int, f.readline().split())
# gruzi = []
# podoshel = []
# for s in f:
#     gruzi.append((int(s)))
# gruzi.sort()
# # print(sum(gruzi[0:4413]))
# # print(vmestimost-sum(gruzi[0:4412]))
# for gruz in gruzi:
#     if sum(podoshel) + gruz <= vmestimost:
#         podoshel.append(gruz)
#     elif sum(podoshel[:-1]) + gruz <= vmestimost:
#         del podoshel[-1]
#         podoshel.append(gruz)
# print(len(podoshel), max(podoshel))


# f = open('26.2 (1).txt')
# vmestimost, n = map(int, f.readline().split())
# gruzi = []
# for s in f:
#     gruzi.append(int(s))
# gruzi.sort()
# # print(sum(gruzi[:314]))
# # print(314 - 0) # 1 ответ
# # print(vmestimost - sum(gruzi[:313]))
# # print(gruzi.index(107))
# # print(len(gruzi[537:])) # 2
# podochel = []
# cnt = 0
# for gruz in gruzi:
#     if sum(podochel) + gruz <= vmestimost:
#         podochel.append(gruz)
#     elif sum(podochel[:-1]) + gruz <= vmestimost:
#         del podochel[-1]
#         podochel.append(gruz)
#     else:
#         cnt += 1
# print(len(podochel), cnt)


# f = open('26.3 (1).txt')
# n = int(f.readline())
# tovari = []
# tovari120 = []
# for s in f:
#     tovari.append(int(s))
#     if int(s) > 120:
#         tovari120.append(int(s))
# tovari120.sort()
# skidka = sum(tovari120[:len(tovari120)//2]) * 0.25
# print(sum(tovari) - skidka)
# print(max(tovari120[:len(tovari120)//2]))


# f = open('26.4 (1).txt')
# n = int(f.readline())
# tovari = []
# for s in f:
#     tovari.append(int(s))
# tovari.sort(reverse=True)
# # #(n//4) # на сколько скидка
# skidka = sum(tovari[:n//4])*0.5
# print(sum(tovari) - skidka)
# tovari.sort()
# skidka = sum(tovari[:n//4])*0.5
# print(sum(tovari) - skidka)


# f = open('26.5 (1).txt')
# n = int(f.readline())
# tovari = []
# for s in f:
#     tovari.append(int(s))
# tovari.sort(reverse=True)
# print(sum(tovari) - sum(tovari[:n//3]))
# summ = sum(tovari)
# for i in range(2, len(tovari), 3):
#     summ -= tovari[i]
# print(summ)



#ДЗ



# f = open('26.web_1.txt')
# vmestimost, n = map(int, f.readline().split())
# gruzi = []
# podoshel = []
# for s in f:
#     gruzi.append((int(s)))
# gruzi.sort()
# for gruz in gruzi:
#     if sum(podoshel) + gruz <= vmestimost:
#         podoshel.append(gruz)
#     elif sum(podoshel[:-1]) + gruz <= vmestimost:
#         del podoshel[-1]
#         podoshel.append(gruz)
# print(len(podoshel), max(podoshel))

# f = open('26.web_2.txt')
# vmestimost, n = map(int, f.readline().split())
# gruzi = []
# for s in f:
#     gruzi.append(int(s))
# gruzi.sort()
# podochel = []
# cnt = 0
# for gruz in gruzi:
#     if sum(podochel) + gruz <= vmestimost:
#         podochel.append(gruz)
#     elif sum(podochel[:-1]) + gruz <= vmestimost:
#         del podochel[-1]
#         podochel.append(gruz)
#     else:
#         cnt += 1
# print(len(podochel), cnt)


# f = open('26.web_5 (1).txt')
# n = int(f.readline())
# tovari = []
# tovari120 = []
# for s in f:
#     tovari.append(int(s))
#     if int(s) > 120:
#         tovari120.append(int(s))
# tovari120.sort()
# skidka = sum(tovari120[:len(tovari120)//2]) * 0.25
# print(sum(tovari) - skidka)
# print(max(tovari120[:len(tovari120)//2]))


f = open('26.2_5xUhRUh.txt')
n = int(f.readline())
tovari = []
for s in f:
    tovari.append(int(s))
tovari.sort(reverse=True)
print(sum(tovari) - sum(tovari[:n//3]))
summ = sum(tovari)
for i in range(2, len(tovari), 3):
    summ -= tovari[i]
print(summ)