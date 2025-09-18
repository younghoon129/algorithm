from collections import deque

dxy= [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(arr, x, y):
    global result
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    
    while queue:
        cx, cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx+dx, cy+dy

            if arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 3:
                result = 1
                return

            queue.append((nx, ny))
            arr[nx][ny] = 1

for t in range(1, 11):
    test = input()
    result = 0

    ed = []
    size = 16
    box = [list(map(int, input().strip())) for _ in range(size)]
    # print(box)

    for i in range(size):
        for j in range(size):
            # print(i, j)
            if box[i][j] == 3:
                ed.append((i, j))
        
        for k in range(size):
            if box[i][k] == 2:
                bfs(box, i ,k)

    print(f"#{t} {result}")