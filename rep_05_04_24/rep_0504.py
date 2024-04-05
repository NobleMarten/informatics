f = open('24_5_vauct9E.txt')
a = [s for s in f]
alph = 'abcdefghijklmnopqrstuvwxyz'
max_r = 0
for i in range(len(a)):
    if a[i].count('g') < 25:
        for j in range(0, 26):
            t = a[i]
            t = t.split(alph[j])
            for h in range(len(t)):
                max_r = max(max_r, len(t[h]))
print(max_r)