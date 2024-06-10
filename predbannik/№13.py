# from ipaddress import *
# cnt = 0
# ip_net = ip_network('192.168.32.176/255.255.255.240')
# for ip_add in ip_net:
#     if f'{ip_add:b}'.count('1') % 2 != 0:
#         cnt += 1
# print(cnt)


# from ipaddress import *
# cnt = 0
# ip_net = ip_network('192.168.32.160/255.255.255.240')
# for ip_add in ip_net:
#     if f'{ip_add:b}'.count('1') % 2 == 0:
#         cnt += 1
# print(cnt)


# from ipaddress import *
# cnt = 0
# ip_net = ip_network('252.67.33.87/255.248.0.0', False)
# for ip_add in ip_net:
#     if (f'{ip_add:b}'[16:].count('1') / f'{ip_add:b}'[:16].count('1')) > 2:
#         cnt += 1
# print(cnt)


from ipaddress import *
for n in range(0, 9):
    A = int('1'*n + '0'*(8-n), 2)
ip_net = ip_network(f'255.224.33.160/255.255.{A}.0', False)
for ip_add in ip_net:
    if (f'{ip_add:b}'[:-16].count('1') >= f'{ip_add:b}'[-16:].count('1')) == False:
        break
    else:
        print(A)


# from ipaddress import *
# for A in range(0, 256):
#     ip_net = ip_network(f'127.254.{A}.19/255.255.224.0', False)
#     for ip_add in ip_net:
#         if (bin(int(ip_add))[2:][:-16].count('1') >= bin(int(ip_add))[2:][-16:].count('1')) == False:
#             break
#     else:
#         print(A)