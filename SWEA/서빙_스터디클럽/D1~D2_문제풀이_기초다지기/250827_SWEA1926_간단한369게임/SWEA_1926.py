# 22 : 16 ~ 22 : 36


n = int(input())
box = [str(n) for n in range(1,n+1)]
for i in range(n):
    cnt = 0
    for j in box[i]:
        if j in '369':
            cnt += 1
    if cnt == 0:
        pass
    elif cnt >0:
        box[i] = ('-'*cnt)


print(*box)

