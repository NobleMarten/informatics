# def WIN1(s):
#     return (s + 1) >= 100 or (s * 2) >= 100
#
# def LOSS1(s):
#     return (not(WIN1(s))) and WIN1(s + 1) and WIN1(s * 2)
#
# def WIN2(s):
#     return LOSS1(s + 1) or LOSS1(s * 2)
#
# def LOSS12(s):
#     return (WIN2(s + 1) and WIN1(s * 2))
#
# # for s in range(1, 99 + 1):
# #     if WIN1(s):
# #         print(s) #50
#
# # for s in range(1, 99 + 1):
# #     if WIN2(s):
# #         print(s) #48
#
# for s in range(1, 99 + 1):
#     if LOSS12(s):
#         print(s) #47





# def win1(s):
#     return (s+1) >= 93 or (s*3-1) >= 93
#
# def loss1(s):
#     return (not(win1(s))) and win1(s+1) and win1(s*3-1)
#
# def win2(s):
#     return loss1(s+1) or loss1(s*3-1)
#
# def loss12(s):
#     return (win1(s*3-1) and win2(s+1))
#
# # for s in range(1, 92 + 1):
# #     if win1(s+1) or win1(s*3-1):
# #         print(s) #11
#
# # for s in range(1, 92 + 1):
# #     if win2(s):
# #         print(s) #30
#
# for s in range(1, 92 + 1):
#     if loss12(s):
#         print(s) #29



#ДЗ


def win1(s):
    return (s+2) >= 46 or (s*2) >= 46

def loss1(s):
    return (not(win1(s))) and win1(s+2) and win1(s*2)

def win2(s):
    return loss1(s+2) or loss1(s*2)

def loss12(s):
    return (win1(s*2) and win2(s+2))

# for s in range(1, 45 + 1):
#     if win1(s+2) or win1(s*2):
#         print(s) #12

# for s in range(1, 45 + 1):
#     if win2(s):
#         print(s) #1120

for s in range(1, 45 + 1):
    if loss12(s):
        print(s) #17