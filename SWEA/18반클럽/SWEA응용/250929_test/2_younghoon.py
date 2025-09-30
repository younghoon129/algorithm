import sys
sys.stdin = open('2_input.txt', 'r')
import heapq

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(q, w):
    queue = []
    heapq.heappush(queue, (q, w))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for dx, dy in dxy:
            nx, ny = dx+x, dy+y
            while 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and box[nx][ny] != 0:
                pass


tc = int(input())
for t in range(1, tc+1):
    m, n = map(int, input().split())  # m= 세로, n = 가로
    box = [list(map(int, input().split())) for _ in range(m)]
    se = list(map(int, input().split()))
    st = []
    en = []
    result = 0
    for i in range(len(se)):
        if i < 2:
            st.append(se[i])
        else:
            en.append(se[i])
    visited = [[False] * n for _ in range(m)]
    bfs(st[0], st[1])
