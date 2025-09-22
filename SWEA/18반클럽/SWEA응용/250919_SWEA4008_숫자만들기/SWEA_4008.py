# from collections import deque
# # deque에 숫자들 넣기
import sys
# sys.stdin = open('/SWEA/18반클럽/SWEA기본/숫자만들기/MakeNum.txt', 'r')
def dfs(arr, dep, p, m ,x, d):  # arr : 
    global max_num, min_num
    if dep == n:
        
        max_num = max(max_num, arr)
        min_num = min(min_num, arr)
        return
    
    if p > 0:
        dfs(arr+box[dep], dep+1, p-1, m, x, d)

    if m > 0:
        dfs(arr-box[dep], dep+1, p, m-1, x, d)
    if x > 0:
        dfs(arr*box[dep], dep+1, p, m, x-1, d)
    if d > 0:
        # if arr == 0:
        #     dfs(0, dep+1, p, m, x, d-1)
        if arr < 0:
            dfs(-(-arr//box[dep]), dep+1, p, m, x, d-1)
        else:
            dfs(arr//box[dep], dep+1, p, m, x, d-1)


# def dfs(depth, value, plus, minus, mul, div):
#     global max_num, min_num, n, box
#     if depth == n:
#         max_num = max(max_num, value)
#         min_num = min(min_num, value)
#         if max_num == 16:
#             print(depth, value, plus, minus, mul, div)
        
#         return

#     if plus > 0:
#         dfs(depth + 1, value + box[depth], plus - 1, minus, mul, div)
#     if minus > 0:
#         dfs(depth + 1, value - box[depth], plus, minus - 1, mul, div)
#     if mul > 0:
#         dfs(depth + 1, value * box[depth], plus, minus, mul - 1, div)
#     if div > 0:
#         if value < 0:
#             dfs(depth + 1, int(-value / box[depth]), plus, minus, mul, div - 1)
#         else:
#             dfs(depth + 1, value // box[depth], plus, minus, mul, div - 1)

test = int(input())
for t in range(1, test+1):
    n = int(input())  # 숫자의 개수
    p, m, x, d = map(int, input().split())  # 연산자
    box = list(map(int, input().split()))  # 숫자
    max_num = float('-inf')
    min_num = float('inf')
    c_num = 0
    dfs(box[0],1,  p, m, x, d)

    print(f"#{t} {max_num-min_num}")


# 5
# 2 1 0 1
# 3 5 3 7 9

# def dfs(depth, value, plus, minus, mul, div):
#     global max_value, min_value, N, numbers
#     if depth == N:
#         max_value = max(max_value, value)
#         min_value = min(min_value, value)
#         return

#     if plus > 0:
#         dfs(depth + 1, value + numbers[depth], plus - 1, minus, mul, div)
#     if minus > 0:
#         dfs(depth + 1, value - numbers[depth], plus, minus - 1, mul, div)
#     if mul > 0:
#         dfs(depth + 1, value * numbers[depth], plus, minus, mul - 1, div)
#     if div > 0:
#         if value < 0:
#             dfs(depth + 1, int(-value / numbers[depth]), plus, minus, mul, div - 1)
#         else:
#             dfs(depth + 1, value // numbers[depth], plus, minus, mul, div - 1)


# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     plus, minus, mul, div = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     max_value = -1e9
#     min_value = 1e9
#     dfs(1, numbers[0], plus, minus, mul, div)

#     print(f"#{t} {max_value - min_value}")

    # -------------gpt





