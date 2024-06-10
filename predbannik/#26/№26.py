# f = open('26.1_rgJenqs.txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# sale1 = sum(a[:3333]) * 0.5
# a.sort()
# sale2 = sum(a[:3333]) * 0.5
# print(sum(a)-sale1, sum(a)-sale2)

# f = open('26.2_5xUhRUh (1).txt')
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# sale1 = sum(a[:n//3])
# sale2 = []
# for i in range(len(a)):
#     if (i+1) % 3 == 0:
#         sale2.append(a[i])
# print(sum(a)-sale1, sum(a)-sum(sale2))



# f = open('26.19.txt')
# n = int(f.readline())
# boxes = [int(s) for s in f]
# boxes.sort(reverse=True)
# gift = [boxes[0]]
# for box in boxes:
#     if gift[-1] - box >= 3:
#         gift.append(box)
# print(len(gift), min(gift))
#
#
# f = open('26.20.txt')
# n = int(f.readline())
# boxes = [int(s) for s in f]
# boxes.sort(reverse=True)
# blocks = []
# while len(boxes) != 0:
#     gift = [boxes[0]]
#     boxes.remove(boxes[0])
#     for box in boxes[:]:
#         if gift[-1] - box >= 5:
#             gift.append(box)
#             boxes.remove(box)
#     blocks.append(gift)
# print(len(blocks), len(blocks[0]))
#
#
# f = open('26.21.txt')
# n = int(f.readline())
# boxes = []
# for s in f:
#     size, color = s.split()
#     boxes.append([int(size), color])
# boxes.sort(reverse=True)
# blocks = []
# while len(boxes) != 0:
#     gift = [boxes[0]]
#     del boxes[0]
#     for size, color in boxes[:]:
#         if gift[-1][0] - size >= 8 and gift[-1][1] != color:
#             gift.append([size, color])
#             boxes.remove([size, color])
#     blocks.append(gift)
# print(len(blocks), len(max(blocks, key=len)))
#
#
# f = open('26.22.txt')
# n = int(f.readline())
# events = []
# for s in f:
#     start, end = map(int, s.split())
#     events.append([end, start])
# events.sort()
# events_ok = [] #ивенты которые подошли
# freetime = 0
# for end, start in events:
#     if start >= freetime:
#         events_ok.append([start, end])
#         freetime = end
#     if start >= 1369:
#         print(start, end)
# print(len(events_ok))
# print(events_ok[-2], events_ok[-1])


# f = open('26.23.txt')
# k = int(f.readline())
# n = int(f.readline())
# bagazhi = []
# for s in f:
#     start, end = map(int, s.split())
#     bagazhi.append([start, end])
# bagazhi.sort()
# cnt = 0
# numb_cell = 0
# cells = [-1]*k
# for start, end in bagazhi:
#     for i in range(k):
#         if start > cells[i]:
#             cnt += 1
#             cells[i] = end
#             numb_cell = i + 1
#             break
# print(cnt, numb_cell)