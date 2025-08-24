# 22: 48 ~ 22 : 58

n = int(input())
box = list(map(int, input().split()))
box.sort()
a = int(len(box)/2)
print(f"{box[a]}")
