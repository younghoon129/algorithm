import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\SW대비_기본문제_난이도1_3\\251001_SWEA2805_농작물수확하기\\SWEA_2805_input.txt', 'r')
tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    up_num = 0
    down_num = 0
    for i in range((n//2)+1):
        up_num += sum(box[(n//2)-i][0+i:n-i])
        down_num += sum(box[(n//2)+i][0+i:n-i])
    result = up_num + down_num - sum(box[n//2][0:])
    print(f"#{t} {result}")