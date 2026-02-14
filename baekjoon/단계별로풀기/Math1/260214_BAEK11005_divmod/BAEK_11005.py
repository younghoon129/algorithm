n, b = map(int, input().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""

while n:
    n, r = divmod(n, b)
    res += tmp[r]

print(res[::-1])