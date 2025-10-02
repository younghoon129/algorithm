import sys
sys.stdin = open('Maze_input.txt','r')
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(box, visited, x, y):
    global result
    if box[x][y] == 3:
        result = 1
        return

    visited[x][y] = True

    for dx, dy in dxy:
        nx, ny = dx+x, dy+y

        if visited[nx][ny]:
            continue

        if box[nx][ny] == 1:
            continue

        dfs(box, visited, nx, ny)

tc = 10
for t in range(1, tc+1):
    tq = int(input())
    n = 16
    box = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = 0
    s, e = 1, 1
    dfs(box, visited, s, e)
    print(f"#{t} {result}")