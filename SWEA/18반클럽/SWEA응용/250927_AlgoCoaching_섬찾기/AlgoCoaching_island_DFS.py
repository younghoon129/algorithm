import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_AlgoCoaching_섬찾기\\island_input.txt')

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(x, y):
    island[x][y] = 0
    for dx, dy in dxy:
        nx, ny = dx+x, dy+y
        if 0 <= nx < n and 0 <= ny < n:
            if island[nx][ny] == 0: continue

            elif island[nx][ny] == 1:
                island[nx][ny] = 0
                dfs(nx, ny)
                
    

n, m = map(int, input().split())  # 섬의 크기 입력
island = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
island_cnt = 0  # 섬의 개수

for i in range(n):
    for j in range(n):
        if island[i][j] == 0: continue
        dfs(i, j)
        island_cnt += 1

print(island_cnt)  # 섬의 개수 출력
