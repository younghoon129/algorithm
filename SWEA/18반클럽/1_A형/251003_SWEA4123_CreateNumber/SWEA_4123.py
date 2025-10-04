# 19:31
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\1_A형\\251003_SWEA4123_MakeNumber\\SWEA_4123_input.txt', 'r')


def dfs(oper, nl):
    


tc = int(input())
for t in range(1, tc+1):
    n = int(input())  # 숫자의 개수
    operate = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_num = float('-inf')
    min_num = float('inf')
    
    dfs(operate, num_list)

# + 2, - 1, * 0, / 1