# f = open("24.3.txt")
# s = f.readline()
# a = s.split('O')
# res = []
# for i in range(len(a)-1):
#     res.append(a[i] + 'O' + a[i+1])
# print(len(max(res, key=len)))


# f = open('24.4.txt')
# s = f.readline()
# s = s.replace('S', 'T') #T это согласные
# s = s.replace('R', 'T')
# s = s.replace('A', 'U')
# print(len('UTUTUTUTUTUTUTUTUTUTUT')) #11


# f = open('24.5.txt')
# s = f.readline()
# s = s.replace('I', 'F')
# s = s.replace('N', 'F')
# s = s.replace('FF', 'F F')
# s = s.replace('FF', 'F F')
# a = s.split()
# print(len(max(a, key=len)))


# f = open('24.6.txt')
# s = f.readline()
# s = s.replace('FJN', '*')
# s = s.replace('JFN', '*')
# for i in range(1000): #проверка на порядок звездочек в строке
#     if '*'*i in s:
#         print(i)


# f = open('24.7.txt')
# s = f.readline()
# s = s.replace('FJW', 'FJ JW')
# s = s.replace('FJ', '*')
# s = s.replace('JW', '*')
# for i in range(1000):
#     if '*'*i in s:
#         print(i)


f = open('24.8.txt')
s = f.readline()
s = s.replace('YCRR', 'YCR CRR')
a = s.split()
print(len(max(a, key=len)))