import sys
sys.stdin = open('C://Users//user//Desktop//git//algorism//SWEA//18반클럽//0_IM복기//250908_SWEA10761_신뢰//SWEA10761_신뢰.txt', 'r')
from collections import deque
test = int(input())
for t in range(1, test+1):
    box = list(input().split())
    b = deque()  # 숫자
    o = deque()  # 숫자
    max_cnt = 0
    bs = 1
    os = 1
    for i in range(int(box[0])):
        if box[(2*i)+1] == 'B':
            b.append(int(box[2*(i+1)]))
        elif box[(2*i)+1] == 'O':
            o.append(int(box[2*(i+1)]))
    
    cnt=0
    i = 1
    while b or o:
        # print(bs, 'bs')
        # print(os, 'os')
        # print(cnt, max_cnt, 'cnt, max_cnt')
        # print(box[i*2])
        if b or o:
            if b:
                # print(b[0], bs,'bs', cnt, 'cnt', max_cnt, 'max_cnt')
                if b[0] > bs:
                    bs+=1
                    # cnt+=1
                elif b[0] < bs:
                    bs -=1
                    # cnt+=1
                
            if o:
                
                if o[0] > os:
                    os+=1
                    # cnt+=1
                elif o[0] < os:
                    os-=1
                    # cnt+=1
            cnt += 1
            
        if box[i*2-1] == 'B' and int(box[i*2]) == bs:
            # cnt+=1
            max_cnt += cnt
            cnt = 0
            print(b[0], bs,'bs', cnt, 'cnt', max_cnt, 'max_cnt')
            b.popleft()
            i+=1
            
            print('1111111111111111')
        elif box[i*2-1] == 'O' and int(box[i*2]) == os:
            # cnt += 1
            max_cnt += cnt
            cnt = 0
            print(o[0], os,'os', cnt, 'cnt', max_cnt, 'max_cnt')
            o.popleft()
            i+=1
            
            print('2222222222222222')

        # print(box[i*2-1])
    print(max_cnt, cnt)

# from collections import deque

# T = int(input())
# for t in range(1, T+1):
#     box = list(input().split())
#     n = int(box[0])

#     seq = []  # 실행 순서 저장
#     for i in range(n):
#         robot = box[2*i+1]
#         pos = int(box[2*i+2])
#         seq.append((robot, pos))

#     # 각 로봇의 현재 위치
#     bs, os = 1, 1
#     # 각 로봇이 마지막으로 버튼 누른 시점 (이때부터 움직일 수 있음)
#     b_time, o_time = 0, 0
#     # 전체 시간
#     total_time = 0

#     for robot, pos in seq:
#         if robot == 'B':
#             dist = abs(pos - bs)
#             # B가 움직일 수 있었던 시간
#             move_time = total_time - b_time
#             # 아직 못 간 거리
#             wait = max(0, dist - move_time)
#             # 버튼 누르는 시간 포함
#             total_time += wait + 1
#             bs = pos
#             b_time = total_time
#         else:
#             dist = abs(pos - os)
#             move_time = total_time - o_time
#             wait = max(0, dist - move_time)
#             total_time += wait + 1
#             os = pos
#             o_time = total_time

#     print(total_time)
