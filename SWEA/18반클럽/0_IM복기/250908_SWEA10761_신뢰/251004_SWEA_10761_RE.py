import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\0_IM복기\\250908_SWEA10761_신뢰\\SWEA10761_신뢰.txt', 'r')
from collections import deque

tc = int(input())
for t in range(1, tc+1):
    box = list(map(str, input().split()))
    o_list = deque()
    b_list = deque()
    word = deque()
    for i in range(1, len(box), 2):
        if box[i] == 'B':
            b_list.append(int(box[i+1]))
            word.append(box[i])
        else:
            o_list.append(int(box[i+1]))
            word.append(box[i])
    
    b_st = 1
    o_st = 1
    cnt = 0
    while o_list or b_list:
        cnt += 1
        text = word[0]
        if o_list:
            if o_list[0] > o_st:
                o_st += 1
            elif o_list[0] < o_st:
                o_st -= 1
            elif text == 'O':
                word.popleft()
                o_list.popleft()

        if b_list:
            if b_list[0] > b_st:
                b_st += 1
            elif b_list[0] < b_st:
                b_st -= 1
            elif text == 'B':
                word.popleft()
                b_list.popleft()
        
    print(f"#{t} {cnt}")