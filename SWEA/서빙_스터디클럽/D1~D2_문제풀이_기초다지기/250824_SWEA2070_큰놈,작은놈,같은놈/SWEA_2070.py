# 22 : 43 ~ 22 : 45
test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    result = ''
    if n > m:
        result = '>'
    elif n == m:
        result ='='
    else:
        result = '<'
    print(f"#{t} {result}") 