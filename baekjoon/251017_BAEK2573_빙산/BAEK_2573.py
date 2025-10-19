import sys
sys.stdin = open('BAEK_2573_input.txt','r')
from collections import deque
from pprint import pprint

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 빙산 녹이는 거
def melt_iceberg():
    global box
    for i in range(1, n):
        for j in range(1, m):
            if not box[i][j]: continue

            for dx, dy in dxy:
                nx, ny = dx + i, dy + j
                if new_box[nx][ny] == 0:
                    if not box[i][j]: continue
                    box[i][j] -= 1

def bfs(q, w, visited):  # 빙산 갯수 구하는 거
    queue = deque()
    queue.append((q, w))
    visited[q][w] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if visited[nx][ny]: continue  # 방문했으면 안함
            if not box[nx][ny]: continue  # 0이면 빙산 아님
            visited[nx][ny] = True
            queue.append((nx, ny))

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
max_num = max(map(max, box))
cnt = 0  # 빙산 녹인 년도
no_iceberg = 0  # 빙산 조건 안되면 출력
condition_iceberg = 2  # 빙산 문제 조건
iceberg_cnt = 0  # 빙산 갯수

# 빙산 녹이고 방문처리 초기화 해야됨
while iceberg_cnt < condition_iceberg:
    new_box = [var[:] for var in box]
    melt_iceberg()  # 빙산 녹이는 거
    cnt += 1
    iceberg_cnt = 0
    visited = [[False] * m for _ in range(n)]
    for q in range(1, n):
        for w in range(1, m):
            if not box[q][w]: continue
            if visited[q][w]: continue
            bfs(q, w, visited)
            iceberg_cnt += 1
    if not iceberg_cnt: break
if iceberg_cnt >= condition_iceberg:
    print(cnt)
else:
    print(no_iceberg)

# pprint(box)
