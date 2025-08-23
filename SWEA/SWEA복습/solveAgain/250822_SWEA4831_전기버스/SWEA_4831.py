# 17:05 ~ 17 : 50
import sys
sys.stdin = open("C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA복습\\solveAgain\\250822_SWEA4831_전기버스\\sample_input (1).txt", "r")

test = int(input())
for t in range(1, test+1):
    k,n,m = map(int, input().split())
    bs = [0]*(n+1)
    box = list(map(int, input().split()))
    cnt = 0
    for b in box:
        bs[b] = b

    i = 0
    while i+k < n:
        nc = i + k
        while nc > i and nc not in bs:
            nc -= 1
        if nc == i:
            cnt = 0
            break
        i = nc
        cnt += 1

                    
    print(cnt)
