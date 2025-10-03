# 19:31
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\1_A형\\250824_SWEA4130_특이한자석\\4130_input.txt','r')
from collections import deque

def bfs(l, r, visited):
    global t_list
    visited[l] = True
    t_list.append([l, r])
    queue = deque()
    queue.append([l, r])
    while queue:
        mag_num, rot = queue.popleft()
        if 0 < mag_num:
            if magnetic[mag_num][6] != magnetic[mag_num-1][2] and not visited[mag_num-1]:
                visited[mag_num-1] = True
                t_list.append([mag_num-1, -rot])
                queue.append([mag_num-1, -rot])
        if n-1 > mag_num:
            if magnetic[mag_num][2] != magnetic[mag_num+1][6] and not visited[mag_num+1]:
                visited[mag_num+1] = True
                t_list.append([mag_num+1, -rot])
                queue.append([mag_num+1, -rot])

n = 4
tc = int(input())
for t in range(1, tc+1):
    k = int(input())
    magnetic = deque(deque(map(int, input().split())) for _ in range(n))
    mag_point = [1,2,4,8]
    result = 0
    for _ in range(k):
        l, r = map(int, input().split())
        t_list = []
        visited = [False] * n
        l -= 1
        bfs(l, r, visited)
        for i in range(len(t_list)):
            magnetic[t_list[i][0]].rotate(t_list[i][1])
    for j in range(n):
        if magnetic[j][0] == 1:
            result += mag_point[j]
    print(f"#{t} {result}")