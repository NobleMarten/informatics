# 2
from fnmatch import *
from itertools import *
from turtle import *
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not (y))) <= ((x and w) == (z and (not (w))))
                if F == 0:
                    print(x, y, z, w)
# x y z w
# 0 1 1 0
# 1 0 1 0
# 1 0 1 1
# wzyx


# 5
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n2.count('1') > n2.count('0'):
        n2 += '1'
    if n2.count('1') == n2.count('0') or n2.count('0') > n2.count('1'):
        n2 += '0'
    R = int(n2, 2)
    if R > 100:
        print(R)


# 6
left(90)
tracer(0)
k = 20
pendown()
for i in range(14):
    right(60)
    forward(2*k)
    right(60)
    forward(2*k)
    right(270)
penup()
for x in range(-5, 10):
    for y in range(-20, 10):
        setpos(x*k, y*k)
        dot(4)
forward(1*k)
done()


# 8
numb = 0
for i in product('АОУ', repeat=5):
    numb += 1
    print(numb, i)
    if i == ('У', 'А', 'У', 'А', 'У'):
        print(numb)


# 9
f = open('9')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    povt = [x for x in a if a.count(x) > 1]
    ne_povt = [x for x in a if a.count(x) == 1]
    if len(ne_povt) == 5 and 3 * (max(a) + min(a)) <= 2 * (a[1] + a[2] + a[3]):
        cnt += 1
print(cnt)


# 12
s = '1' + '9' * 100
while '19' in s or '299' in s or '3999' in s:
    if '19' in s:
        s = s.replace('19', '2', 1)
    if '299' in s:
        s = s.replace('299', '3', 1)
    if '3999' in s:
        s = s.replace('3999', '1', 1)
print(s)


# 14
s = 4**8 + 2**8 - 8
s2 = bin(s)[2:]
print(s2.count('1'))
print(s2)


# 15
p = list(range(22, 73))
q = list(range(42, 103))
A = []
for x in range(1, 1000):
    if ((not ((not (x in A)) and (x in p))) or (x in q)) == False:
        A.append(x)
print(A)


# 16
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return f(n-2) * (n-1)


print(f(7))


# 17
f = open('17 (3).txt')
a = [int(s) for s in f]
troiki = []
max_15 = []
for i in range(len(a)):
    if str(a[i])[-2:] == '15':
        max_15.append(a[i])
max15 = max(max_15)
for i in range(len(a)-2):
    if (len([True for j in range(3) if len(str(abs(a[i+j]))) == 4]) == 1) and ((a[i]+a[i+1]+a[i+2]) >= max15):
        troiki.append(a[i]+a[i+1]+a[i+2])
print(len(troiki), max(troiki))


# 23
def task23(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > end:
        return task23(start-2, end) + task23(start-5, end)


print(task23(23, 2))


# 25
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '3?1*57'):
        print(x, x // 2023)
