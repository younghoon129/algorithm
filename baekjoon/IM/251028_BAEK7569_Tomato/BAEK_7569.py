import sys
sys.stdin = open('BAEK_7569_input.txt', 'r')
from collections import deque
# 이동 방향 (위, 아래, 앞, 뒤, 좌, 우)
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
cnt = 0  # 며칠
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, y, x = queue.popleft()
    for l in range(6):
        nz, ny, nx = dz[l] + z, dy[l] + y, dx[l] + x
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz,ny,nx))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                cnt = -1
                break
            cnt = max(cnt, box[i][j][k])
        if cnt == -1:
            break
    if cnt == -1:
        break

if cnt == -1:
    print(cnt)
else:
    print(cnt -1)