f = open('26.web_1.txt')
vmestimost, n = map(int, f.readline().split())
gruzi = []
podoshel = []
for s in f:
    gruzi.append((int(s)))
gruzi.sort()
for gruz in gruzi:
    if sum(podoshel) + gruz <= vmestimost:
        podoshel.append(gruz)
    elif sum(podoshel[:-1]) + gruz <= vmestimost:
        del podoshel[-1]
        podoshel.append(gruz)
print(len(podoshel), max(podoshel))
#504 89