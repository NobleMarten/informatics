# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (z and (not(x))) or w or (not(y))
#                 if F == False:
#                     print(x, y, z, w)
# # x y z w
# # 0 1 0 0
# # 1 1 0 0
# # 1 1 1 0
# # zyxw


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w or (not(z))) and x and (not(y))
#                 if F == True:
#                     print(x, y, z, w)
# x y z w
# 1 0 0 0
# 1 0 0 1
# 1 0 1 1
# ywzx


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#                 F = (y or z) == ((z and (not(y))) <= (not(x)))
#                 if F == 0:
#                     print(x, y, z)
# x y z
# 0 0 0
# 1 0 0
# 1 0 1
# zyx


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = (z <= ((not(x)) and y)) <= (z == y)
#             if F == 0:
#                 print(x, y, z)
# zxy

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (y and (not(x))) or (x == w) or z
#                 if F == False:
#                     print(x, y, z, w)
# x y z w
# 0 0 0 1
# 1 0 0 0
# 1 1 0 0
# xyzw


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w or x or z) and ((x <= z) <= (y <= w))
#                 if F == 0:
#                     print(x, y, z, w)
# x y z w
# 0 0 0 0
# 0 1 0 0
# 0 1 1 0
# 1 1 1 0
# yzxw


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((z <= x) or ((not(w)) and y)) == (y == x)
#                 if F == True:
#                     print(x, y, z, w)
# x y z w
# 0 0 0 0
# 0 0 0 1
# 0 1 1 1
# 1 1 0 0
# 1 1 0 1
# 1 1 1 0
# 1 1 1 1

# x y z w
# 0 0 0 1 *

# 0 1 1 1
# 1 1 0 0 *

# xyzw


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((z <= w) or (y == w)) and ((x or z) == y)
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 0 0 1
# 0 1 1 1
# 1 1 0 0
# 1 1 0 1
#zyxw




# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x <= y) == (z <= (not(w)))) and (z or y)
#                 print(x, y, z, w, int(F))
# x y z w F
# 0 1 1 1 0
# 1 1 0 0 1
# 0 0 1 0 1

# 0 1 0 0 1
# 0 1 0 1 1
# 0 1 1 0 1
# 1 0 1 1 1
# 1 1 0 1 1
# 1 1 1 0 1

# xwyz

#10
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(x)) and ((z <= y) <= w)
#                 print(x, y, z, w, int(F))
# x y z w F
# 0 1 0 0 0
# 0 1 1 0 0
# 0 1 0 1 1 * точно где-то есть

# 0 0 1 0 1

# 0 0 0 1 1
# 0 0 1 1 1

# x всегда нолик

# wxzy


# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((y <= w) == (x <= (not(z)))) and (x or w)
#                 print(x, y, z, w, int(F))
# x y z w F
# 1 0 1 1 0
# 0 1 0 1 1
# 1 0 0 0 1

# yzwx


# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w == (z <= x)) and y
#                 print(x, y, z, w, int(F))
# x y z w F
# 1 1 1 0 0
# 0 1 0 1 1
# 0 1 1 0 1

# ywxz


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or (not(y))) and (not(y == z)) and (not(w))
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 0 1 0
# 1 0 1 0
# 1 1 0 0
# xzyw


# print('x y z w F1 F2')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F1 = (w == x) and (z <= y)
#                 F2 = (w <= x) <= (y == z)
#                 print(x, y, z, w, int(F1), int(F2))
# x y z w F1 F2
# 1 1 0 1 1 0 *
# 1 1 0 0 0 0 **
# 0 1 1 0 1 1


# xzwy







#ДЗ


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (y and x) or z or (not(w))
#                 if F == False:
#                     print(x, y, z, w)
# x y z w
# 0 0 0 1
# 0 1 0 1
# 1 0 0 1
# wzyx


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(y)) or x or (z and (not(w)))
#                 if F == False:
#                     print(x, y, z, w)
# x y z w
# 0 1 0 0
# 0 1 0 1
# 0 1 1 1
# xwzy


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (y <= x) and z and (not(z == y))
#                 if F == 1:
#                     print(x, y, z)
# x y z
# 0 0 1
# 1 0 1
# yzx


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not(z)) or (not(y))) <= (x == z)
#                 if F == 0:
#                     print(x, y, z)
# x y z
# 1 0 0
# 1 1 0
# yxz


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or y) and (not(y == z)) and (not(w))
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 1 0 0
# 1 0 1 0
# 1 1 0 0
# zywx


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((y <= z) <= (x and y)) and (x <= w)
#                 if F == True:
#                     print(x, y, z, w)
# x y z w
# 0 1 0 0
# 0 1 0 1
# 1 1 0 1
# zxwy


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and (not(y))) or (y == z) or w
#                 if F == False:
#                     print(x, y, z, w)
# x y z w
# 0 0 1 0
# 0 1 0 0
# 1 1 0 0
# xwzy


# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((y <= x) == (w <= (not(z)))) and (w or x)
#                 print(x, y, z, w, int(F))
# x y z w F
# 1 0 1 1 0
# 1 1 0 0 1
# 0 0 0 1 1
#yzxw


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or y) and (not(y == z)) and (not(w))
#                 if F == 1:
#                     print(x, y, z, w)
# x y z w
# 0 1 0 0
# 1 0 1 0
# 1 1 0 0


# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or y) and((not(y)) == z) and w
#                 print(x, y, z, w, int(F))
# x y z w F
# 0 0 0 0 0
# 0 0 0 1 0
# 0 0 1 0 0
# 0 0 1 1 0
# 0 1 0 0 0
# 0 1 1 0 0
# 0 1 1 1 0
# 1 0 0 0 0
# 1 0 0 1 0
# 1 0 1 0 0
# 1 1 0 0 0
# 1 1 1 0 0
# 1 1 1 1 0


# 0 1 0 1 1
# 1 0 1 1 1
# 1 1 0 1 1
# wzxy


print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(x)) or (z == w)) or (not(y <= w))
                print(x, y, z, w, int(F))
# x y z w F
# 0 0 0 0 1
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 1
# 0 1 0 1 1
# 0 1 1 0 1
# 0 1 1 1 1
# 1 0 0 0 1
# 1 0 1 1 1
# 1 1 0 0 1
# 1 1 1 0 1
# 1 1 1 1 1

# 1 0 0 1 0
# 1 0 1 0 0
# 1 1 0 1 0
# wzyx
