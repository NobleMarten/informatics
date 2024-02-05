f = open('24_8.txt')
s = f.readline()
a = s.split('C')
res = []
for i in range(len(a)-1):
    res.append(a[i] + 'C' + a[i+1])
print(len(max(res, key=len)))
