import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\SWEA응용\\250920_SWEA1249_보급로\\SWEA_1249_input.txt','r')
from collections import deque
import heapq
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(box, visited, st, en):
    queue = []
    heapq.heappush(queue, (st))
    visited[0, 0] = 0
    while queue:
        x, y = heapq.heappop(queue)
        for dx, dy in dxy:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < n:
                


tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    st = (0, 0)
    en = (n-1, n-1)
    bfs(box, visited, st, en)
