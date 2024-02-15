# from turtle import *
# tracer(0)
# k = 20
# pendown()
# left(90)
# for i in range(2):
#     forward(15*k)
#     left(90)
#     forward(10*k)
#     left(90)
# penup()
# backward(5*k)
# right(90)
# backward(4*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(44*k)
#     right(90)
#     forward(12*k)
#     right(90)
# penup()
# for x in range(-20, 20):
#     for y in range(-20, 50):
#         setpos(x*k, y*k)
#         dot(3)
# done()
# print(16*11 + 45*13 - 16*5)


# from turtle import *
# tracer(0)
# left(90)
# k = 20
# pendown()
# for i in range(6):
#     forward(8*k)
#     right(90)
# penup()
# forward(1*k)
# right(90)
# forward(3*k)
# left(90)
# pendown()
# for i in range(12):
#     forward(60*k)
#     right(90)
#     forward(90*k)
#     right(90)
# penup()
# for x in range(-10, 100):
#     for y in range(-10, 100):
#         setpos(x*k, y*k)
#         dot(3)
# print(6*8)
# done()


# from math import *
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if (x > 0 and y > tan(radians(30))*x and y < tan(radians(150))*x + 99):
#             cnt += 1
# print(cnt)



#ДЗ



# from turtle import *
# tracer(0)
# left(90)
# k = 20
# pendown()
# for i in range(6):
#     forward(6*k)
#     right(90)
# penup()
# forward(3*k)
# right(270)
# forward(5*k)
# right(90)
# pendown()
# for i in range(6):
#     forward(11*k)
#     right(90)
#     forward(8*k)
#     right(90)
# penup()
# for x in range(-15, 15):
#     for y in range(-15, 15):
#         setpos(x*k, y*k)
#         dot(3)
# done()


# from turtle import *
# tracer(0)
# left(90)
# k = 20
# pendown()
# for i in range(8):
#     forward(7*k)
#     right(90)
# penup()
# forward(2*k)
# right(90)
# forward(3*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(6*k)
#     right(90)
#     forward(8*k)
#     right(90)
# penup()
# for x in range(-10, 15):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(3)
# done()


# from math import *
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if x > 0 and y > tan(radians(30))*x and y < tan(radians(150))*x+101:
#             cnt += 1
# print(cnt)


cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y < x + 15*(2**(1/2)) and y > x - 15*(2**(1/2)) and y > -x - 15*(2**(1/2)) and y < -x:
            cnt += 1
print(cnt)