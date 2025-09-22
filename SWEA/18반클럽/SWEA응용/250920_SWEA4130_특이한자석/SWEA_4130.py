from collections import deque
import copy
def turn_mag(x, y):  # x : 자석번호, y : 회전방향, 여기서 회전 해야될 정보만 만들자
    global new_mag, result, visited
    new_mag[x].rotate(y)
    visited[x] = True
    if 0 <= x-1:  # 왼쪽 자석 있다면
        if not visited[x-1]:
            if magnetic[x][6] != magnetic[x-1][2]:
                turn_mag(x-1, -(y))
    if x+1 < m_num:  # 오른쪽 자석 있다면
        if not visited[x+1]:
            if magnetic[x][2] != magnetic[x+1][6]:
                turn_mag(x+1, -(y))
tc = int(input())
for t in range(1, tc+1):
    m_num = 4
    nn = int(input())
    magnetic = ([deque(map(int, input().split())) for _ in range(m_num)])
    result = 0
    mag_point = [1, 2, 4, 8]
    for n in range(nn):
        visited = [False]*m_num
        x, y = map(int, input().split())
        x -= 1
        new_mag = copy.deepcopy(magnetic)
        turn_mag(x, y)
        magnetic = copy.deepcopy(new_mag)

    for i in range(m_num):
        if magnetic[i][0] == 1:
            result+=mag_point[i]
    print(f"#{t} {result}")
# 1
# 2
# 0 0 1 0 0 1 0 0
# 1 0 0 1 1 1 0 1
# 0 0 1 0 1 1 0 0
# 0 0 1 0 1 1 0 1
# 1 1
# 3 -1