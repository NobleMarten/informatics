#2
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(x)) and (not(y))) or (y == z) or (not(w))
                if F == 0:
                    print(x, y, z, w)
# x y z w
# 0 1 0 1
# 1 0 1 1
# 1 1 0 1
import sys
#5
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n2.count('0') == n2.count('1'):
        n2 += n2[-1]
    if n2.count('0') > n2.count('1'):
        n2 += '1'
    if n2.count('0') < n2.count('1'):
        n2 += '0'
    if n2.count('0') == n2.count('1'):
        n2 += n2[-1]
    if n2.count('0') > n2.count('1'):
        n2 += '1'
    if n2.count('0') < n2.count('1'):
        n2 += '0'
    if n2.count('0') == n2.count('1'):
        n2 += n2[-1]
    if n2.count('0') > n2.count('1'):
        n2 += '1'
    if n2.count('0') < n2.count('1'):
        n2 += '0'
    r = int(n2, 2)
    if r % 4 == 0:
        print(n)


#6
from turtle import *
left(90)
pendown()
k = 20
x = 2
tracer(0)
for i in range(4):
    forward(x*k)
    right(90)
    forward(x * k)
    left(90)
    forward(x * k)
    right(90)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(4)
done()


#8
from itertools import *
cnt = 0
for i in product('СВЕТЛАН', repeat=8):
    s = ''.join(i)
    if i.count('А') == 2 and i.count('С') == 1 and i.count('В') == 1 and i.count('Е') == 1 and \
            i.count('Т') == 1 and i.count('Л') == 1 and i.count('Н') == 1 and 'АА' not in s:
        print(s)
        cnt += 1
print(cnt)


#9
f = open('9')
cnt = 0
# s = '37	83 24 19 37	41'
for s in f:
    a = list(map(int, s.split()))
    povt = [x for x in a if a.count(x) > 1]
    ne_povt = [x for x in a if a.count(x) == 1]
    if len(set(povt)) > 0 and len(set(ne_povt)) > 0 and ((sum(ne_povt) / len(ne_povt)) > (sum(povt) / len(povt))):
        cnt += 1
print(cnt)


#12
s = '1'*99
while '111' in s:
    s = s.replace('111', '22', 1)
    s = s.replace('222', '11', 1)
print(s)


#14
for x in '0123456789ABCDEFGHI':
    if (int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)) % 18 == 0:
        print(x, (int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)) // 18)


#15
for A in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x < A) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= A))) == False:
                break
        if (((x < A) <= (x ** 2 < 81)) and ((y ** 2 <= 36) <= (y <= A))) == False:
            break
    else:
        print(A)


#16
from sys import *
sys.setrecursionlimit(3000)
def f(n):
    if n < 7:
        return 7
    if n >= 7:
        return 2*n + f(n-1)
print(f(2024)-f(2022))


#17
f = open('1_17.txt')
a = [int(s) for s in f]
pari = []
max_p = []
for i in range(len(a)):
    if 9 < a[i] < 100:
        max_p.append(a[i])
max_d = max(max_p)
for i in range(len(a)-1):
    if (((9 < a[i] < 100) and (len(str(a[i+1])) != 2)) or ((9 < a[i+1] < 100) and (len(str(a[i])) != 2))) and \
            ((a[i]+a[i+1]) % max_d == 0):
        pari.append(a[i]+a[i+1])
print(len(pari), max(pari))


#19-21
# (x+1, s) (x+s, s) (x, s+1) (x, s+x)
def win1(x, s):
    return (x+s) > 75 and (x+1+s) >= 75 or (x+s+s) >= 75 or (x+s+x) >= 75
def los1(x, s):
    return (not(win1(x, s))) and win1(x+1, s) and win1(x+s, s) and win1(x, s+1) and win1(x, s+x)
def win2(x, s):
    return los1(x+1, s) or los1(x+s, s) or los1(x, s+1) or los1(x, s+x)
def los12(x, s):
    return ((win1(x+1, s) or win2(x+1, s)) and (win1(x+s, s) or win2(x+s, s)) and \
        (win1(x, s+1) or win2(x, s+1)) and (win1(x, s+x) or win2(x, s+x))) and\
        (win2(x+1, s) or win2(x+s, s) or win2(x, s+1) or win2(x, s+x))

x = 7
for s in range(1, 68):
    if win1(x+1, s) or win1(x+s, s) or win1(x, s+1) or win1(x, s+x):
        print(s)
for s in range(1, 68):
    if los12(x, s):
        print(s)


#24
f = open('24 (3).txt')
s = f.readline()
s = s.replace('KL', '*')
s = s.replace('LK', '*')
s = s.split('*')
print(len(max(s, key=len))+2)

#28
f = open('24 (4).txt')
s = f.readline()
s = s.replace('XZZY', '*')
s = s.split('*')
print(len(max(s, key=len))+6)

#25
from collections import *
f = open('24 (5).txt')
s = f.readline()
s = s.split('G')
max_len = []
for i in range(len(s)):
    max_len.append([len(s[i]), s[i]])
print(max_len)
a = 'YKSPFJCTUVVBVDEHOVNPUJNSKQKLAVRBVPYMQQFAZIKKOCOHYHZUQWISMZIDULBPGRJNAMOSQARQCFVFWHOLRBYLPFNPTAAKCIHVJZP'
c = Counter(a)
print(c.most_common(1)[0][0])


#23
def task23(start, end):
    if start > end:
        return 0
    if start == 6:
        return 0
    if start == 12:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start*2, end) + task23(start+3, end)
print(task23(3, 16))


#29
def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
cnt = 0
for i in range(2422000, 2422081):
    if is_prime(i) == True:
        print(i)
        cnt += 1
print(cnt)


#32
f = open('27A_59854.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(s) for s in f]
pari = []
for i in range(len(a)):
    for j in range(i+k, len(a)):
        pari.append(a[i]*a[j])
print(min(pari))


#33
f = open('27-A_demo.txt')
n = int(f.readline())
a = []
max_e = []
for s in f:
    a.append(list(map(int, s.split())))
print(a)
for i in range(len(a)):
    max_e.append(max(a[i]))
print(sum(max_e)-5841+5627)