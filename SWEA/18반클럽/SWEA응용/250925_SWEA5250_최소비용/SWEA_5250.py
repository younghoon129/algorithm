import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\SWEA응용\\250925_SWEA5250_최소비용\\SWEA_5250_input.txt')
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


import heapq


def dijkstra(bl, i, j):
    global result
    visited = [[float('INF')]*n for _ in range(n)]
    queue = []
    heapq.heappush(queue, (i, j))
    visited[i][j] = 0
    while queue:
        x, y = heapq.heappop(queue)
        if x == n-1 and y == n-1:
            return visited[n-1][n-1]
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if bl[x][y] < bl[nx][ny]:
                    if visited[x][y] + (bl[nx][ny]-bl[x][y]+1) < visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] +(bl[nx][ny] - bl[x][y] + 1)
                        heapq.heappush(queue, (nx, ny))
                elif visited[x][y] + (bl[nx][ny]-bl[x][y]+1) < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    heapq.heappush(queue, (nx, ny))
        
    return visited[n-1][n-1]        

    # while queue:
    #     cost, x, y = heapq.heappop(queue)
 
    #     if cost > visited[x][y]:  # 이동 비용이 저장된 비용보다 크면 pass
    #         continue
 
    #     for dx, dy in dxy:
    #         nx, ny = x + dx, y + dy
    #         if 0 <= nx < n and 0 <= ny < n:
    #             next_cost = 1  # 다음 칸 기본 이동 비용 1
    #             if bl[nx][ny] > bl[x][y]:  # 다음칸 높이가 더 높으면
    #                 next_cost += (bl[nx][ny] - bl[x][y])  # 이동 비용에다 높이 차이만큼 +
    #             new_dist = cost + next_cost  # 새로운 이동 비용 = 현재까지의 비용 + 이동 비용
 
    #             if new_dist < visited[nx][ny]:  # 새로운 이동 비용이 기록된 최소 비용보다 적으면 갱신
    #                 visited[nx][ny] = new_dist
    #                 heapq.heappush(queue, (new_dist, nx, ny))
 
    #     if (x, y) == (n - 1, n - 1):  # 도착하면 반환
    #         return cost  

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