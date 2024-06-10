# from turtle import *
# left(90)
# k = 20
# x = 5
# pendown()
# tracer(0)
# for i in range(4):
#     forward(x*k)
#     right(90)
#     forward(x*k)
#     left(90)
#     forward(x*k)
#     right(90)
# penup()
# for x in range(-10, 20):
#     for y in range(-10, 11):
#         setpos(x*k, y*k)
#         dot(4)
# done()


# f = open('24 (7).txt')
# s = f.readline()
# a = [0]*26
# for i in range(len(s)-1):
#     if s[i] == 'A':
#         a[ord(s[i+1])-65] += 1
# print(a) #G


f = open('24 (8).txt')
s = f.readline()
cnt = 0
s = s.split('E')
for i in range(len(s)):
    if len(s[i]) > 10 and 'F' not in s[i]:
        cnt += 1
print(cnt) #8917
print(len(s[0]), len(s[-1]))