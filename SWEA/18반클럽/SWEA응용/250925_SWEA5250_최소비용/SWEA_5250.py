dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

from collections import deque
import heapq
def bfs(box, x, y, cnt):
    queue = []
    heapq.heappush(queue, (x, y))
    while queue:
        x, y = heapq.heappop(queue)
        visited[x][y] = True
        # if visited[x][y]:
        # 힙큐로 경로를 가장 낮은 값들로 하고 빈 set에 if not in set 해서
        # 세트 안에 없으면 추가 하고 그것들 카운트해서 cnt에 값 더하기
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:

    pass

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    visited = [[0] for _ in range(n)]
    result = bfs(box, 0, 0, cnt)