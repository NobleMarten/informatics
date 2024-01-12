#ТЕОРИЯ


# def win1(x, s):
#     return (x + s < 156) and (((x + 2 + s) >= 156) or ((s + 2 + x) >= 156) or ((x * 5 + s) >= 156) or ((s * 5 + x) >= 156))
# def loss1(x, s):
#     return (not(win1(x, s))) and win1(x+2, s) and win1(x*5, s) and win1(x, s+2) and win1(x, s*5)
# def win2(x, s):
#     return loss1(x+2, s) or loss1(x*5, s) or loss1(x, s+2) or loss1(x, s*5)
# def loss12(x, s):
#     return (((win1(x+2, s) or win2(x+2, s)) and (win1(x*5, s) or win2(x*5, s)) and \
#         (win1(x, s+2) or win2(x, s+2)) and (win1(x, s*5) or win2(x, s*5))) and
#     (win2(x+2, s) or win2(x*5, s) or win2(x, s+2) or win2(x, s*5)))
#
# x = 5
#
# for s in range(1, 151):
#     # if win1(x, s):
#     #     print(s) #31
#     # if win1(x+2, s) or win1(x*5, s) or win1(x, s+2) or win1(x, s*5):
#     #     print(s) #7
#     # if win2(x, s):
#     #     print(s) #6
#     if loss12(x, s):
#         print(s) #29




#ПРАКТИКА



# def win1(s):
#     if s % 2 == 0:
#         return (s+1) >= 51 or (s+3) >= 51
#     else:
#         return (s * 3) >= 51
# def loss1(s):
#     if s % 2 == 0:
#         return (not(win1(s))) and win1(s+1) and win1(s+3)
#     else:
#         return (not(win1(s))) and win1(s*3)
# def win2(s):
#     if s % 2 == 0:
#         return loss1(s+1) or loss1(s+3)
#     else:
#         return loss1(s*3)
# def loss12(s):
#     if s % 2 == 0:
#         return win2(s+1) and win2(s+3)
#     else:
#         return win2(s*3)
#
#
# # for s in range(1, 51):
# #     if s % 2 == 0:
# #         if win1(s + 1) or win1(s + 3):
# #             print(s)
# #     else:
# #         if win1(s*3):
# #             print(s) #7
# # for s in range(1, 51):
# #     if win2(s):
# #         print(s) #1214
# for s in range(1, 51):
#     if loss12(s):
#         print(s) #2



# def win1(x, s):
#     return (x+s > 94) and (x + 2 + s) >= 94 or (s + 2 + x) >= 94 or (x+s + s) >= 94 or (x + s + x) >= 94
# def loss1(x, s):
#     return (not(win1(x, s))) and win1(x+2, s) and win1(x, s+2) and win1(x+s, s) and win1(x, s+x)
# def win2(x, s):
#     return loss1(x+2, s) or loss1(x, s+2) or loss1(x+s, s) or loss1(x, s+x)
# def loss12(x, s):
#     return (win1(x+2, s) or win2(x+2, s)) and (win1(x, s+2) or win2(x, s+2)) and \
#         (win1(x+s, s) or win2(x+s, s)) and (win1(x, s+x) or win2(x, s+x)) \
#         and (win2(x+2, s) or win2(x, s+2) or win2(x+s, s) or win2(x, s+x))
#
# #(x+2, s) (x, s+2) (x+s, s) (x, s+x)
# x = 7
# # for s in range(1, 87):
# #     if win1(x+2, s) or win1(x, s+2) or win1(x+s, s) or win1(x, s+x):
# #         print(s) #27
# # for s in range(1, 87):
# #     if win2(x, s):
# #         print(s) #2642
# for s in range(1, 87):
#     if loss12(x, s):
#         print(s) #40


# def win1(x, s):
#     return (x+3) * s >= 90 or (x+4) * s >= 90 or x * (s+3) >= 90 or x * (s+4) >= 90
# def loss1(x, s):
#     return (not(win1(x, s))) and win1(x+3, s) and win1(x+4, s) and win1(x, s+3) and win1(x, s+4)
# def win2(x, s):
#     return loss1(x+3, s) or loss1(x+4, s) or loss1(x, s+3) or loss1(x, s+4)
# def loss12(x, s):
#     return (win1(x+3, s) or win2(x+3, s)) and (win1(x+4, s) or win2(x+4, s)) and \
#         (win1(x, s+3) or win2(x, s+3)) and (win1(x, s+4) or win2(x, s+4))
#
# # (x+3, s) (x+4, s) (x, s+3) (x, s+4)
# x = 2
#
# # for s in range(1, 45):
# #     if win1(x+3, s) or win1(x+4, s) or win1(x, s+3) or win1(x, s+4):
# #         print(s) #9
# # for s in range(1, 45):
# #     if win2(x, s):
# #         print(s) #611
# for s in range(1, 45):
#     if loss12(x, s):
#         print(s) #4


#СТАТГРАД

from functools import lru_cache
def moves(x, s):
    return [(min(x, s) + i, max(x, s)) for i in range(1, min(x, s) + 1)]

@lru_cache
def game(x, s):
    if any(sum(m) >= 51 for m in moves(x, s)): return 'WIN1'
    if all(game(*m) == 'WIN1' for m in moves(x, s)): return 'LOSS1'
    if any(game(*m) == 'LOSS1' for m in moves(x, s)): return 'WIN2'
    if all(game(*m) == 'WIN1' or game(*m) == 'WIN2' for m in moves(x, s)): return 'LOSS12'

# a = []
# for x in range(1, 45):
#     for s in range(1, 45):
#         if game(x, s) == 'WIN1':
#             a.append(x + s)
# print(min(a)) #34
x = 6
# for s in range(1, 45):
#     if game(x, s) == 'WIN2':
#         print(s) #2536
for s in range(1, 45):
    if game(x, s) == 'LOSS12':
        print(s) #21