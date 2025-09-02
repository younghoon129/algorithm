# # 15:44

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    print(box)
    num = 0
    l = n//2
    for i in range(l+1):
        num += sum(box[l-i][0+i:n-i])  # up
        num += sum(box[l+i][0+i:n-i])  # down
    num -= sum(box[l][0:])
    print(f"#{t} {num}")
