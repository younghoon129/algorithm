import sys
sys.stdin = open('BAEK_2564_input.txt', 'r')
from collections import deque

dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(i, j):
    global result
    cnt = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx, ny = dx+x, dy+y
                if 0 <= nx < m and 0 <= ny < n:
                    if visited[nx][ny]: continue
                    if box[nx][ny]:
                        result += cnt
                    visited[nx][ny] = True
                    queue.append((nx, ny))


n, m = map(int, input().split()) # 가로 세로
stores = int(input())
n, m = n+1, m+1
box = [[False] * n for _ in range(m)]
visited = [[True] * n for _ in range(m)]
result = 0

for i in range(n):
    visited[0][i] = False
    visited[m-1][i] = False
for j in range(m):
    visited[j][0] = False
    visited[j][n-1] = False

for store in range(stores):
    nswe, lluu = map(int, input().split())
    if nswe == 1:  # 북
        box[0][lluu] = True
    elif nswe == 2:  # 남
        box[m-1][lluu] = True
    elif nswe == 3:  # 서
        box[lluu][0] = True
    elif nswe == 4:  # 동
        box[lluu][n-1] = True

s, e = map(int, input().split())
st_i, st_j = 0, 0
if s == 1:  # 북
    st_i, st_j = 0, e
elif s == 2:  # 남
    st_i, st_j = m-1, e
elif s == 3:  # 서
    st_i, st_j = e, 0
elif s == 4:  # 동
    st_i, st_j = e, n-1
bfs(st_i, st_j)
print(result)
