# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x <= (y and (not(z)))) or w
#                 if F == 0:
#                     print(x, y, z, w)
# # x y z w
# # 1 0 0 0
# # 1 0 1 0
# # 1 1 1 0
# # ywxz


# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((w <= x) == (z <= y)) and ((not(y)) or w)
#                 print(x, y, z, w, int(F))


# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((z <= y) == (x <= (not(w)))) and (x or y)
#                 print(x, y, z, w, int(F))
# x y z w F
# 1 0 0 0 1
# 0 1 1 0 1
# 1 1 0 1 0
# zwyx


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w <= y) <= (x <= z)
#                 if F == 0:
#                     print(x, y, z, w)
# # x y z w
# # 1 0 0 0
# # 1 1 0 0
# # 1 1 0 1
# # yzxw


# print('x y z w F1 F2')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F1 = (x <= w) == (z <= y)
#                 F2 = (x <= w) and ((not(y)) == z)
#                 print(x, y, z, w, int(F1), int(F2))
# # x y z w  F1 F2
# # 1 0 0 0  0 0
# # 1 1 1 0  0 0
# # 0 0 1 0  0 1
# # wxzy