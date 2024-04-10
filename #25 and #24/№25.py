from fnmatch import *
# for x in range(4323, 10**9, 4323):
#     if fnmatch(str(x), '1?7344*3'):
#         print(x, x // 4323)


# for x in range(3323, 10**9, 3323):
#     if fnmatch(str(x), '13*61?2?'):
#         print(x, x // 3323)


# for x in range(149, int('FFFFFF', 16)+1 ,149):
#     if fnmatch(hex(x)[2:], 'a15?*f'):
#         print(x, x // 149)


# prime = [2, 3, 5, 7]
# fib = [0, 1, 1, 2, 3, 5, 8]
# # '11ПФ2?7'
# for x in range(513*2, 10**8, 513):
#     if int(str(x)[2]) in prime and int(str(x)[3]) in fib and fnmatch(str(x), '11??2?7'):
#         print(x, x // 513)