import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250919_SWEA4008_숫자만들기\\MakeNum.txt', 'r')

# def dfs(pl, mi, go, na, sum_num, depth):
#     global max_num, min_num
#     if depth == n:
#         max_num = max(max_num, sum_num)
#         min_num = min(min_num, sum_num)
#         return
#     if pl > 0:
#         dfs(pl-1, mi, go, na, sum_num+box[depth], depth+1)
        
#     if mi > 0:
#         dfs(pl, mi-1, go, na, sum_num-box[depth], depth+1)
        
#     if go > 0:
#         dfs(pl, mi, go-1, na, sum_num*box[depth], depth+1)
        
#     if na > 0:
#         if sum_num == 0:
#             return
#         res = int(sum_num / box[depth])
#         dfs(pl, mi, go, na-1, res, depth+1)
    
def dfs(pl, mi, go, na, sum_num, depth):  # arr : 
    global max_num, min_num
    if depth == n:
         
        max_num = max(max_num, sum_num)
        min_num = min(min_num, sum_num)
        return
     
    if pl > 0:
        dfs(pl-1, mi, go, na, sum_num+box[depth], depth+1)
 
    if mi > 0:
        dfs(pl, mi-1, go, na, sum_num-box[depth], depth+1)
    if go > 0:
        dfs(pl, mi, go-1, na, sum_num*box[depth], depth+1)
    if na > 0:
        # if sum_num == 0:
        #     dfs(0, depth+1, p, m, x, d-1)
        if sum_num < 0:
            dfs(pl, mi, go, na-1, -(-sum_num//box[depth]), depth+1)
        else:
            dfs(pl, mi, go, na-1, sum_num//box[depth], depth+1)

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    pl, mi, go, na = map(int, input().split())
    box = list(map(int, input().split()))
    sum_num = box[0]
    depth = 1
    max_num = -100000000
    min_num = 100000000
    dfs(pl, mi, go, na, sum_num, depth)
    print(f"#{t} {max_num - min_num}")

