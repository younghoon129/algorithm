import sys
sys.stdin = open('C://Users//SSAFY//Desktop//김영훈//algorithm//SWEA//18반클럽//0_IM복기//250908_SWEA10761_신뢰//SWEA10761_신뢰.txt', 'r')
from collections import deque
test = int(input())
for t in range(1, test+1):
    box = list(input().split())
    b = deque()  # 숫자
    o = deque()  # 숫자
    bst = 1
    ost = 1
    for i in range(int(box[0])):
        if box[(2*i)+1] == 'B':
            b.append(int(box[2*(i+1)]))
        elif box[(2*i)+1] == 'O':
            o.append(int(box[2*(i+1)]))
    time=0
    i = 1
    while b or o:  # b나 o 누를 버튼이 있으면 실행
        time+=1
        text = box[i*2-1]
        if b:
            if b[0] > bst:
                bst+=1
            elif b[0] < bst:
                bst -=1
            elif text == 'B':
                # max_cnt += cnt
                # cnt = 0
                b.popleft()
                i+=1
        if o:
            if o[0] > ost:
                ost+=1
            elif o[0] < ost:
                ost-=1
            elif text == 'O':
            # max_cnt += cnt
            # cnt = 0
                o.popleft()
                i+=1
        
    print(f"#{t} {time}")
