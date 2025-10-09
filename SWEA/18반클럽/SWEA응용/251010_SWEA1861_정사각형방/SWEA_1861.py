dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(i, j, c):
    global max_cnt, cnt
    cnt = c
    max_cnt = max(max_cnt, c)

    for dx, dy in dxy:
        nx, ny = dx+i, dy+j
        if 0 <= nx < n and 0 <= ny < n:
            if box[nx][ny] == box[i][j] + 1:
                dfs(nx, ny, c+1)

tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    st = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            cnt = 1
            dfs(i, j, cnt)
            if max_cnt == cnt:
                st = box[i][j]
    print(f"#{t} {st} {max_cnt}")