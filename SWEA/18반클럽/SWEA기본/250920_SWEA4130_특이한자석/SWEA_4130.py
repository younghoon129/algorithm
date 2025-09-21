from collections import deque
def turn_mag(x, y):  # x : 자석번호, y : 회전방향, 여기서 회전 해야될 정보만 만들자
    global magnetic, result
    if x == nn:
        return
    if x < 0:
        return
    magnetic[x].rotate(y)
    print(magnetic[x])

    if magnetic[x][0] == 1:
        result += mag_point[x]
        print('더하기')

    if 0 <= x-1:  # 왼쪽 자석 있다면
        print(y, '조건1')
        if magnetic[x][6] != magnetic[x-1][2]:
            turn_mag(x-1, -(y))
            print('1')
    if x+1 < m_num:  # 오른쪽 자석 있다면
        print(y, '조건2')
        if magnetic[x][2] != magnetic[x+1][6]:
            turn_mag(x+1, -(y))
            print('2')

tc = int(input())
for t in range(1, tc+1):
    m_num = 4
    nn = int(input())
    magnetic = ([deque(map(int, input().split())) for _ in range(m_num)])
    result = 0
    mag_point = [1, 2, 4, 8]
    for n in range(nn):
        x, y = map(int, input().split())
        x -= 1
        turn_mag(x, y)
    print(result)
# 1
# 2
# 0 0 1 0 0 1 0 0
# 1 0 0 1 1 1 0 1
# 0 0 1 0 1 1 0 0
# 0 0 1 0 1 1 0 1
# 1 1
# 3 -1