from collections import deque

dxy= [[0, 1], [1, 0], [0, -1], [-1, 0]]

def road(box, visited):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = box[0][0]
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx+ x, dy +y
            if 0 <= nx < n and 0 <= ny < n:
                n_box = visited[x][y] + box[nx][ny]
                if visited[nx][ny] > n_box:
                    visited[nx][ny] = n_box
                    queue.append((nx,ny))

    return visited[n-1][n-1]

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    visited = [[float('INF')]* n for _ in range(n)]  

    result = road(box, visited)

    print(f"#{t} {result}")