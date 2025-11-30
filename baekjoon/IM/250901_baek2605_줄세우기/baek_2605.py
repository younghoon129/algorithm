n = int(input())
box = list(map(int, input().split()))
stu = []
for i in range(1, n+1):
    if box[i-1] == 0:
        stu.insert(len(box)-1, i)

    else:
        stu.insert(-box[i-1], i)

print(*stu)
