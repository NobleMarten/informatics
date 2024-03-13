# №5

# for n in range(1000):
#     n2 = bin(n)[2:]
#     if len(n2) % 2 == 0:
#         n2 = n2[:len(n2)//2] + '1' + n2[len(n2)//2:]
#     r = int(n2, 2)
#     if r <= 33:
#         print(n)


# for n in range(1000):
#     n2 = bin(n)[2:]
#     n2 = n2.replace('0', '2')
#     n2 = n2.replace('1', '11')
#     n2 = n2.replace('2', '0')
#     r = int(n2, 2)
#     if r < 777:
#         print(n)


# for n in range(1000):
#     b = n
#     n -= n % 8
#     n2 = bin(n)[2:]
#     n2 += str(n2.count('1') % 2)
#     n2 += str(n2.count('1') % 2)
#     r = int(n2, 2)
#     if r < 86:
#         print(bin(b)[2:])


# for n in range(1000):
#     n2 = bin(n)[2:]
#     if n % 5 == 0:
#         n2 += n2[-3:]
#     else:
#         k = bin((n % 5) * 4)[2:]
#         n2 += k
#     r = int(n2, 2)
#     if r > 150:
#         print(n)


# def p3(n):
#     s = ''
#     while n > 0:
#         s = str(n % 3) + s
#         n = n // 3
#     return s
# for n in range(1000):
#     n3 = str(p3(n))
#     if n % 3 == 0:
#         n3 += n3[-3:]
#     else:
#         k = p3((n % 3) * 3)
#         n3 += k
#     if n3:
#         r = int(n3, 3)
#         if r > 344:
#             print(n)


# for n in range(1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += bin(n2.count('1'))[2:]
#     else:
#         n2 = '1' + n2 + '00'
#     r = int(n2, 2)
#     if r > 843:
#         print(n)


# for n in range(1000):
#     cnt_s = sum([int(s) for s in str(n)])
#     n2 = bin(n)[2:]
#     if cnt_s % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     if cnt_s % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     if cnt_s % 2 == 0:
#         n2 += '0'
#     else:
#         n2 += '1'
#     r = int(n2, 2)
#     if r > 522:
#         print(r)


# for n in range(100000):
#     n2 = bin(n)[2:]
#     n2 = n2.replace('1', '2')
#     n2 = n2.replace('0', '1')
#     n2 = n2.replace('2', '0')
#     n2 = n2.strip('0')
#     if n2:
#         np = int(n2, 2)
#         r = n - np
#         if r == 817:
#             print(n)


# def R(n):
#     cnt_s = sum([int(s) for s in str(n)])
#     n2 = bin(n)[2:]
#     if cnt_s % 2 != 0:
#         n2 += '1'
#     else:
#         n2 += '0'
#     if cnt_s % 2 != 0:
#         n2 += '1'
#     else:
#         n2 += '0'
#     if cnt_s % 2 != 0:
#         n2 += '1'
#     else:
#         n2 += '0'
#     return int(n2, 2)
# print(12345678 // 8)
# print(R(1543210))
# print(87654321 // 8)
# print(R(10956790-1))
# print(87654319 - 12345680 + 1)


# for n in range(1000):
#     s = '>' + '4'*97 + '7'*30 + '3'*n
#     while '>4' in s or '>7' in s or '>3' in s:
#         if '>4' in s:
#             s = s.replace('>4', '37>', 1)
#         if '>7' in s:
#             s = s.replace('>7', '3>', 1)
#         if '>3' in s:
#             s = s.replace('>3', '437>4', 1)
#     summ = s.count('3')*3 + s.count('4')*4 + s.count('7')*7
#     if summ % 103 == 0:
#         print(n)


# for n in range(1, 100000):
#     s = '>' + '2'*n + '4'*54 + '8'*33
#     while '>2' in s or '>4' in s or '>8' in s:
#         if '>2' in s:
#             s = s.replace('>2', '28>', 1)
#         if '>4' in s:
#             s = s.replace('>4', '22>8', 1)
#         if '>8' in s:
#             s = s.replace('>8', '244>', 1)
#     summ = s.count('2')*2 + s.count('4')*4 + s.count('8')*8
#     if 10000 <= summ <= 99999:
#         print(n)


for n in range(1, 1000):
    s = '>' + '1'*30 + '2'*20 + '3'*n
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 1)
    summ = s.count('2')*2 + s.count('1') + s.count('3')*3
    if summ % 11 == 0:
        print(n)