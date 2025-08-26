# 8:15
from itertools import combinations as co
import sys
sys.stdin = open("4128.txt", "r")

test = int(input())

for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    isum = 0
    for i in range(1, n):
        isum += i
    mix = [0]*isum
    cnt = -1
    for i in range(n):
        for j in range(n):
            if i < j:
                cnt += 1
                mix[cnt] = box[i][j] + box[j][i]

    print(mix)
