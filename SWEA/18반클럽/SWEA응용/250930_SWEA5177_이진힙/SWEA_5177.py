import sys
sys.stdin = open('SWEA_5177_input.txt', 'r')
import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = list(map(int, input().split()))
    h = [0]
    heapq.heapify(h)

    for i in range(len(box)):
        heapq.heappush(h, box[i])
    # print(h)

    result = h[1]
    print(h)
    print(h[8], h[8//2], h[(8//2)//2], h[1])
    # for idx, j in enumerate(h):