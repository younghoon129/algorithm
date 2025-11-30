import sys
sys.stdin = open('BAEK_1316_input.txt', 'r')

n = int(input())

box = [list(map(str, input())) for _ in range(n)]
cnt = n
for i in range(n):
    result = set()
    # print(box[i])
    if len(box[i]) == 1: continue
    for j in range(len(box[i])-1):
        # print(box[i][j])
        # print(result)
        if box[i][j] == box[i][j+1]: continue
        if box[i][j+1] in result:
            cnt -= 1
            break
        result.add(box[i][j])
print(cnt)


