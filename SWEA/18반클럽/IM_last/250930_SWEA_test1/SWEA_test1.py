import sys
sys.stdin = open("C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\IM_last\\250930_SWEA_test1\\test_input.txt", "r")

tc = int(input())

for t in range(1, tc+1):
    n, l, u = map(int, input().split())
    box = list(map(int, input().split()))
    box.sort()
    # print(box)
    min_num = float('inf')
    result = float('inf')    
    max_num = 0
    s_box = set(box)
    n_box = []
    for i in s_box:
        n_box.append(box.count(i))
    # print(n_box)
    grade = [0, 0, 0]
    for i in range(len(n_box)):
        grade[0] += n_box[i]
        grade[1] = 0
        grade[2] = 0
        for j in range(i+1, len(n_box)):
            grade[1] += n_box[j]
            grade[2] = 0
            for k in range(j+1, len(n_box)):
                grade[2] += n_box[k]
            if l <= grade[0] <= u and l <= grade[1] <= u and l <= grade[2] <= u:
                # print(grade, '@@@@@@@@@@@@@', l, u)
                max_num = max(grade)
                min_num = min(grade)
                a = max_num - min_num
                result = min(result, a)
                # print(a, max_num, min_num, result)

    if result != float('inf'):
        print(result)
    else:
        print(-1)