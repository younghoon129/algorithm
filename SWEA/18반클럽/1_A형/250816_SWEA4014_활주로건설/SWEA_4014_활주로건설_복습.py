

num = int(input())
box = [[0]*1001 for _ in range(1001)]
cnt = 1

for n in range(num):  # 색종이 수
    y, h, gr,sr = map(int, input().split())
    for i in range((1001-y-1), (1001-y-1-sr), -1):
        for j in range(y, y+gr):
            box[i][j] = cnt
    
    cnt += 1
a= [0]*num
for pa in box:
    for c in range(1, cnt):
        a[c-1]+=pa.count(c)

print(a)