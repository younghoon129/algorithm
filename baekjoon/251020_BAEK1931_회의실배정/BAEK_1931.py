import sys
sys.stdin = open('BAEK_1931_input.txt', 'r')

# 85에서 틀림
n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
box.sort(key= lambda x:x[1])
cnt = 1
i = 0
W_ex = True
if len(box) >= 2:
    while W_ex:
        for j in range(i+1, n):
            if box[i][1] <= box[j][0]:
                cnt += 1
                print(box[i][1], box[j][0])
                i = j
                break
        else:
            W_ex = False
print(cnt)