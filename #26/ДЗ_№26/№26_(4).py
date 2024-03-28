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
#2192564 3317498