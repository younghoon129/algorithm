

num = int(input())
box = [[0]*100 for _ in range(100)]
cnt = 1
num_li = [0]
for n in range(num):  # 색종이 수
    y, h, gr,sr = map(int, input().split())
    for i in range((100-y-1), (100-y-1-sr), -1):
        for j in range(y, y+gr):
            box[i][j] = cnt
    cnt += 1
a= 0
b= 0
for pa in box:
    a+=pa.count(1)
    b+=pa.count(2)

print(a, b)