import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\251009_SWEA1227_Maze2\\SWEA_1227_input.txt', 'r')
from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(st, en, visited, box):
    global cnt
    queue = deque()
    x, y = st
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        xx, yy = queue.popleft()
        print(xx, yy)
        if xx == en[0] and yy == en[1]:
            cnt = 1
            break
        

        for dx, dy in dxy:
            nx, ny = dx +xx, dy+yy
            if 0 <= nx < n and 0 <= ny < n:
                if box[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])


tc = 1 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
n = 100
for t in range(1, tc+1):
    x = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    st = []
    en = []
    for i in range(n):
        for j in range(n):
            if box[i][j] == 1 or box[i][j] == 0: continue
            if box[i][j] == 2:
                st = [i, j]
            if box[i][j] == 3:
                en = [i, j]
            if st and en:
                break

    # bfs(st, en, visited, box)
    print(cnt, st, en)
