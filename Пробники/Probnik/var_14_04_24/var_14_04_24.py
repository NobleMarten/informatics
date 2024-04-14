#2
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == (y <= z)) and (y or w)
                if F == 1:
                    print(x, y, z, w)
# x y z w
# 0 0 0 1
# 0 1 1 0
# 0 0 1 1


#5
for n in range(1, 10000):
    n2 = bin(n)[2:]
    n2 += str(int(n2.count('1')) % 2)
    n2 += str(int(n2.count('1') % 2))
    r = int(n2, 2)
    if r > 77:
        print(n)


#6
from turtle import *
left(90)
tracer(0)
pendown()
k = 40
for i in range(5):
    forward(9*k)
    right(120)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(4)
done()


#8
from itertools import *
cnt = 0
for i in permutations('ЛЕВИЙ', r=5):
    s = ''.join(i)
    if s[0] != 'Й' and 'ЕИ' not in s:
        cnt += 1
        print(s)
print(cnt)


#12
s = 54*'5' + '7'
while '722' in s or '557' in s:
    if '722' in s:
        s = s.replace('722', '57')
    else:
        s = s.replace('557', '72')
print(s)


#14
s = 6 * 343**5 + 5 * 49**7 - 50
cnt = 0
while s > 0:
    if s % 7 == 6:
        cnt += 1
    s = s // 7
print(cnt)


#15
for A in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((y + 2*x < A) or (x > 30) or (y > 20)) == False:
                break
        if ((y + 2 * x < A) or (x > 30) or (y > 20)) == False:
            break
    else:
        print(A)


#16
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + 2**(n-1)
print(f(12))


#17
f = open('17 (5).txt')
a = [int(s) for s in f]
pari = []
for i in range(len(a)-1):
    if (a[i] % 3 == 0 or a[i+1] % 3 == 0) and ((a[i]+a[i+1]) % 5 == 0):
        pari.append(a[i]+a[i+1])
print(len(pari), max(pari))


#19-21
# (x+1, s+2) (x+2, s+1) (x*2, s) (x, s*2)

def win1(x, s):
    return (x+s) > 47 and (x+1+s+2) >= 47 or (x*2+s) >= 47 or (x+s*2) >= 47
def los1(x, s):
    return (not(win1(x, s))) and win1(x+1, s+2) and win1(x+2, s+1) and win1(x*2, s) and win1(x, s*2)
def win2(x, s):
    return los1(x+1, s+2) or los1(x+2, s+1) or los1(x*2, s) or los1(x, s*2)
def los12(x, s):
    return (win1(x+1, s+2) or win2(x+1, s+2)) and (win1(x+2, s+1) or win2(x+2, s+1)) and \
        (win1(x*2, s) or win2(x*2, s)) and (win1(x, s*2) or win2(x, s*2)) and\
        (win2(x+1, s+2) or win2(x+2, s+1) or win2(x*2, s) or win2(x, s*2))

x = 10
for s in range(1, 37):
    if win1(x+1, s+2) or win1(x+2, s+1) or win1(x*2, s) or win1(x, s*2):
        print(s)
for s in range(1, 37):
    if win2(x, s):
        print(s)
for s in range(1, 37):
    if los12(x, s):
        print(s)


#23
def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+2, end) + task23(start*5, end)
print(task23(2, 50))


#27
f = open('27_A.txt')
a = [int(s) for s in f]
pari = []
for i in range(len(a)):
    for j in range(i, len(a)):
        if (a[i] - a[j]) % 2 == 0 and (a[i] % 17 == 0 or a[j] % 17 == 0):
            pari.append([(a[i]+a[j]), a[i], a[j]])
print(max(pari))