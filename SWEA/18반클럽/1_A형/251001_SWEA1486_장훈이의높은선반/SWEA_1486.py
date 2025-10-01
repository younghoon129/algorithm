# b보다 큰데 그 중 가장 낮은거

def dfs(arr, st, cnt):
    global result
    if cnt >= b:
            result = min(result, cnt)
    if st == n:
        return
    dfs(arr, st+1, cnt+arr[st])
    dfs(arr, st+1, cnt)


tc = int(input())
for t in range(1, tc+1):
    n, b = map(int, input().split())
    box = list(map(int, input().split()))
    result = float('inf')
    cnt = 0
    dfs(box, 0, cnt)
    print(f"#{t} {result-b}")