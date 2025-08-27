# 22 : 05 ~ 22 :10

m = []
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        m.append(i)
print(*m)