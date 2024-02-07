# from turtle import *
# pendown()
# left(90)
# k = 15
# for i in range(12):
#     right(60)
#     forward(5 * k)
#     left(30)
#     backward(5 * k)
# done()


# from turtle import *
# # tracer(0)
# pendown()
# left(90)
# k = 15
# for i in range(5):
#     forward(10*k)
#     right(144)
#     forward(10*k)
#     right(72)
# done()


from turtle import *
tracer(0)
pendown()
left(90)
k = 40
for i in range(12):
    forward(5 * k)
    right(120)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(4)
done()


# from math import *
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if (x > 0 and y > tan(radians(30))*x and y < tan(radians(150))*x + 137):
#             cnt += 1
# print(cnt)

# from turtle import *
# speed(0)
# left(90)
# k = 50
# pendown()
# begin_fill()
# for i in range(21):
#     forward(137*k)
#     right(120)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#       if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
#           cnt += 1
# print(cnt)
# done()


# from turtle import *
# speed(0)
# left(90)
# pendown()
# k = 20
# left(90)
# for i in range(3):
#     right(45)
#     forward(10*k)
#     right(45)
# right(315)
# forward(10*k)
# for i in range(2):
#     right(90)
#     forward(10*k)
# done()

# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if (y < x + 10*(2**(1/2)) and y > x - 10*(2**(1/2)) and y > -x - 10*(2**(1/2)) and y < -x):
#             cnt += 1
# print(cnt)
