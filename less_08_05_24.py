# from ipaddress import *
# cnt = 0
# ip_net = ip_network('192.168.32.176/255.255.255.240', False)
# for ip_add in ip_net:
#     if bin(int(ip_add)).count('1') % 2 != 0:
#         cnt += 1
# print(cnt)


# from ipaddress import *
# cnt = 0
# ip_net = ip_network('192.168.32.160/255.255.255.240', False)
# for ip_add in ip_net:
#     if bin(int(ip_add)).count('1') % 2 == 0:
#         cnt += 1
# print(cnt)


# from ipaddress import *
# cnt = 0
# ip_net = ip_network('252.67.33.87/255.255.0.0', False)
# for ip_add in ip_net:
#     if bin(int(ip_add))[-16:].count('1') > bin(int(ip_add))[:-16].count('1'):
#         cnt += 1
# print(cnt)


# from ipaddress import *
# cnt = 0
# for n in range(9):
#     A = int(n*'1' + '0'*(8-n), 2)
#     ip_net = ip_network(f'255.224.33.160/255.255.{A}.0', False)
#     for ip_add in ip_net:
#         if bin(int(ip_add))[:-16].count('1') >= bin(int(ip_add))[-16:].count('1') == False:
#             break
#     else:
#         print(A)



# s = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
# cnt = 0
# while s > 0:
#     if s % 27 > 9:
#         cnt += 1
#     s = s // 27
# print(cnt)


s = 2 * 1296**2014 - 2 * 432**2016 + 2 * 36**2020 - 2 * 12**2022 -2024
cnt = 0
while s > 0:
    if s % 36 > 15:
        cnt += 1
    s = s // 36
print(cnt)
