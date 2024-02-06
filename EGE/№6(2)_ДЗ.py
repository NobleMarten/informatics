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