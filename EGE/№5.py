# a = [2, 6, 1, 767, 9]
#
# print(a[:4])

# s = bin(1893)
# print(s[2::])
# print(s[-3::])

# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0: #n2 += str(n2.count('1') % 2)
#         n2 += '0'
#     else:
#         n2 += '1'
#     if n2.count('1') % 2 == 0: ##n2 += str(n2.count('1') % 2)
#         n2 += '0'
#     else:
#         n2 += '1'
#     R = int(n2, 2)
#     if R > 3123:
#         print(n)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     n2 += str(n2.count('1') % 2)
#     n2 += str(n2.count('1') % 2)
#     R = int(n2, 2)
#     if R > 2222:
#         print(R)
#         break

# a = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += n2[0] + n2[1] #n2[:2]
#     else:
#         n2 = '1' + n2 + '0'
#     R = int(n2, 2)
#     if R > 410:
#         a.append(R)
# print(min(a))


# a = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = '1' + n2 + '10'
#     else:
#         n2 = '11' + n2 + '0'
#     R = int(n2, 2)
#     if R > 260:
#         a.append(R)
# print(min(a))


# a = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += bin(n2.count('1'))[2:]
#     else:
#         n2 = '1' + n2 + '00'
#     R = int(n2, 2)
#     if R > 432:
#         print(n) # если нужно найти n, то список не нужен
#         break


#другой способ
# def R(n):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2:
#         n2 += '0'
#         n2 = '10' + n2[2:]
#     else:
#         n2 += '1'
#         n2 = '11' + n2[2:]
#     return int(n2, 2)
# for n in range(1, 1000):
#     if R(n) >= 256:
#         print(n)
#         break #128



#дз


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     R = int(n2, 2)
#     if R > 1096:
#         print(n)


# a = []
# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     R = int(n2, 2)
#     if R > 680:
#         a.append(R)
# print(min(a))


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += n2[-2::]
#     else:
#         n2 = '1' + n2 + '0'
#     R = int(n2, 2)
#     if R > 1038:
#         print(n)


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0:
#         n2 += '10'
#         n2 = '10' + n2[2:]
#     else:
#         n2 += '01'
#         n2 = '11' + n2[2:]
#     R = int(n2, 2)
#     if R > 102:
#         print(n)