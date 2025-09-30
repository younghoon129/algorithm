# 23:35 ~ 13: 45
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\IM_last\\250902_SWEA9367_당근의개수\\carrot_input.txt', 'r')

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    box.sort()
    max_num = 0
    min_num = float('inf')
    result = float('inf')
    s_box = set(box)
    carrot = []
    na = n // 2
    for i in s_box:
        carrot.append(box.count(i))

    c_list = [0, 0, 0]
    for i in range(len(carrot)):
        c_list[0] += carrot[i]
        c_list[1] = 0
        for j in range(i+1, len(carrot)):
            c_list[1] += carrot[j]
            c_list[2] = 0
            for k in range(j+1, len(carrot)):
                c_list[2] += carrot[k]
            if 0 < c_list[0] <= na and 0 < c_list[1] <= na and 0 < c_list[2] <= na:
                max_num = max(c_list)
                min_num = min(c_list)
                a = max_num - min_num
                result = min(result, a)
    
    if result != float('inf'):
        print(f"#{t} {result}")
    else:
        print(f"#{t} -1")
    
    
    
    
    
    
    # for i in range(n-1):
    #     if box[i] < box[i+1]:
    #         cnt += 1
    #     else:
    #         cnt = 1
    #     max_cnt = max(max_cnt, cnt)
    # print(f"#{t} {max_cnt}")