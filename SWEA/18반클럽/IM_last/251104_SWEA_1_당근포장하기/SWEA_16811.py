import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\IM_last\\251104_SWEA_1_당근포장하기\\SWEA_16811_input.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = list(map(int, input().split()))
    bl = set(box)
    box.sort()
    rl = []
    limit = n // 2

    min_num = float('inf')
    max_num = 0
    num = 0
    result = float('inf')
    for i in bl:
        rl.append(box.count(i))
    
    a = 0

    for i in range(len(rl)):
        a+=rl[i]
        b = 0
        for j in range(i+1, len(rl)):
            b+=rl[j]
            c = 0
            for k in range(j+1, len(rl)):
                c+=rl[k]
            if 0 < a <= limit and 0 < b <= limit and 0 < c <= limit:
                num = max(a, b, c) - min(a, b, c)
                result = min(result, num)
    
    if result == float('inf'):
        result = -1
    print(f"#{t} {result}")