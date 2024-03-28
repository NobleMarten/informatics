f = open('26.web_5 (1).txt')
n = int(f.readline())
tovari = []
tovari120 = []
for s in f:
    tovari.append(int(s))
    if int(s) > 120:
        tovari120.append(int(s))
tovari120.sort()
skidka = sum(tovari120[:len(tovari120)//2]) * 0.25
print(sum(tovari) - skidka)
print(max(tovari120[:len(tovari120)//2]))
# 446166 522