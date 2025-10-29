import sys
sys.stdin = open('BAEK_2206_input.txt', 'r')
from collections import deque
from pprint import pprint
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(i, j, c):
    queue = deque()
    queue.append((i,j,c))
    visited0 = [[float('inf')] * m for _ in range(n)]
    visited1 = [[float('inf')] * m for _ in range(n)]
    visited0[i][j] = 1
    visited1[i][j] = 1
    while queue:
        # print(queue)
        x, y, z = queue.popleft()
        # print()
        if not z:
            for dx, dy in dxy:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m:
                    if box[nx][ny] == 1: continue
                    if visited0[nx][ny] <= visited0[x][y] + 1: continue

                    elif box[nx][ny] == 0:
                        visited0[nx][ny] = visited0[x][y] + 1
                        queue.append((nx, ny, z))
        if z:
            for dx, dy in dxy:
                nx, ny = dx + x, dy + y
                p = z
                if 0 <= nx < n and 0 <= ny < m:
                    if visited1[nx][ny] <= visited1[x][y] + 1: continue
                    if box[nx][ny] == 1:
                        p -= 1
                        visited1[nx][ny] = visited1[x][y] + 1
                        queue.append((nx, ny, p))

                    elif box[nx][ny] == 0:
                        visited1[nx][ny] = visited1[x][y] + 1
                        queue.append((nx, ny, p))
    return min(visited0[n-1][m-1], visited1[n-1][m-1])
n, m = map(int, input().split())

box = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0, 1))
