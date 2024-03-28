f = open('26.web_2.txt')
vmestimost, n = map(int, f.readline().split())
gruzi = []
for s in f:
    gruzi.append(int(s))
gruzi.sort()
podochel = []
cnt = 0
for gruz in gruzi:
    if sum(podochel) + gruz <= vmestimost:
        podochel.append(gruz)
    elif sum(podochel[:-1]) + gruz <= vmestimost:
        del podochel[-1]
        podochel.append(gruz)
    else:
        cnt += 1
print(len(podochel), cnt)
#304 475
