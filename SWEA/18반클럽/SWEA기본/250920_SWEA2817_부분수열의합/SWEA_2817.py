def sl(idx, b_sum):
    global result
    if b_sum == k:
        result+=1
        return

    if b_sum > k: return
    if idx == len(box): return
    sl(idx+1, b_sum+box[idx])
    sl(idx+1, b_sum)
    
tc = int(input())
for t in range(1, tc+1):
    n, k = map(int,input().split())
    box = list(map(int, input().split()))
    result = 0
    sl(0, 0)

    print(f"#{t} {result}")