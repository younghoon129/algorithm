from collections import deque
def turn_mag(x, y, mag_sum):  # x : 자석번호, y : 회전방향
    global magnetic
    if x == nn:
        return
    if x < 0:
        return
    magnetic[x].rotate(y)
    

    if magnetic[x][0] == 1:
        mag_sum += mag_point[x]

    if 0 <= x-1 and x+1 < m_num:
        if magnetic[x][6] != magnetic[x-1][2]:
            turn_mag(x-1, -y, mag_sum)
        if magnetic[x][2] != magnetic[x+1][6]:
            turn_mag(x+1, -y, mag_sum)

tc = int(input())
for t in range(1, tc+1):
    m_num = 4
    nn = int(input())
    magnetic = ([deque(map(int, input().split())) for _ in range(m_num)])
    mag_sum = 0
    result = 0
    mag_point = [1, 2, 4, 8]
    for n in range(nn):
        x, y = map(int, input().split())
        turn_mag(x, y, mag_sum)
        result += mag_sum
    print(result)

# 1
# 2
# 0 0 1 0 0 1 0 0
# 1 0 0 1 1 1 0 1
# 0 0 1 0 1 1 0 0
# 0 0 1 0 1 1 0 1
# 1 1
# 3 -1