import sys
sys.stdin = open('SWEA_2819_input.txt', 'r')
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(box, re, x, y):

    if len(re) > max_len:
        return

    re.append(box[x][y])
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        dfs(box, re, nx, ny)


tc = int(input())

for t in range(1, tc + 1):
    n = 4
    max_len = 7
    cnt = 0
    box = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dfs(box, [], i, j)