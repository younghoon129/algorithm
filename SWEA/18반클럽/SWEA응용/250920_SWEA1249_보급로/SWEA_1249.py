from collections import deque
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def road(box, n, visited):
    global result
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = box[0][0]

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < n:
                min_vi = visited[x][y] + box[nx][ny]
                if visited[nx][ny] > min_vi:
                    visited[nx][ny] = min_vi
                    queue.append((nx, ny))
    return visited[n-1][n-1]
                


tc = int(input())
for t in range(1, 2):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    result = 0
    visited = [[float('INF')]*n for _ in range(n)]
    result = road(box, n, visited)
    print(f"#{t} {result}")
    