# from turtle import *
# left(90)
# k = 10 #переменная, отвечающая за масштаб
# pendown()
# for i in range(102):
#     forward(2 * k)
#     right(36)
#     forward(3 * k)
# done()


# from turtle import *
# left(90)
# k = 10
# pendown()
# for i in range(124):
#     right(30)
#     forward(5 * k)
# done()


# from turtle import *
# left(90)
# k = 10
# pendown()
# for i in range(24):
#     right(60)
#     forward(10 * k)
#     left(30)
#     backward(20)
# done()


# from turtle import *
# tracer(0)
# left(90)
# k = 20
# pendown()
# for i in range(13):
#     forward(7*k)
#     right(90)
# penup()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(4)
# done()


# from turtle import *
# tracer(0)
# left(90)
# k = 20
# pendown()
# right(45)
# forward(5*k)
# for i in range(7):
#     right(45)
#     forward(16*k)
#     right(135)
#     forward(8*k)
# penup()
# for x in range(-10, 20):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(5)
# done()


# from turtle import *
# tracer(0)
# left(90)
# k = 40
# pendown()
# for i in range(130):
#     forward(7*k)
#     right(120)
# penup()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(4)
# done()






# from turtle import *
# pendown()
# k = 20
# begin_fill()
# for i in range(6):
#     forward(3 * k)
#     left(60)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ): #список (5, ) порказывает, что на
#     # этих координатах есть заливка (то что нам нужно)
#             cnt += 1
# print(cnt)
# done() #24



# from turtle import * #автоподбор
# tracer(0)
# pendown()
# k = 50
# left(90)
# begin_fill()
# for i in range(123):
#     forward(111*k)
#     right(120)
# canvas = getcanvas()
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
#             cnt += 1
# print(cnt)
# end_fill()
# done()

# from math import * #математика
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if x > 0 and \
#             y > tan(radians(30))*x and \
#                 y < tan(radians(150))*x + 111:
#             cnt += 1
# print(cnt)


# from math import *
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if x > 0 and \
#             y > tan(radians(30))*x and \
#             y < tan(radians(150))*x + 123:
#             cnt += 1
# print(cnt)


# from turtle import *
# speed(0)
# pendown()
# k = 10
# begin_fill()
# for i in range(2):
#     right(90)
#     forward(120*k)
#     right(90)
#     forward(14*k)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
#             cnt += 1
# print(cnt)
# done()


# from turtle import *
# speed(0)
# pendown()
# k = 10
# begin_fill()
# right(90)
# for i in range(3):
#     right(45)
#     forward(12*k)
#     right(45)
# right(315)
# forward(12*k)
# for i in range(2):
#     right(90)
#     forward(12*k)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
#             cnt += 1
# print(cnt)
# done()

# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if (y < x + 12*(2**(1/2)) and y > x - 12*(2**(1/2)) and y > -x - 12*(2**(1/2)) and y < -x):
#             cnt += 1
#     print(cnt) #264


