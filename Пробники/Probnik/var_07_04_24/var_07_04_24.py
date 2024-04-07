from itertools import *
from turtle import *
# 2
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not (y))) or (y == z) or (not (w))
                if F == 0:
                    print(x, y, z, w)
# x y z w
# 0 0 1 1
# 0 1 0 1
# 1 1 0 1
# wzyx


# 5
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    r = int(n2, 2)
    if r > 97:
        print(n)


# 6
left(90)
pendown()
tracer(0)
k = 30
for i in range(4):
    forward(12*k)
    right(90)
right(30)
for i in range(3):
    forward(8*k)
    right(60)
    forward(8*k)
    right(120)
penup()
for x in range(-10, 15):
    for y in range(-10, 15):
        setpos(x*k, y*k)
        dot(4)
done()


# 8
cnt = 0
for i in product('1234', repeat=5):
    if i.count('1') == 2:
        cnt += 1
print(cnt)


# 9
f = open('9')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    povt = [x for x in a if a.count(x) > 1]
    ne_povt = [x for x in a if a.count(x) == 1]
    if len(set(povt)) == 2 and len(ne_povt) == 2 and sum(set(povt)) > sum(ne_povt):
        cnt += 1
print(cnt)


# 12
s = '8'*1000
while '999' in s or '888' in s:
    if '888' in s:
        s = s.replace('888', '9', 1)
    else:
        s = s.replace('999', '8', 1)
print(s)


# 14
s = 49**10 + 7**30 - 49
cnt = 0
while s > 0:
    if s % 7 == 6:
        cnt += 1
    s = s // 7
print(cnt)


# 15
def dell(n, m):
    return n % m == 0


for A in range(1, 1000):
    for x in range(1, 1000):
        if ((not (dell(x, A))) <= (dell(x, 6) <= (not (dell(x, 4))))) == False:
            break
    else:
        print(A)


# 16
def f(n):
    if n == 1:
        return 0
    if n > 1:
        return f(n-1) + n


def g(n):
    if n == 1:
        return 1
    if n > 1:
        return g(n-1) * n


print(f(5)+g(5))


# 17
f = open('17.txt')
a = [int(s) for s in f]
pari = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]*a[j] % 10 == 0:
            pari.append(a[i]+a[j])
print(len(pari), max(pari))


# 19-21
# (x-1, s) (x//2, s) (x, s-1) (x, s//2)
def win1(x, s):
    return (x+s > 20) and (x + s - 1) <= 20 or (x + s//2) <= 20 or (x - 1 + s) <= 20 or (x//2+s) <= 20


def loss1(x, s):
    return (not (win1(x, s))) and win1(x-1, s) and win1(x//2, s) and win1(x, s-1) and win1(x, s//2)


def win2(x, s):
    return loss1(x-1, s) or loss1(x//2, s) or loss1(x, s-1) or loss1(x, s//2)


def loss12(x, s):
    return (win1(x-1, s) or win2(x-1, s)) and (win1(x//2, s) or win2(x//2, s)) and \
        (win1(x, s-1) or win2(x, s-1)) and (win1(x, s//2) or win2(x, s//2)) and \
        (win2(x - 1, s) or win2(x // 2, s) or win2(x, s - 1) or win2(x, s // 2))


x = 10
for s in range(10, 100000):
    if win1(x-1, s) or win1(x//2, s) or win1(x, s-1) or win1(x, s//2):
        print(s)
for s in range(10, 100000):
    if win2(x, s):
        print(s)
for s in range(10, 100000):
    if loss12(x, s):
        print(s)


# 23
def task23(start, end):
    if start > end or start == 26:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start+1, end) + task23(start*2+1, end)


print(task23(1, 27))
