import sys
sys.stdin = open('SWEA_5177_input.txt', 'r')
import heapq
from collections import deque

# def dfs(num):
#     global result
#     if num <= 0:
#         return
#     result += h[num]
#     if num == 2:
#         return
#     else:
#         dfs(num//2)
#
# tc = int(input())
# for t in range(1, tc+1):
#     n = int(input())
#     box = list(map(int, input().split()))
#     h = []
#     result = 0
#     for i in range(len(box)):
#         heapq.heappush(h, box[i])
#     st = len(h)
#     result = h[0]
#     dfs((st-1)//2)
#     print(f"#{t} {result}")
#

# tc = int(input())
# for t in range(1, tc+1):
#     n = int(input())
#     box = list(map(int, input().split()))
#     h = []
#     result = 0
#     queue = deque()
#     queue.append(n)
#     for i in range(len(box)):
#         heapq.heappush(h, box[i])
#     while queue:
#         x = queue.popleft()
#         if x > 0:
#             x = (x - 1) // 2
#             result += h[x]
#             # print(h[x], '@')
#             queue.append(x)
#     print(f"#{t} {result}")


# import heapq
#
# def dfs(num):
#     global result
#
#     if num < 0:
#         return
#     result += h[num]
#     dfs((num-1)//2)
#
#
# tc = int(input())
# for t in range(1, tc+1):
#     n = int(input())
#     box = list(map(int, input().split()))
#     h = []
#     result = 0
#     for i in range(len(box)):
#         heapq.heappush(h, box[i])
#     dfs((n-1)//2)
#     print(f"#{t} {result}")


def dfs(num):
    global cnt

    if num < 0:
        return
    cnt += result.heap[num]
    dfs((num-1)//2)


class MinHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) -1)

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2


tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = list(map(int, input().split()))
    result = MinHeap()
    cnt = 0
    for i in box:
        result.heappush(i)
    jdx = len(result.heap) - 1
    while jdx > 0:
        jdx = (jdx-1) // 2
        cnt += result.heap[jdx]
        # print(result.heap[jdx])
    print(f"#{t} {cnt}")
