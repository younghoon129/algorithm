import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_SWEA1226_Maze\\Maze_input.txt','r')
from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(box, s, e, visited):
    global result
    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if box[nx][ny] == 3:
                    result = 1
                    return result
                if box[nx][ny] == 1: continue

                if box[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

tc = 10
n = 16
for t in range(1, tc+1):
    x = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    s = []
    e = []
    result = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if box[i][j] == 2:
                s.extend([i, j])
            elif box[i][j] == 3:
                e.extend([i, j])
    # ======================================
    bfs(box, s, e, visited)
    print(f"#{t} {result}")