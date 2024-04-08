f = open('24.6.txt')
s = f.readline()
s = s.replace('ANT', 'AN NT')
s = s.replace('AN', '*')
s = s.replace('NT', '*')
for i in range(1000):
    if '*'*i in s:
        print(i)
#answer = 10