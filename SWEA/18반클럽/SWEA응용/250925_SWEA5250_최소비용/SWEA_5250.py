dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


import heapq


def dijkstra(bl, i, j):
    global result
    visited = [[float('INF')]*n for _ in range(n)]
    queue = []
    cnt = 0
    heapq.heappush(queue, (i, j, 0))
    visited[i][j] = 0
    while queue:

        x, y, cnt = heapq.heappop(queue)
        print(x, y, '##')
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                result = 1 + max(0, box[nx][ny] - box[x][y])
                n_cnt = cnt +
                if visited[x][y] < bl[nx][ny]:
                    visited[nx][ny] = bl[nx][ny] - bl[x][y]
                    result += (bl[nx][ny]-bl[x][y]+1)
                    heapq.heappush(queue, (nx, ny, cnt))
                else:
                    result += 1
                    heapq.heappush(queue, (nx, ny, cnt))

        if nx == n-1 and ny == n-1:
            return

    return

tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    dijkstra(box, 0, 0)
    print(result)


# 1
# 3
# 0 2 1
# 0 1 1
# 1 1 1