# from turtle import *
# pen()
# k = 10
# tracer(0) # чтобы рисунок появился моментально
# # speed(10000)
# for i in range(124):
#     right(30) # градусы не умножаются
#     forward(5*k)
# done() # чтобы рисунок не пропал
# #12

# from turtle import *
# pen()
# tracer(0)
# k = 10
# for i in range(24):
#     right(60)
#     forward(10*k)
#     left(30)
#     backward(20*k)
# done()
# #24

# from turtle import *
# pen()
# tracer(0)
# k = 20
# for i in range(13):
#     forward(6*k)
#     right(90)
# penup() # поднять хвост(чтобы между точками не было линий)
# # done() #6**2=36
# for x in range(0, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(5)
# done()

# from turtle import *
# pen()
# tracer(0)
# k = 20
# right(45)
# forward(5*k)
# for i in range(7):
#     right(45)
#     forward(12*k)
#     right(135)
#     forward(6*k)
# penup()
# for x in range(-10, 10):
#     for y in range(-20, 10):
#         setpos(x*k, y*k)
#         dot(5)
# done()


# 13 задача

# треугольник равносторонний
# Y = kx
# k = tg()
# y = tg(30)x
# y = tg(150)x + 99

# from math import *
# cnt = 0
# for x in range(0, 1000):
#     for y in range(0, 1000):
#         if x > 0 and y > tan(radians(30))*x and y < tan(radians(150))*x + 99:
#             cnt += 1
# print(cnt)

# 14 задание

# x < 0
# y > tg(150)x
# y < tg(30)x +100

# cnt = 0
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if x < 0 and y > tan(radians(150))*x and y < tan(radians(30))*x + 100:
#             cnt += 1
# print(cnt)


# from turtle import *
# pen()
# speed(1000)
# k = 20
# for i in range(30):
#     forward(4*k)
#     right(120)
# penup()
# for x in range(-5, 10):
#     for y in range(0, 10):
#      setpos(x*k, y*k)
#      dot(5)
# done()


from math import *
cnt = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if x > 0 and y > tan(radians(30))*x and y < tan(radians(150))*x + 111:
            cnt += 1
print(cnt)
