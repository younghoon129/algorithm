from collections import deque
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_3_TestPracitce\\magnet_input.txt','r')


# def bfs(rot, visited):
#     global rotate
#     queue = deque()
#     queue.append([rot[0][0]-1, rot[0][1]])
#     # print(queue, 'Qweqwe')
#     visited[rot[0][0]-1] = True
#     while queue:
#         m_num, m_rot = queue.popleft()
#         if 0 < m_num:
#             if magnet[m_num][6] != magnet[m_num][2] and not visited[m_num]:
#                 visited[m_num] = True
#                 rotate.append([m_num, -m_rot])
#                 queue.append([m_num, -m_rot])
#         if n-1 > m_num:
#             # print(m_num)
#             # print(magnet[m_num])
#             # print(magnet[m_num+1])
#             # print(visited[m_num+1])
#             if magnet[m_num][2] != magnet[m_num+1][6] and not visited[m_num+1]:
#                 visited[m_num+1] = True
#                 rotate.append([m_num+1, -m_rot])
#                 queue.append([m_num+1, -m_rot])

def mag(rotate, visited):
    x, y = rotate
    visited[x] = True
    turn.append([x, y])

    if 0 <= x - 1 and not visited[x-1]:  # 왼
        if magnet[x-1][6] != magnet[x-2]:

tc = int(input())
n = 4
for t in range(1, tc+1):
    k = int(input())
    magnet = [list(map(int, input().split())) for _ in range(n)]

    for i in range(k):
        visited = [False] * n
        m, t = map(int, input().split())
        rotate = [m, t]
        turn = []
        m -= 1
        mag([rotate], visited)
        print(rotate)
    