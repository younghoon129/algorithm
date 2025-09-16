import sys
sys.stdin = open('GraphLine_input.txt', 'r')

def dfs(current, box):
    global ans
    if current == g:
        ans = 1
    for i in range(len(box)):
        if box[current][i]:
            dfs(i, box)

test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [[0]*n for _ in range(n)]

    for i in range(m+1):
        if i < m:
            ff, ee = map(int, input().split())
            f = ff-1
            e = ee-1
            box[f][e] = 1
        elif i == m:
            ss, gg = map(int, input().split())
            s = ss-1
            g = gg-1
    ans = 0
    dfs(s, box)
    print(f"#{t} {ans}")