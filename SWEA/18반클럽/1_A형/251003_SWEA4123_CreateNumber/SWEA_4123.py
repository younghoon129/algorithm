# 19:31
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\1_A형\\251003_SWEA4123_CreateNumber\\SWEA_4123_input.txt', 'r')


def dfs(op, idx, res):
    global max_num, min_num

    if idx == n:
        max_num = max(max_num, res)
        min_num = min(min_num, res)
        return
    
    for op_idx, op_cnt in enumerate(op):
        if op_cnt == 0:
            continue
        tmp_res = res
        if op_idx == 0:
            tmp_res += num_list[idx]
        elif op_idx == 1:
            tmp_res -= num_list[idx]
        elif op_idx == 2:
            tmp_res *= num_list[idx]
        elif op_idx == 3:
            if num_list[idx] == 0:
                return
            tmp_res = int(tmp_res / num_list[idx])
        
        op[op_idx] -= 1
        dfs(op, idx +1, tmp_res)
        op[op_idx] += 1


tc = int(input())
for t in range(1, tc+1):
    n = int(input())  # 숫자의 개수
    operate = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_num = float('-inf')
    min_num = float('inf')
    init_num = num_list[0]
    init_idx = 1
    dfs(operate, init_idx, init_num)
    print(f"#{t} {max_num - min_num}")