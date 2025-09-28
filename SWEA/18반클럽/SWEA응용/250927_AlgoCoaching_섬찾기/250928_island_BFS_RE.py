import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_AlgoCoaching_섬찾기\\island_input.txt')
from collections import deque
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(box, visited, i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < n:
                if box[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

n, m = map(int, input().split())
box = [list(map(int, input().strip())) for _ in range(n)]
result = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if box[i][j] == 0 or visited[i][j]: continue
        bfs(box, visited, i, j)
        result += 1

print(result)