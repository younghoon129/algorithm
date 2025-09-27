import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250925_SWEA5250_최소비용\\SWEA_5250_input.txt')
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


import heapq


def dijkstra(height, i, j):
    global result
    cost = [[float('INF')]*n for _ in range(n)]
    queue = []
    heapq.heappush(queue, (i, j))
    cost[i][j] = 0
    while queue:
        x, y = heapq.heappop(queue)
        
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                n_cost = cost[x][y]+(height[nx][ny]-height[x][y]+1)
                if height[x][y] < height[nx][ny]:
                    if n_cost < cost[nx][ny]:
                        cost[nx][ny] = n_cost
                        heapq.heappush(queue, (nx, ny))
                if height[x][y] >= height[nx][ny]:
                    if cost[x][y]+1 < cost[nx][ny]:
                        cost[nx][ny] = cost[x][y] + 1
                        heapq.heappush(queue, (nx, ny))
        if x == n-1 and y == n-1:
            return cost[n-1][n-1]

tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    result = dijkstra(box, 0, 0)
    print(f"#{t} {result}")


# 1
# 3
# 0 2 1
# 0 1 1
# 1 1 1