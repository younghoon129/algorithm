import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250919_SWEA4008_숫자만들기\\MakeNum.txt', 'r')

def dfs(oper, nl, num, depth):
    global max_num, min_num
    
    if depth == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    for idx, op_num in enumerate(oper):
        if op_num == 0:
            continue
        ex_num = num
        if idx == 0:
            ex_num += nl[depth]
        if idx == 1:
            ex_num -= nl[depth]
        if idx == 2:
            ex_num *= nl[depth]
        if idx == 3:
            if nl[depth] == 0:
                return
            ex_num = int(ex_num / nl[depth])
        oper[idx] -= 1
        dfs(oper, nl, ex_num, depth+1)
        oper[idx] += 1

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    oper = list(map(int, input().split()))
    nl = list(map(int, input().split()))
    max_num = float('-inf')
    min_num = float('inf')
    num = nl[0]
    dfs(oper, nl, num, 1)
    print(f"#{t} {max_num - min_num}")
