import sys
sys.stdin = open('SWEA_1249_input.txt','r')
from collections import deque
import heapq
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(box, visited, st, en):
    queue = []
    visited[0][0] = 0
    dis = visited[0][0]
    heapq.heappush(queue, (st[0], st[1], dis))

    while queue:
        x, y, dist = heapq.heappop(queue)
        if x == en[0] and y == en[1]:
            return
        for dx, dy in dxy:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > dist + box[nx][ny]:
                    visited[nx][ny] = dist + box[nx][ny]
                    heapq.heappush(queue, (nx, ny, visited[nx][ny]))

tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    visited = [[float('inf')] * n for _ in range(n)]
    st = (0, 0)
    en = (n-1, n-1)
    bfs(box, visited, st, en)
    result = visited[en[0]][en[1]]
    print(f"#{t} {result}")